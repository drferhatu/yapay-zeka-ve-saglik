---
week: 12
title: "Makine Öğrenmesine Giriş I: Denetimli Öğrenme ve İlk Model"
topic: "Makine öğrenmesine giriş I: denetimli öğrenme, eğitim/test ayrımı, basit sınıflandırma"
description: "Denetimli öğrenme kavramı, eğitim/test ayrımı ve scikit-learn ile ilk sınıflandırma modeli."
module: m4
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "makine öğrenmesi"
  - "scikit-learn"
  - "sınıflandırma"
  - "eğitim/test"
objectives:
  - "Denetimli öğrenmeyi ve etiketli veri kavramını açıklar."
  - "Veriyi eğitim ve test kümelerine ayırmanın nedenini kavrar."
  - "scikit-learn ile lojistik regresyon veya karar ağacı modeli eğitir."
tools:
  - "scikit-learn"
  - "Pandas"
---

## Ders Notları

> [!not] Bu bölüm ders notlarının genişletileceği alandır. Haftanın özgün konu başlığı: **Makine öğrenmesine giriş I: denetimli öğrenme, eğitim/test ayrımı, basit sınıflandırma**

Ders notları ilerleyen haftalarda buraya eklenecektir.

## Temel Kavramlar

- **Denetimli öğrenme** — Girdi ve doğru cevap (etiket) çiftlerinden öğrenen yöntem.
- **Özellik (feature)** — Modelin kullandığı girdi değişkeni; yaş, HbA1c gibi.
- **Eğitim / test ayrımı** — Modelin görmediği veride sınanması; ezberlemeyi ortaya çıkarır.
- **Aşırı öğrenme (overfitting)** — Modelin eğitim verisini ezberleyip yeni veride başarısız olması.

## Tıptan Örnekler

- Yaş, VKİ ve glukoz ile diyabet tanısı öngören basit model.
- Klinik verilerden kalp hastalığı varlığını sınıflandırma.

## Uygulama / Etkinlik

Diyabet veri setini eğitim/test olarak bölün; lojistik regresyon eğitin ve test doğruluğunu hesaplayın.

## Tartışma Soruları

1. Model eğitim verisinde %99 doğru ama test verisinde %70 ise ne olmuştur?

## Haftanın Özeti

Bilgisayarın veriden nasıl “öğrendiğini” gördük ve ilk tahmin modelimizi kurduk.
