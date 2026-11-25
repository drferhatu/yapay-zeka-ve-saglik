---
week: 8
title: "Gerçek mi, Uydurma mı? Yapay Zekanın Sağlıkta Yaptıkları"
topic: "Ara değerlendirme ve veri görselleştirme I: Matplotlib/Seaborn ile epidemiyolojik grafikler"
description: "On haber kartı: yapay zekanın sağlıkta yaptığı iddia edilen şeyler; yedisi gerçek, ikisi uydurma, biri yarı yarıya. Derste telefonla oy verdik, kartları çevirdik; hikâyeler ve kaynaklar burada. Kapanışta 2032'den üç sahne."
module: m3
semester: 1
exam: false
status: hazir
changeNote: "Program yenilendi: Bu hafta yarım saatlik bir oyun; Python ve grafik yok. Kurul sınavına dokuz gün."
tags:
  - "gerçek mi uydurma mı"
  - "FDA"
  - "AlphaFold"
  - "halicin"
  - "pankreas kanseri"
  - "USMLE"
  - "ambient scribe"
  - "yanlılık"
objectives:
  - "Yapay zekanın sağlıkta gerçekten yaptığı en az beş şeyi, kaynağıyla birlikte söyler."
  - "Bir haberdeki 'tek başına', 'onay aldı', 'kullanılıyor' gibi kelimelerin neyi iddia ettiğini sorgular."
  - "Doğru bir araştırmanın üstüne uydurma bir sonuç eklendiğinde bunu fark etmeye başlar."
tools:
  - "Cevap Kartı"
---

## Bugün ne yaptık?

Bugün bir oyun oynadık: perdede on haber kartı, her birinde yapay zekanın sağlıkta yaptığı iddia edilen bir şey. Telefonlar [cevap kartıyla](/araclar/cevap-karti) yeşile ve kırmızıya döndü, kartlar çevrildi. Aşağıda kartların hikâyeleri ve kaynakları var; derste şaşırdığınız yerleri burada sakin kafayla okuyun.

## Gerçek olanlar

