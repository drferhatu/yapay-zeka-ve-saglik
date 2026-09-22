#!/usr/bin/env python
"""Haftalık Colab defterlerini üretir ve sitede gömülmek üzere HTML'e çevirir.

- notebooks/hafta-XX.ipynb dosyalarını (yoksa) bu dosyadaki tanımlardan oluşturur.
- İsteğe bağlı çalıştırır (--execute): internet gereken/anahtar isteyen hücreler
  anahtar yoksa dostça mesaj basar, hata vermez.
- nbconvert ile public/notebooks/hafta-XX.html üretir (site içinde iframe olarak gömülür).

Kullanım:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/build_notebooks.py [--execute] [--force]
"""
import sys
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

ROOT = Path(__file__).resolve().parent.parent
NB_DIR = ROOT / "notebooks"
OUT_DIR = ROOT / "public" / "notebooks"
REPO = "drferhatu/yapay-zeka-ve-saglik"

md, code = new_markdown_cell, new_code_cell

# --------------------------------------------------------------------------
# HAFTA 1 — Yapay zekâ tıbbı nasıl dönüştürüyor? İlk kod
# --------------------------------------------------------------------------
WEEK01 = [
md(f"""# Hafta 1 · Yapay Zekâ Tıbbı Nasıl Dönüştürüyor? İlk Kod

**Yapay Zeka ve Sağlık** · Fırat Üniversitesi Tıp Fakültesi

Bu defter dersin ilk saatinde birlikte çalıştıracağımız kodları içerir. Hiçbir şey kurmanız gerekmez:
sağ üstteki **Bağlan** düğmesine basın, sonra her hücrenin solundaki ▶ simgesine tıklayın (veya `Shift+Enter`).

> Amaç bugün Python öğrenmek değil; *bir hekimin tarayıcıdan çıkmadan gerçek veriyle ve yapay zekâyla neler yapabildiğini* görmek.
"""),
md("""## 0 · Merhaba

Bilgisayara bir şey söyletmek için `print()` kullanırız. Tırnak içindeki metni ekrana yazar."""),
code('print("Merhaba! Bu ders için yazdığım ilk satır.")'),
md("""Şimdi adınızı yazın ve çalıştırın. Hata alırsanız korkmayın; hata mesajı bize ne olduğunu söyler."""),
code('ad = "Adınızı buraya yazın"\nprint("Merhaba", ad, "— Yapay Zeka ve Sağlık dersine hoş geldin.")'),
md("""## 1 · Hesap makinesinden fazlası: ilk klinik hesap

Bir hastanın kilosu ve boyu var. Vücut kitle indeksini (VKİ) elle hesaplamak yerine bilgisayara hesaplatıyoruz.
`kilo` ve `boy` birer **değişken**: bir değeri isimle saklayan kutu."""),
code('''kilo = 82      # kg
boy = 1.74     # m

vki = kilo / boy ** 2
print("VKİ:", round(vki, 1))

if vki < 18.5:
    print("Zayıf")
elif vki < 25:
    print("Normal")
elif vki < 30:
    print("Fazla kilolu")
else:
    print("Obez")'''),
md("""> **Deneyin:** `kilo` değerini 60 yapın ve hücreyi yeniden çalıştırın. Sınıflama değişti mi?"""),
md("""## 2 · Tek hasta değil, tüm servis

Asıl güç, aynı işlemi yüzlerce hasta için tek seferde yapabilmekte. Aşağıda 8 hastanın kilo/boy listesi var.
Bir **döngü** ile hepsini dolaşıyoruz."""),
code('''hastalar = [
    ("H1", 82, 1.74), ("H2", 58, 1.62), ("H3", 95, 1.80), ("H4", 70, 1.68),
    ("H5", 110, 1.71), ("H6", 49, 1.60), ("H7", 77, 1.85), ("H8", 88, 1.66),
]

for kod, kilo, boy in hastalar:
    vki = kilo / boy ** 2
    uyari = "  ← dikkat" if vki >= 30 else ""
    print(f"{kod}: VKİ {vki:4.1f}{uyari}")'''),
md("""## 3 · Gerçek bir sağlık veri seti, 3 satırda

Şimdi internetten gerçek bir veri seti indiriyoruz: **Pima Kızılderilileri Diyabet Veri Seti** (768 kadın hasta,
glukoz, kan basıncı, VKİ, yaş ve diyabet tanısı). Bu, dünyada makine öğrenmesi öğretiminde en çok kullanılan tıbbi veri setlerinden biri.

`pandas` kütüphanesi tablo verisiyle çalışmak için; Excel gibi düşünün ama programlanabilir."""),
code('''import pandas as pd

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
sutunlar = ["gebelik", "glukoz", "kan_basinci", "cilt_kalinligi", "insulin", "vki", "soyagaci", "yas", "diyabet"]

try:
    df = pd.read_csv(url, names=sutunlar)
except Exception as e:  # çevrimdışı çalışıyorsak küçük bir örnek üret
    import numpy as np
    rng = np.random.default_rng(0)
    df = pd.DataFrame({"gebelik": rng.integers(0, 10, 768), "glukoz": rng.normal(120, 30, 768).round(),
        "kan_basinci": rng.normal(70, 12, 768).round(), "cilt_kalinligi": rng.normal(20, 10, 768).round(),
        "insulin": rng.normal(80, 100, 768).clip(0).round(), "vki": rng.normal(32, 7, 768).round(1),
        "soyagaci": rng.random(768).round(3), "yas": rng.integers(21, 70, 768), "diyabet": rng.integers(0, 2, 768)})
    print("İnternet yok; sentetik örnek veri kullanılıyor.")

print("Satır sayısı (hasta):", len(df))
df.head()'''),
md("""Her satır bir hasta, her sütun bir ölçüm. Son sütun `diyabet`: 1 = tanı var, 0 = yok.

Bir bakışta özet istatistik:"""),
code('df.describe().round(1)'),
md("""**Klinik soru:** Diyabetli hastaların glukoz ortalaması diyabetsizlerden ne kadar farklı? Elle saatler sürecek işlem, tek satır:"""),
code('''df.groupby("diyabet")[["glukoz", "vki", "yas"]].mean().round(1)'''),
md("""## 4 · Veriyi görmek

Sayı tablosu yerine grafik. Glukoz dağılımını diyabet durumuna göre çiziyoruz."""),
code('''import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
for etiket, renk, ad in [(0, "#0f4c5c", "Diyabet yok"), (1, "#e4572e", "Diyabet var")]:
    ax.hist(df.loc[df.diyabet == etiket, "glukoz"], bins=30, alpha=0.6, color=renk, label=ad)
ax.axvline(126, color="black", linestyle="--", linewidth=1)
ax.text(128, ax.get_ylim()[1] * 0.9, "126 mg/dL eşiği", fontsize=9)
ax.set_xlabel("Açlık glukozu (mg/dL)")
ax.set_ylabel("Hasta sayısı")
ax.set_title("Glukoz dağılımı — diyabet durumuna göre")
ax.legend()
plt.tight_layout()
plt.show()'''),
md("""> **Tartışma:** İki dağılım örtüşüyor. Tek başına glukoz tanı koymaya yeter mi? Bu örtüşme, ileride öğreneceğimiz *duyarlılık/özgüllük* kavramının ta kendisi."""),
md("""## 5 · Bir dakikada "yapay zekâ": bilgisayar kendi kuralını öğreniyor

Şimdiye kadar kuralı **biz** yazdık (VKİ eşikleri). Makine öğrenmesinde kuralı **veri** yazar.
Aşağıda bilgisayara 768 hastanın verisini verip "diyabeti tahmin et" diyoruz. Bunun nasıl çalıştığını
12–13. haftalarda öğreneceğiz; bugün sadece *olabildiğini* görüyoruz."""),
code('''from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = df[["glukoz", "vki", "yas", "kan_basinci"]]
y = df["diyabet"]

X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_egitim, y_egitim)               # ← öğrenme burada oluyor

dogruluk = model.score(X_test, y_test)
print(f"Modelin hiç görmediği {len(X_test)} hastada doğruluk: %{dogruluk*100:.0f}")'''),
md("""Yeni bir hasta gelsin: 55 yaşında, glukoz 150, VKİ 33, kan basıncı 80. Model ne diyor?"""),
code('''yeni_hasta = pd.DataFrame([[150, 33, 55, 80]], columns=X.columns)
olasilik = model.predict_proba(yeni_hasta)[0, 1]
print(f"Diyabet olasılığı: %{olasilik*100:.0f}")'''),
md("""> **Dikkat:** Bu %'lik bir *tanı* değil, bir *olasılık*. Modelin kimlerde yanıldığını, hangi gruplarda kötü çalıştığını bilmeden klinikte kullanılamaz. Dersin ikinci yarısı tam da bunu sorgulamayı öğretiyor."""),
md("""## 6 · Büyük dil modeline Python'dan soru sormak

ChatGPT'yi tarayıcıda kullandınız. Aynı modelle **kod içinden** de konuşabilirsiniz; böylece yüzlerce hastaya ait
bulguyu otomatik özetletmek, sınav sorusu üretmek, çıktıyı tabloya dökmek mümkün olur.

Bunun için bir **API anahtarı** gerekir. Ders sırasında öğretim üyesinin anahtarıyla çalıştırılacak; kendiniz denemek için:
1. Sol menüde 🔑 **Secrets** bölümüne `LLM_API_KEY` adıyla anahtarınızı ekleyin (Gemini için [aistudio.google.com](https://aistudio.google.com/apikey) ücretsiz anahtar verir).
2. Gerekirse `BASE_URL` ve `MODEL` değerlerini sağlayıcınıza göre değiştirin.

Anahtar yoksa hücre hata vermez, sadece açıklama basar."""),
code('''import os

# Sağlayıcıya göre değiştirilebilir (OpenAI-uyumlu uç noktalar): Gemini, OpenAI, Groq, OpenRouter...
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL = "gemini-2.5-flash"

def anahtar_al():
    try:
        from google.colab import userdata      # Colab'de Secrets
        return userdata.get("LLM_API_KEY")
    except Exception:
        return os.environ.get("LLM_API_KEY")   # yerelde ortam değişkeni

API_KEY = anahtar_al()
print("Anahtar bulundu." if API_KEY else "Anahtar yok — bu bölüm derste öğretim üyesinin anahtarıyla gösterilecek.")'''),
code('''soru = f"""Aşağıdaki tablo bir diyabet veri setinde diyabetli ve diyabetsiz hastaların ortalama değerleridir.
Tıp fakültesi 1. sınıf öğrencisine 3 cümleyle, sade Türkçeyle yorumla. Tanı koyma, sadece veriyi anlat.

{df.groupby("diyabet")[["glukoz", "vki", "yas"]].mean().round(1).to_string()}
"""

if API_KEY:
    try:
        from openai import OpenAI
    except ImportError:
        import subprocess, sys
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "openai"], check=True)
        from openai import OpenAI
    istemci = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    yanit = istemci.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": soru}])
    print(yanit.choices[0].message.content)
else:
    print("Gönderilecek istem (prompt) şuydu:\\n")
    print(soru)'''),
md("""> **Tartışma:** Model bu yorumu nereden biliyor? Yanlış bir şey söylediyse nasıl fark ederiz? Bu soruların yanıtı 17. haftada.

## 7 · Bugün ne gördük?

| Dakika | Ne yaptık | Hangi haftada derinleşecek |
|---|---|---|
| 5 | İlk `print`, değişken | Hafta 2 |
| 10 | VKİ hesabı, koşullar, döngü | Hafta 2–3 |
| 10 | Gerçek veri setini yükleme ve özetleme | Hafta 6–7 |
| 5 | Grafik | Hafta 8–9 |
| 10 | İlk makine öğrenmesi modeli | Hafta 12–13 |
| 5 | Python'dan LLM'e soru | Hafta 17–20 |

**Eve ödev (isteğe bağlı, 10 dk):** Bu defteri kendi Google hesabınıza kopyalayın (Dosya → Drive'a kopya kaydet), bölüm 1'deki VKİ hesabını kendi değerlerinizle çalıştırın ve bölüm 2'deki listeye bir hasta ekleyin.
"""),
]

