#!/usr/bin/env python
"""İki noktadan sonra küçük harfle başlayan yerleri listeler (kod blokları, frontmatter anahtarları ve URL'ler hariç).

Kullanım: python scripts/colon_scan.py [--apply kimlikler.txt]
Çıktı: <kimlik>\t<dosya>:<satır>\t<bağlam>
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = [*sorted((ROOT/"content").rglob("*.md")), *sorted((ROOT/"content").rglob("*.mdx")),
         ROOT/"content/data/course.json", ROOT/"content/data/modules.json",
         *sorted((ROOT/"src/pages").rglob("*.astro")), *sorted((ROOT/"src/components").glob("*.astro")),
         *sorted((ROOT/"public/araclar").glob("*.html")), *sorted((ROOT/"public/materyal").rglob("*.txt"))]
PAT = re.compile(r"(: )([a-zçğıöşü])")
LOWER_UP = {"i": "İ", "ı": "I", "ç": "Ç", "ğ": "Ğ", "ö": "Ö", "ş": "Ş", "ü": "Ü"}
YAML_KEY = re.compile(r"^\s*-?\s*[A-Za-z_]+: ")

def hits():
    for f in FILES:
        in_code = False
        fm = 0
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if f.suffix in (".md", ".mdx"):
                if line.strip() == "---": fm += 1
                if line.lstrip().startswith("```"): in_code = not in_code; continue
                if in_code: continue
            for m in PAT.finditer(line):
                pre = line[:m.start()]
                # YAML/JSON anahtarından hemen sonraki iki nokta değilse al
                if f.suffix in (".md", ".mdx") and fm < 2 and YAML_KEY.match(line) and m.start() == YAML_KEY.match(line).end() - 2: continue
                if f.suffix == ".json" and pre.rstrip().endswith('"'): continue
                if f.suffix in (".astro", ".html") and re.search(r"[\w-]$", pre) and re.search(r"(style|class|font|color|background|border|padding|margin|display|gap|width|height|position|const|let|var|return|\{|;)\s*[^<>]*$", pre): continue
                yield f, n, m, line

def main():
    rows = list(hits())
    if "--apply" in sys.argv:
        ids = {int(x) for x in Path(sys.argv[sys.argv.index("--apply")+1]).read_text().split()}
        by = {}
        for i, (f, n, m, line) in enumerate(rows):
            if i in ids: by.setdefault(f, []).append((n, m.start(2)))
        for f, lst in by.items():
            L = f.read_text(encoding="utf-8").split("\n")
            for n, pos in lst:
                ch = L[n-1][pos]
                L[n-1] = L[n-1][:pos] + LOWER_UP.get(ch, ch.upper()) + L[n-1][pos+1:]
            f.write_text("\n".join(L), encoding="utf-8")
        print(f"{len(ids)} yer düzeltildi, {len(by)} dosya"); return
    for i, (f, n, m, line) in enumerate(rows):
        a, b = max(0, m.start()-55), min(len(line), m.end()+60)
        print(f"{i}\t{f.relative_to(ROOT)}:{n}\t…{line[a:b]}…")

if __name__ == "__main__":
    main()
