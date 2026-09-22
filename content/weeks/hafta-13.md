---
week: 13
title: "Makine Öğrenmesine Giriş II: Model Değerlendirme ve ROC"
topic: "Makine öğrenmesine giriş II: model değerlendirme (duyarlılık/özgüllük, ROC) ve tıpta önemi"
description: "Karışıklık matrisi, duyarlılık, özgüllük, PPV/NPV, ROC eğrisi ve eşik seçimi."
module: m4
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "ROC"
  - "duyarlılık"
  - "özgüllük"
  - "karışıklık matrisi"
  - "AUC"
objectives:
  - "Karışıklık matrisinden duyarlılık, özgüllük, PPV ve NPV hesaplar."
  - "ROC eğrisini çizer ve AUC'yi yorumlar."
  - "Klinik bağlama göre karar eşiğini tartışır."
tools:
  - "scikit-learn"
  - "Matplotlib"
---

## Ders Notları

> [!not] Bu bölüm ders notlarının genişletileceği alandır. Haftanın özgün konu başlığı: **Makine öğrenmesine giriş II: model değerlendirme (duyarlılık/özgüllük, ROC) ve tıpta önemi**

Ders notları ilerleyen haftalarda buraya eklenecektir.

## Temel Kavramlar

- **Karışıklık matrisi** — Doğru/yanlış pozitif ve negatif sayılarının tablosu.
- **Duyarlılık / özgüllük** — Hastaları yakalama ve sağlıklıları doğru ayırma oranları.
- **ROC eğrisi ve AUC** — Tüm eşiklerde duyarlılık–özgüllük dengesini gösteren eğri ve altındaki alan.
- **Eşik** — Modelin “pozitif” demeye başladığı olasılık sınırı; klinik maliyete göre seçilir.

## Tıptan Örnekler

- Tarama testinde duyarlılığı yüksek tutmanın yanlış pozitif maliyeti.
- Sepsis uyarı modelinde eşik düşürülünce alarm yorgunluğu.

## Uygulama / Etkinlik

Geçen haftaki modelin ROC eğrisini çizin; AUC hesaplayın ve iki farklı eşikte duyarlılık/özgüllüğü karşılaştırın.

## Tartışma Soruları

1. Doğruluk (accuracy) tıpta neden çoğu zaman yanıltıcı bir ölçüttür?

## Haftanın Özeti

Bir modelin klinik açıdan iyi olup olmadığını değerlendirmenin doğru ölçütlerini öğrendik.
