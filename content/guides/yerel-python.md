---
title: "Kendi Bilgisayarında Python"
description: "Windows ve macOS için Miniconda kurulumu, ilk ortamın oluşturulması, Jupyter'in çalıştırılması ve yapay zeka ajanlarının (ör. Claude Code) bu ortamı kullanması."
order: 1
---

## Neden yerel kurulum?

Bu dersin tamamı Google Colab'de yapılabilir; kurulum gerekmez. Yerel kurulum şu durumlarda gerekir:

- **Yapay zeka ajanları** (Claude Code, Cursor, GitHub Copilot gibi) bilgisayarınızdaki bir klasörde sizin adınıza kod yazıp çalıştırmasını istiyorsanız. Bu araçlar bir Python ortamı ister.
- İnternet olmadan ya da hasta verisiyle (kurum izniyle, kurum bilgisayarında) çalışacaksanız.
- Colab'in zaman sınırları ve oturum kesilmeleri sizi yoruyorsa.

> [!not] Süre
> Kurulum yaklaşık 15 dakika sürer ve bir kez yapılır. Takıldığınız yerde ekran görüntüsü alıp bir yapay zeka asistanına "bu adımda ne yapmalıyım?" diye sormak çoğu zaman yeterlidir; yine de çözemezseniz ofis saatinde birlikte bakarız.

## Adım 1 · Miniconda'yı kur

**Conda**, Python sürümlerini ve kütüphaneleri birbirinden ayrı "ortamlarda" tutan bir yöneticidir. Bir projede bozulan bir şey diğerini etkilemez. **Miniconda** bunun küçük kurulum paketidir.

İndirme sayfası: [docs.conda.io → Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Windows

1. "Miniconda3 Windows 64-bit" kurulum dosyasını indirip çalıştırın.
2. Kurulumda **"Just Me"** seçin; "Add Miniconda3 to my PATH" kutusunu işaretlemeyin (varsayılan).
3. Kurulum bitince Başlat menüsünden **Anaconda Prompt (miniconda3)** uygulamasını açın. Komutları buraya yazacaksınız.

### macOS

1. İşlemcinize göre indirin: Apple Silicon (M1/M2/M3/M4) için "arm64", eski Intel Mac için "x86_64". Emin değilseniz sol üst  → Bu Mac Hakkında → "Çip" satırına bakın.
2. `.pkg` dosyasını çalıştırın ve varsayılanlarla ilerleyin.
3. **Terminal** uygulamasını açın (Spotlight'ta "Terminal" yazın). Komut satırının başında `(base)` görünüyorsa kurulum tamam.

### Kontrol

```bash
conda --version
```

`conda 24.x` gibi bir sürüm görüyorsanız hazırsınız.

## Adım 2 · İlk ortamını oluştur

Ders için `tip` adında bir ortam oluşturup ders kütüphanelerini kuruyoruz. Tek komut:

```bash
conda create -n tip python=3.12 numpy pandas matplotlib seaborn scikit-learn jupyterlab -y
```

Ortamı etkinleştirin:

```bash
conda activate tip
```

Komut satırının başındaki `(base)` yazısı `(tip)` olur. Artık yazdığınız her Python komutu bu ortamda çalışır.

> [!uyari] En sık yapılan hata
> Ortamı etkinleştirmeden `python` yazmak. Hangi ortamda olduğunuzu her zaman satır başındaki parantezden kontrol edin. `ModuleNotFoundError: No module named 'pandas'` görüyorsanız büyük olasılıkla yanlış ortamdasınız.

## Adım 3 · Jupyter'i çalıştır

Ders defterlerini kendi bilgisayarınızda açmak için:

```bash
jupyter lab
```

Tarayıcınızda JupyterLab açılır. Colab'den indirdiğiniz `.ipynb` dosyalarını (Dosya → İndir → .ipynb) buraya sürükleyip çalıştırabilirsiniz. Kapatmak için terminalde `Ctrl + C`.

## Adım 4 · Yapay zeka ajanlarıyla çalışmak

Claude Code, Cursor gibi araçlar bir **klasörde** çalışır: o klasördeki dosyaları okur, kod yazar, çalıştırır. Güvenli çalışma düzeni:

1. Ders için ayrı bir klasör açın, örneğin `Belgeler/yz-saglik`. Ajan yalnızca bu klasöre erişsin; tüm diskinize değil.
2. Ajanı bu klasörde başlatın ve ilk mesajınızda ortamı söyleyin:

```
Python için conda "tip" ortamını kullan. Komutları "conda run -n tip python ..." biçiminde çalıştır.
```

3. Ajan bir komut çalıştırmak istediğinde önce **ne yaptığını okuyun**, sonra onaylayın. Silme, indirme ve ağ erişimi isteyen komutlarda iki kez düşünün.
4. Ürettiği kodu çalıştırmadan önce göz gezdirin: `import` satırları, `def` tanımları, dosya yolları. Anlamadığınız satırı ajana açıklattırın.

> [!neden] Neden önemli?
> Ajan, sizin yetkilerinizle çalışır. Klasörü daraltmak ve komutları okumak, "kodu yapay zeka yazsın ama sorumluluk bende kalsın" ilkesinin pratikteki karşılığıdır.

> [!uyari] Hasta verisi
> Yerel kurulum, hasta verisini kişisel bilgisayarınıza almanız için bir gerekçe değildir. Gerçek hasta verisi yalnızca kurumun izin verdiği ortamlarda ve KVKK çerçevesinde işlenir. Bu derste açık ve anonim veri setleri kullanıyoruz.

## Sık karşılaşılan sorunlar

| Belirti | Olası neden | Çözüm |
|---|---|---|
| `conda: command not found` | Terminal Miniconda'yı tanımıyor | Windows'ta Anaconda Prompt kullanın; macOS'ta Terminal'i kapatıp yeniden açın |
| `ModuleNotFoundError` | Yanlış ortam ya da kütüphane kurulmamış | `conda activate tip`, sonra `conda install <paket>` |
| `jupyter lab` açılmıyor | Ortam etkin değil | `conda activate tip` sonra tekrar deneyin |
| Kurulum çok yer kaplıyor | Normal; ~3 GB | Gereksiz ortamları `conda env remove -n <ad>` ile silebilirsiniz |

## Yararlı komutlar

```bash
conda env list                 # tüm ortamları listele
conda activate tip             # ortama gir
conda deactivate               # ortamdan çık
conda install -n tip <paket>   # ortama paket ekle
conda run -n tip python x.py   # ortamı etkinleştirmeden bir dosyayı çalıştır
```
