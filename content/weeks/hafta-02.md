---
week: 2
title: "Python Temelleri I: Değişkenler ve Klinik Hesaplamalar"
topic: "Python temelleri I: değişkenler ve veri tipleri; basit klinik hesaplamalar (ör. VKİ)"
description: "Değişkenler, sayı ve metin tipleri; vücut kitle indeksi gibi basit klinik hesaplamalar."
module: m1
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "python"
  - "değişken"
  - "veri tipi"
  - "VKİ"
  - "BMI"
objectives:
  - "Değişken tanımlar ve sayı, metin, mantıksal (bool) tiplerini ayırt eder."
  - "Aritmetik operatörlerle klinik bir formülü (VKİ) koda çevirir."
  - "Kullanıcıdan alınan girdiyi uygun tipe dönüştürür."
tools:
  - "Google Colab"
---

## Ders Notları

> [!not] Bu bölüm ders notlarının genişletileceği alandır. Haftanın özgün konu başlığı: **Python temelleri I: değişkenler ve veri tipleri; basit klinik hesaplamalar (ör. VKİ)**

Ders notları ilerleyen haftalarda buraya eklenecektir.

## Temel Kavramlar

- **Değişken** — Bir değeri isimle saklayan kutu; `kilo = 72` gibi.
- **Veri tipi** — Değerin türü: tam sayı (int), ondalık (float), metin (str), mantıksal (bool).
- **Tip dönüşümü** — `float("72.5")` gibi bir metni sayıya çevirme işlemi.

## Tıptan Örnekler

- VKİ = kilo / boy² formülünü koda dökme ve DSÖ sınıflamasına göre yorumlama.
- Vücut yüzey alanı (Mosteller) hesabı ile kemoterapi dozu örneği.

## Uygulama / Etkinlik

Boy ve kiloyu değişkenlere atayıp VKİ hesaplayan bir hücre yazın; sonucu iki ondalıkla yazdırın.

## Tartışma Soruları

1. Aynı formülü her hasta için elle hesaplamakla kodla hesaplamak arasında güvenlik açısından ne fark var?

## Haftanın Özeti

Değişkenleri ve temel veri tiplerini öğrenip ilk klinik hesaplayıcımız olan VKİ'yi yazdık.
