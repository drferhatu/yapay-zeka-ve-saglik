---
week: 16
title: "Sağlıkta Tahmin ve Karar Destek: Yanlılık ve Eşitlik"
topic: "Sağlıkta tahmin ve karar destek modelleri; model çıktısını klinik karara çevirme, yanlılık/eşitlik"
description: "Klinik karar destek sistemleri, model çıktısının karara dönüşümü, algoritmik yanlılık ve eşitlik."
module: m5
semester: 2
exam: false
status: taslak
changeNote: ""
tags:
  - "karar destek"
  - "yanlılık"
  - "eşitlik"
  - "tahmin modeli"
  - "CDSS"
objectives:
  - "Klinik karar destek sisteminin bileşenlerini ve iş akışına yerleşimini açıklar."
  - "Bir olasılık çıktısının klinik karara nasıl çevrildiğini örnekler."
  - "Algoritmik yanlılığın kaynaklarını ve etkilenen grupları tanımlar."
tools:
  - "scikit-learn"
  - "Pandas"
---

## Ders Notları

> [!not] Bu bölüm ders notlarının genişletileceği alandır. Haftanın özgün konu başlığı: **Sağlıkta tahmin ve karar destek modelleri; model çıktısını klinik karara çevirme, yanlılık/eşitlik**

Ders notları ilerleyen haftalarda buraya eklenecektir.

## Temel Kavramlar

- **Klinik karar destek (CDSS)** — Hekime karar anında veri temelli öneri sunan sistem.
- **Kalibrasyon** — Modelin %30 dediği hastaların gerçekten yaklaşık %30'unun hasta olması.
- **Algoritmik yanlılık** — Modelin belirli gruplarda sistematik olarak daha kötü çalışması.
- **İnsan denetimi** — Nihai kararın ve sorumluluğun hekimde kalması ilkesi.

## Tıptan Örnekler

- Sepsis erken uyarı skorlarının gerçek hastanelerdeki performansı.
- Deri renginden etkilenen pulse oksimetre ölçümleri ve model yanlılığı; sağlık harcamasını hastalık şiddeti yerine kullanan algoritma örneği.

## Uygulama / Etkinlik

Güz modelinizin performansını cinsiyet veya yaş gruplarına göre ayrı ayrı hesaplayın; fark varsa nedenlerini tartışın.

## Tartışma Soruları

1. Bir model ortalamada iyi ama belirli bir grupta kötü çalışıyorsa kullanıma alınmalı mı?

## Haftanın Özeti

Model çıktılarının klinik karara dönüşümünü ve bu süreçteki eşitlik sorunlarını inceledik.
