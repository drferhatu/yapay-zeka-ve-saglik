---
week: 15
title: "Tıbbi Görüntülerde Derin Öğrenme Sezgisi"
topic: "Tıbbi görüntülerde derin öğrenme sezgisi (röntgen/patoloji); hazır modellerle uygulama"
description: "Yapay sinir ağları ve evrişimli ağların (CNN) sezgisel açıklaması; hazır modellerle röntgen/patoloji uygulaması."
module: m5
semester: 2
exam: false
status: taslak
changeNote: ""
tags:
  - "derin öğrenme"
  - "CNN"
  - "tıbbi görüntüleme"
  - "röntgen"
  - "patoloji"
objectives:
  - "Yapay sinir ağının ve evrişimli ağın (CNN) ne yaptığını matematiğe girmeden açıklar."
  - "Hazır bir görüntü modelini çalıştırıp çıktısını yorumlar."
  - "Görüntü modellerinin başarısızlık biçimlerini (veri kayması, kısayol öğrenme) tanır."
tools:
  - "Google Colab"
  - "Hazır (önceden eğitilmiş) modeller"
---

## Ders Notları

> [!not] Bu bölüm ders notlarının genişletileceği alandır. Haftanın özgün konu başlığı: **Tıbbi görüntülerde derin öğrenme sezgisi (röntgen/patoloji); hazır modellerle uygulama**

Ders notları ilerleyen haftalarda buraya eklenecektir.

## Temel Kavramlar

- **Yapay sinir ağı** — Katmanlar hâlinde dizilmiş basit hesap birimlerinden oluşan model.
- **Evrişimli sinir ağı (CNN)** — Görüntüdeki kenar, doku ve şekil gibi örüntüleri katman katman öğrenen ağ.
- **Kısayol öğrenme** — Modelin hastalığı değil, görüntüdeki ilgisiz bir ipucunu (cihaz etiketi) öğrenmesi.
- **Isı haritası (Grad-CAM)** — Modelin karar verirken görüntünün nereye baktığını gösteren görselleştirme.

## Tıptan Örnekler

- Göğüs röntgeninde pnömoni sınıflandırması yapan açık bir model.
- Patoloji lamında tümör alanlarını işaretleme; dermatolojide melanom sınıflandırması.

## Uygulama / Etkinlik

Verilen not defterinde hazır bir röntgen modelini birkaç görüntü üzerinde çalıştırın; ısı haritasını inceleyip modelin nereye baktığını tartışın.

## Tartışma Soruları

1. Bir görüntü modeli radyoloğun yerini alabilir mi, yoksa nasıl bir iş bölümü daha gerçekçidir?

## Haftanın Özeti

Görüntü tanıyan modellerin çalışma mantığını ve sınırlarını sezgisel düzeyde kavradık.
