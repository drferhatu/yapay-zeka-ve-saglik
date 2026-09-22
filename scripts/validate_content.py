#!/usr/bin/env python
"""İçerik ve derleme doğrulaması.

Kontroller:
  1. content/weeks altında 1..28 haftaların tamamı var mı, numaralar tekil mi?
  2. Her haftanın 'module' alanı modules.json'daki bir modülle eşleşiyor ve
     o modülün 'weeks' listesinde yer alıyor mu?
  3. schedule.json 28 satır içeriyor mu; tarih formatı ve status değerleri geçerli mi?
  4. (dist varsa) Üretilen HTML'deki iç bağlantılar mevcut dosyalara gidiyor mu?

Kullanım:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/validate_content.py
"""
import json
import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
WEEKS_DIR = ROOT / "content" / "weeks"
DATA = ROOT / "content" / "data"
DIST = ROOT / "dist"
BASE = "/yapay-zeka-ve-saglik"
errors: list[str] = []


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        errors.append(f"{path.name}: frontmatter yok")
        return {}
    fm: dict = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm and mm.group(2) != "":
            v = mm.group(2).strip()
            fm[mm.group(1)] = v.strip('"')
    return fm


def check_weeks():
    modules = json.loads((DATA / "modules.json").read_text(encoding="utf-8"))
    mod_by_id = {m["id"]: m for m in modules}
    seen = {}
    for p in sorted(WEEKS_DIR.glob("*.md")):
        fm = frontmatter(p)
        try:
            n = int(fm.get("week", -1))
        except ValueError:
            errors.append(f"{p.name}: week sayısal değil")
            continue
        if n in seen:
            errors.append(f"{p.name}: hafta {n} zaten {seen[n]} dosyasında")
        seen[n] = p.name
        if not fm.get("title"):
            errors.append(f"{p.name}: title eksik")
        mod = fm.get("module")
        if mod not in mod_by_id:
            errors.append(f"{p.name}: bilinmeyen modül '{mod}'")
        elif n not in mod_by_id[mod]["weeks"]:
            errors.append(f"{p.name}: hafta {n}, modül {mod} 'weeks' listesinde yok")
        sem = fm.get("semester")
        exp = "1" if n <= 14 else "2"
        if sem != exp:
            errors.append(f"{p.name}: semester {sem} beklenen {exp}")
    missing = sorted(set(range(1, 29)) - set(seen))
    if missing:
        errors.append(f"Eksik haftalar: {missing}")
    extra = sorted(set(seen) - set(range(1, 29)))
    if extra:
        errors.append(f"Beklenmeyen hafta numaraları: {extra}")
    # modüllerin birleşimi 1..28 olmalı
    union = sorted(w for m in modules for w in m["weeks"])
    if union != list(range(1, 29)):
        errors.append(f"modules.json haftaları 1..28'i tam kapsamıyor: {union}")
    print(f"✓ {len(seen)} hafta dosyası, {len(modules)} modül")


def check_schedule():
    sch = json.loads((DATA / "schedule.json").read_text(encoding="utf-8"))["weeks"]
    nums = [r["week"] for r in sch]
    if nums != list(range(1, 29)):
        errors.append(f"schedule.json hafta sırası 1..28 değil: {nums}")
    for r in sch:
        if r.get("status") not in {"normal", "tatil", "ertelendi", "sinav"}:
            errors.append(f"schedule hafta {r['week']}: geçersiz status '{r.get('status')}'")
        d = r.get("date", "")
        if d:
            try:
                date.fromisoformat(d)
            except ValueError:
                errors.append(f"schedule hafta {r['week']}: geçersiz tarih '{d}' (YYYY-AA-GG olmalı)")
    dated = [r for r in sch if r.get("date")]
    for a, b in zip(dated, dated[1:]):
        if a["date"] > b["date"]:
            errors.append(f"schedule: hafta {a['week']} ({a['date']}) hafta {b['week']} ({b['date']})'den sonra")
    print(f"✓ takvim: {len(dated)}/28 haftanın tarihi girilmiş")


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for key in ("href", "src"):
            if key in a and a[key]:
                self.links.append(a[key])


def check_dist():
    if not DIST.exists():
        print("· dist yok, bağlantı kontrolü atlandı (npm run build sonrası çalıştırın)")
        return
    pages = list(DIST.rglob("*.html"))
    broken = set()
    for page in pages:
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            u = urlsplit(link)
            if u.scheme or link.startswith("#") or link.startswith("mailto:"):
                continue
            # sayfanın URL'sine göre çözümle (klasör sayfaları '/' ile biter)
            page_url = "/" + page.relative_to(DIST).as_posix().replace("index.html", "")
            path = unquote(urlsplit(urljoin(BASE + page_url, link)).path)
            if not path.startswith(BASE + "/") and path != BASE:
                broken.add((page.relative_to(DIST).as_posix(), link, "base dışı"))
                continue
            rel = path[len(BASE):].lstrip("/")
            target = DIST / rel
            ok = target.exists() or (target / "index.html").exists() or (target.with_suffix(".html")).exists()
            if not ok:
                broken.add((page.relative_to(DIST).as_posix(), link, "hedef yok"))
    for b in sorted(broken):
        errors.append(f"kırık bağlantı: {b[0]} → {b[1]} ({b[2]})")
    week_pages = [p for p in pages if "haftalar/hafta-" in p.as_posix()]
    if len(week_pages) != 28:
        errors.append(f"dist'te {len(week_pages)} hafta sayfası var, 28 bekleniyor")
    # Türkçe karakter kontrolü: mojibake izi
    for p in pages:
        t = p.read_text(encoding="utf-8")
        if "Ã" in t or "Å" in t:
            errors.append(f"{p.relative_to(DIST)}: olası karakter kodlama hatası")
            break
    print(f"✓ dist: {len(pages)} sayfa, {len(week_pages)} hafta sayfası, bağlantılar tarandı")


def main():
    check_weeks()
    check_schedule()
    check_dist()
    if errors:
        print("\n✗ HATALAR:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("\nTüm kontroller geçti.")


if __name__ == "__main__":
    main()
