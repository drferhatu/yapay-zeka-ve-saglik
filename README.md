# Yapay Zeka ve Sağlık — Ders Web Sitesi

Fırat Üniversitesi Tıp Fakültesi seçmeli dersi **Yapay Zeka ve Sağlık** için 28 haftalık ders web sitesi.
Site tamamen statiktir, GitHub Pages üzerinde yayımlanır ve tüm ders içeriği koddan ayrı Markdown/JSON dosyalarında tutulur.

Canlı adres: `https://drferhatu.github.io/yapay-zeka-ve-saglik/`

## Teknoloji

| Katman | Seçim | Neden |
|---|---|---|
| Çatı | [Astro 5](https://astro.build) | Sıfır istemci JavaScript varsayılanı, içerik koleksiyonları, statik çıktı |
| Stil | [Tailwind CSS 4](https://tailwindcss.com) | Tasarım sistemini tek CSS dosyasında token olarak tutar |
| İçerik | Markdown + JSON | Haftalar Markdown, ders künyesi/modüller/takvim JSON |
| Arama | [Pagefind](https://pagefind.app) | Derleme sonrası tamamen statik arama dizini, sunucu gerekmez |
| Dağıtım | GitHub Actions → GitHub Pages | `main` dalına her push'ta otomatik derleme ve yayın |

## Klasör yapısı

```
content/
  data/course.json        ders künyesi, amaç, öğrenim çıktıları, değerlendirme, kaynaklar
  data/modules.json       8 modül (başlık, haftalar, renk, özet)
  data/schedule.json      haftalık tarihler ve durumlar (tatil/ertelendi/sınav)
  weeks/hafta-01.md …     28 haftalık ders dosyası (her hafta tek dosya)
  announcements/*.md      duyurular
src/
  pages/                  rotalar (index, ders-hakkinda, ders-akisi, haftalar/, kaynaklar, duyurular, arama)
  components/             yeniden kullanılabilir parçalar (Roadmap, WeekCard, Toc, WeekPager …)
  layouts/BaseLayout.astro
  lib/site.ts             yardımcılar (href, modül/takvim erişimi, tarih biçimi)
  lib/remark-callouts.mjs Markdown uyarı kutuları ([!not], [!uyari], [!ornek], [!neden], [!nerede], [!tanim])
  lib/rehype-base-links.mjs  Markdown'daki /haftalar/... bağlantılarına base yolunu ekler
  styles/global.css       tasarım sistemi (renk, yazı tipi, prose stilleri)
scripts/
  extract_course_docx.py  DOCX ders formunu düz metin/JSON'a çıkarır
  generate_week_files.py  28 haftalık Markdown iskeletini üretir (mevcut dosyaları ezmez)
  validate_content.py     içerik + derleme doğrulaması (haftalar, takvim, kırık bağlantı)
public/                   favicon, og.png, robots.txt, .nojekyll
.github/workflows/deploy.yml  GitHub Pages dağıtımı
```

Kaynak belgeler (DOCX/PDF) çalışma klasöründe olduğu gibi durur; `.gitignore` ile depoya ve siteye dâhil edilmez.

## Yerel geliştirme

Gereksinim: Node.js 22+ (bu makinede Homebrew ile kuruldu: `/opt/homebrew/bin/node`).

```bash
npm install
npm run dev        # http://localhost:4321/yapay-zeka-ve-saglik/  (arama dev'de çalışmaz)
npm run build      # dist/ üretir ve Pagefind dizinini oluşturur
npm run preview    # dist/ klasörünü yerelde sunar (arama dâhil)
```

Python scriptleri için `ferhat_ml` conda ortamı kullanılır:

```bash
/opt/miniconda3/envs/ferhat_ml/bin/python scripts/validate_content.py
```

## İçerik düzenleme

### Bir haftanın konusunu veya notlarını değiştirmek

`content/weeks/hafta-XX.md` dosyasını açın. Üst kısım (frontmatter) haftanın kimliğidir:

```yaml
---
week: 13
title: "Makine Öğrenmesine Giriş II: Model Değerlendirme ve ROC"   # sitede görünen başlık
topic: "Makine öğrenmesine giriş II: ..."                          # resmî ders planındaki satır
description: "Karışıklık matrisi, duyarlılık, özgüllük ..."        # kart ve meta açıklaması
module: m4              # modules.json'daki modül kimliği
semester: 1             # 1 = Güz, 2 = Bahar
exam: false             # true ise "Ara değerlendirme" etiketi
status: taslak          # taslak → "Hazırlık aşamasında" kutusu; notlar bitince hazir yapın
changeNote: ""          # dolu ise sayfada "Program değişikliği" uyarısı çıkar
tags: [...]             # arama ve etiketler
objectives: [...]       # öğrenme hedefleri (numaralı kutular)
tools: [...]            # "Bu haftanın araçları"
resources:              # isteğe bağlı ek kaynaklar
  - { title: "…", url: "https://…", note: "…" }
---
```

Alt kısım serbest Markdown'dır. Önerilen başlıklar: `## Derse Başlamadan Önce`, `## Ders Notları`,
`## Temel Kavramlar`, `## Tıptan Örnekler`, `## Uygulama / Etkinlik`, `## Tartışma Soruları`, `## Haftanın Özeti`.
Boş bırakılan bölümleri silmekte serbestsiniz; içindekiler tablosu `##` başlıklarından otomatik oluşur.

Uyarı kutuları:

```markdown
> [!neden] Neden önemli?
> Doğruluk tıpta yanıltıcıdır çünkü ...

> [!ornek]
> 60 yaşında kadın hasta ...

> [!uyari] Dikkat
> Hasta verisini sohbet botuna girmeyin.
```

Türler: `not`, `uyari`, `ornek`, `neden`, `nerede`, `tanim`. Başlık verilmezse varsayılan kullanılır.

Başka bir haftaya bağlantı vermek için kök yol yazın; base otomatik eklenir: `[13. hafta](/haftalar/hafta-13)`.

### Haftaların tarihini değiştirmek, tatil veya erteleme işlemek

`content/data/schedule.json` içindeki ilgili satırı düzenleyin:

```json
{ "week": 9, "date": "2026-11-18", "status": "tatil", "note": "Resmî tatil; konu 10. haftaya kaydı" }
```

- `date` boşsa yalnızca hafta numarası görünür.
- `status`: `normal` | `tatil` | `ertelendi` | `sinav`. Normal dışı durumlar kartlarda ve hafta sayfasında etiket olarak görünür.
- `note` kısa açıklama olarak gösterilir.

İki haftanın konusunu yer değiştirmek için iki Markdown dosyasının içeriğini takas edin (sadece `week` alanını koruyun) ve `changeNote` ile açıklayın.

### Yeni duyuru eklemek

`content/announcements/` altına yeni bir dosya:

```markdown
---
title: "Ara sınav tarihi"
date: 2026-11-10
pinned: true        # üstte sabit
kind: sinav         # bilgi | onemli | sinav
---
Ara sınav 12 Kasım Perşembe 10.00'da ...
```

### Ders künyesi, öğrenim çıktıları, kaynaklar

`content/data/course.json` içinde. Öğrenim çıktılarının `weeks` alanı, Ders Hakkında sayfasındaki hafta bağlantılarını üretir.

### Modül eklemek/değiştirmek

`content/data/modules.json`. Her haftanın tam olarak bir modülde yer alması gerekir; `validate_content.py` bunu denetler.

## Scriptler

| Script | İş |
|---|---|
| `scripts/extract_course_docx.py "<dosya.docx>" [--json çıktı.json]` | DOCX'teki paragraf ve tabloları düz metin/JSON'a çıkarır |
| `scripts/generate_week_files.py [--force]` | 28 haftalık iskeleti üretir; `--force` olmadan var olan dosyalara dokunmaz |
| `scripts/validate_content.py` | Hafta sayısı, modül eşleşmesi, takvim formatı ve (dist varsa) kırık bağlantıları denetler |

## GitHub Pages dağıtımı

1. Depo: `drferhatu/yapay-zeka-ve-saglik`. Ayarlar → Pages → Source: **GitHub Actions**.
2. `main` dalına push edildiğinde `.github/workflows/deploy.yml` çalışır: `npm ci`, `npm run build`, `dist/` yayınlanır.
3. Base yolu `astro.config.mjs` içinde `/yapay-zeka-ve-saglik` olarak ayarlıdır. Depo adı değişirse bu değeri (ve `public/robots.txt`) güncelleyin. Özel alan adına geçilirse `SITE_URL` ve `BASE_PATH=/` ortam değişkenleriyle derleyin.

İçeriği doğrudan GitHub web arayüzünden de düzenleyebilirsiniz; kaydettiğinizde site birkaç dakika içinde yenilenir.

## Bakım notları

- Yayına almadan önce: `npm run build && python scripts/validate_content.py`.
- Ders notları tamamlanan haftada `status: hazir` yapın; "Hazırlık aşamasında" kutusu kalkar.
- Yazı tipleri Google Fonts'tan yüklenir (Fraunces, Manrope, JetBrains Mono). Çevrimdışı kullanım gerekirse `public/fonts/` altına alıp `BaseLayout.astro` içindeki bağlantıyı değiştirin.
- Bağımlılık güncellemeleri: `npm outdated` / `npm update`; büyük sürüm değişimlerinde derlemeyi yerelde doğrulayın.