NOTEBOOKS = {"hafta-01": ("Hafta 1 · İlk Kod", WEEK01)}


def build(name, title, cells, force=False):
    path = NB_DIR / f"{name}.ipynb"
    if path.exists() and not force:
        nb = nbformat.read(path, as_version=4)
        print(f"· {path.name} mevcut, korunuyor")
    else:
        nb = new_notebook(cells=cells, metadata={
            "kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
            "language_info": {"name": "python"},
            "colab": {"name": f"{name}.ipynb", "toc_visible": True},
        })
        nbformat.write(nb, path)
        print(f"✓ {path.name} yazıldı")
    return path


def execute(path):
    from nbclient import NotebookClient
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=180, kernel_name="python3", allow_errors=True,
                            resources={"metadata": {"path": str(path.parent)}})
    client.execute()
    nbformat.write(nb, path)
    errs = [o for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.get("output_type") == "error"]
    print(f"✓ {path.name} çalıştırıldı ({len(errs)} hata hücresi)")


def to_html(path):
    from nbconvert import HTMLExporter
    exp = HTMLExporter(template_name="lab")
    exp.exclude_input_prompt = True
    exp.exclude_output_prompt = True
    body, _ = exp.from_filename(str(path))
    # site zeminiyle uyum ve iframe içinde ferah görünüm
    body = body.replace("</head>", """<style>
      body{background:#fff !important;margin:0}
      .jp-Notebook{padding:16px 20px !important;max-width:100% !important}
      .jp-Cell{padding:0 !important}
      .jp-InputArea-editor{border-radius:10px;border:1px solid #e3ddd2}
      .jp-RenderedHTMLCommon{font-family:Manrope,system-ui,sans-serif;color:#10262e}
      .jp-RenderedHTMLCommon table{font-size:13px}
    </style></head>""")
    out = OUT_DIR / f"{path.stem}.html"
    out.write_text(body, encoding="utf-8")
    print(f"✓ {out.relative_to(ROOT)} ({len(body)//1024} KB)")


def main():
    force = "--force" in sys.argv
    run = "--execute" in sys.argv
    NB_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, (title, cells) in NOTEBOOKS.items():
        p = build(name, title, cells, force)
        if run:
            execute(p)
        to_html(p)
    print(f"\nColab bağlantı biçimi: https://colab.research.google.com/github/{REPO}/blob/main/notebooks/<ad>.ipynb")


if __name__ == "__main__":
    main()