**Hekim bakmadan karar veren ilk sistem (2018).** Amerikan ilaç ve cihaz kurumu FDA, IDx-DR adlı sisteme diyabetik retinopati taramasında hekim görüntüye bakmadan "göz hekimine sevk et" deme yetkisi verdi. Dokuz yüz hastalık çalışmada duyarlılık ve özgüllük hedeflerini aştı ve birinci basamakta, göz hekimi olmayan odalarda çalışıyor. Yapay zekanın "otonom tanı" onayı aldığı ilk örnek. Kaynak: [Abràmoff ve ark., npj Digital Medicine 2018](https://doi.org/10.1038/s41746-018-0040-6).

**Nobel alan protein tahmini (2024).** Amino asit diziliminden proteinin üç boyutlu yapısını tahmin eden AlphaFold'un geliştiricileri Demis Hassabis ve John Jumper, 2024 Nobel Kimya Ödülü'nün yarısını aldı; diğer yarısı hesaplamalı protein tasarımı için David Baker'a gitti. İkinci haftada görüntüleyicisini konuştuğumuz program bu. Kaynak: [Nobel Vakfı basın bülteni, 9 Ekim 2024](https://www.nobelprize.org/prizes/chemistry/2024/press-release/).

**Röntgenden ırkı tahmin eden model (2022).** Bir derin öğrenme modeli, göğüs röntgeni, BT ve mamografide hastanın kendi beyan ettiği ırkı yüksek doğrulukla tahmin etti; radyologlar aynı görüntüde bunu yapamıyor ve modelin neye baktığı tam olarak bilinmiyor. Görüntü bozulsa, çözünürlük düşse bile tahmin sürdü. Ürkütücü olan şu: Model ırkı görebiliyorsa, tanı modelleri de fark etmeden ırka göre farklı davranabilir. Yanlılık tartışmasının çıkış noktası; 16. haftada döneceğiz. Kaynak: [Gichoya ve ark., Lancet Digital Health 2022](https://doi.org/10.1016/S2589-7500(22)00063-2).

**Bilgisayarın bulduğu antibiyotik (2020).** MIT'de bir model önce bilinen moleküllerden "bakteriyi öldürür mü" örüntüsünü öğrendi, sonra yüz milyondan fazla molekülü taradı ve halicin adını verdikleri yeni bir antibiyotik buldu; isim 2001 Uzay Yolu Macerası'ndaki HAL'den. Farelerde dirençli enfeksiyonları tedavi etti. Kaynak: [Stokes ve ark., Cell 2020](https://doi.org/10.1016/j.cell.2020.01.021).

**Radyoloğun normal dediği tomografide pankreas kanseri (2023).** PANDA adlı model, kontrastsız rutin karın tomografisinde pankreas kanserini yakalamak için Çin'de geliştirildi; yaklaşık 20 bin hastada çok merkezli doğrulandı, ardından 20 binden fazla gerçek dünya taramasında yanlış alarmı binde birin altında tutarak radyologların kaçırdığı vakaları buldu. Pankreas kanseri geç tanı aldığı için öldürücüdür; erken yakalamak her şeyi değiştirir. Kaynak: [Cao ve ark., Nature Medicine 2023](https://doi.org/10.1038/s41591-023-02640-w).

**ChatGPT tıp lisans sınavında (2023).** Model, Amerikan tıp lisans sınavı USMLE'nin üç basamağında da yaklaşık yüzde 60 olan geçer sınıra yaklaştı ya da geçti; cevaplarının çoğunda tutarlı gerekçeler vardı. Sınavı geçmek hekim olmak değil; ama bu sonuç, çoktan seçmeli sınavların ne ölçtüğü sorusunu da açtı. Kaynak: [Kung ve ark., PLOS Digital Health 2023](https://doi.org/10.1371/journal.pdig.0000198).

**Görüşmeyi dinleyip notu yazan sistem (2024).** "Ambient scribe" denen sistemler hekim-hasta görüşmesini dinleyip muayene notunun taslağını yazıyor; Kaiser Permanente'nin on haftalık pilotunda yaklaşık 3.400 hekim 300 binden fazla görüşmede kullandı. Notu hekim okuyup imzalıyor. Mahremiyet ve doğruluk sorularını 24. ve 25. haftada konuşacağız. Kaynak: [Tierney ve ark., NEJM Catalyst 2024](https://doi.org/10.1056/CAT.23.0404).

## Uydurma olanlar

**"Türkiye'de robot tek başına apandisit ameliyatı yaptı."** Dünyada da yok. Cerrahi robotlar cerrahın elini uzatır, karar vermez; otonom ameliyat deneyleri laboratuvarda, hayvan dokusunda yapılıyor. "Tek başına" kelimesi duyulduğunda durulacak yer.

**"FDA, hekim onayı olmadan antibiyotik reçete eden yapay zekaya onay verdi."** Onaylı yapay zeka cihazlarının hiçbiri tedavi kararını tek başına vermiyor; en ileri örnek bile "sevk et" diyen bir tarama sistemi. "Onay aldı" cümlesini duyduğunuzda neye onay aldığını sorun.

## Yarısı gerçek olan

**"Konuşmadan depresyonu tespit eden sistem onay aldı ve kliniklerde kullanılıyor."** Konuşmadan psikiyatrik bozuklukları saptama araştırmaları gerçek ve umut verici; sistematik derlemeler onlarca çalışma sayıyor. Ama rutin klinik kullanımda onaylı böyle bir tarama aracı yok. Doğru bir araştırmanın üstüne uydurma bir sonuç eklemek, yanlış haberin en yaygın biçimi; bu kartı yanlış bilenler kendini kötü hissetmesin, bilerek böyle yazıldı. Kaynak: [Low ve ark., Laryngoscope Investigative Otolaryngology 2020 (derleme)](https://doi.org/10.1002/lio2.354).

## Kapanış: 2032'den üç sahne

Görüşme biterken not yazılmış, hekim okuyup imzalıyor. Röntgen çekilirken sistem görüntüyü çoktan okumuş, şüpheli bulguyu sıraya koymuş. Hasta gece ikide ilacının yan etkisini sormuş, bir bot cevaplamış, sabah hekime özet düşmüş. Üçünün de bugün çalışan erken sürümleri var; sorun ne zaman gelecekleri değil, geldiklerinde çıktıyı kimin kontrol edeceği.

## Haftanın iki sorusu

1. Bir haberde "yapay zeka tek başına ameliyat yaptı / reçete yazdı" ifadesini gördüğünüzde ilk sorulacak soru hangisidir?
   A) Hangi marka · B) Kaç para · C) Kararı gerçekten kim verdi ve hangi kurum neye onay verdi · D) Robot kaç kilo · E) Hangi ülkede
2. Aşağıdakilerden hangisi bugün onaylı ve klinikte çalışan bir yapay zeka uygulamasıdır?
   A) Hekim bakmadan diyabetik retinopati taraması yapıp sevk eden sistem · B) Tek başına reçete yazan sistem · C) Tek başına ameliyat yapan robot · D) Konuşmadan depresyon tanısı koyan onaylı tarama · E) Hekimin yerine tanı koyan sohbet botu

<details><summary>Cevaplar</summary>
1 — C. 2 — A.
</details>

## Haftanın Özeti

On kart, yedi gerçek, iki uydurma, bir yarı gerçek. Yapay zeka bugün göz dibinde hekim bakmadan sevk kararı veriyor, protein yapısını tahmin edip Nobel alıyor, antibiyotik buluyor, pankreas kanserini radyoloğun kaçırdığı görüntüde yakalıyor, tıp sınavını geçiyor, muayene notu yazıyor ve röntgenden ırk tahmin edebiliyor. Ama tek başına ameliyat yapmıyor, reçete yazmıyor; en ileri sistem bile karar yetkisini hekime bırakıyor. Haber okurken üç kelimeye dikkat: tek başına, onay aldı, kullanılıyor. Haftaya ders yok; kurul sınavınızda başarılar.
