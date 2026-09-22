---
week: 4
title: "Fonksiyonlar ve Okunabilir Kod: Klinik Hesaplayıcı"
topic: "Fonksiyonlar ve okunabilir kod; basit bir klinik hesaplayıcı geliştirme (ör. eGFR/risk skoru)"
description: "Fonksiyon tanımlama, parametreler, okunabilir kod ilkeleri ve eGFR/risk skoru hesaplayıcısı."
module: m1
semester: 1
exam: false
status: taslak
changeNote: ""
tags:
  - "python"
  - "fonksiyon"
  - "eGFR"
  - "risk skoru"
  - "temiz kod"
objectives:
  - "`def` ile parametre alan ve değer döndüren fonksiyon yazar."
  - "Kodu anlamlı isimler ve açıklamalarla okunabilir hâle getirir."
  - "Bir klinik formülü (eGFR veya risk skoru) yeniden kullanılabilir fonksiyona dönüştürür."
tools:
  - "Google Colab"
---

## Ders Notları

> [!not] Bu bölüm ders notlarının genişletileceği alandır. Haftanın özgün konu başlığı: **Fonksiyonlar ve okunabilir kod; basit bir klinik hesaplayıcı geliştirme (ör. eGFR/risk skoru)**

Ders notları ilerleyen haftalarda buraya eklenecektir.

## Temel Kavramlar

- **Fonksiyon** — Bir işi yapan, isimlendirilmiş ve tekrar çağrılabilen kod bloğu.
- **Parametre / argüman** — Fonksiyona dışarıdan verilen girdiler.
- **Dönüş değeri** — Fonksiyonun `return` ile geri verdiği sonuç.
- **Okunabilirlik** — Kodun başka biri (ya da altı ay sonra siz) tarafından kolay anlaşılması.

## Tıptan Örnekler

- CKD-EPI eGFR formülünü fonksiyon olarak yazıp evre sınıflaması yapma.
- CHA₂DS₂-VASc skorunu hesaplayan fonksiyon.

## Uygulama / Etkinlik

Kreatinin, yaş ve cinsiyet alan bir `egfr()` fonksiyonu yazın; üç farklı hasta için çağırın ve evreyi yazdırın.

## Tartışma Soruları

1. Bir klinik hesaplayıcıda yapılan küçük bir kod hatası nasıl sonuçlar doğurabilir? Bunu nasıl fark ederiz?

## Haftanın Özeti

Fonksiyonlarla kodu parçalara ayırdık ve ilk gerçek klinik hesaplayıcımızı geliştirdik. Python temelleri modülü tamamlandı.
