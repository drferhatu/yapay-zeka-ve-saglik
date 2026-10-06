---
week: 3
title: "Yeniden Başlıyoruz: Araç Senin Seviyene İner, Sen Kaynağı Verirsin"
topic: "Python temelleri II: listeler, sözlükler, döngüler ve koşullar; hasta kayıtlarıyla çalışma"
description: "Bu hafta kimse kod yazmıyor. Kurulda gördüğünüz pH ve tamponlar ile DNA–RNA konularını yapay zekaya üç ayrı dilde anlattırıyor, ürettiği beş sorudan bozuk olanı buluyor ve anatomi notunda neden yanıldığını canlı görüyoruz."
module: m1
semester: 1
exam: false
status: hazir
changeNote: "Ders akışını öğrencilerin yüküne göre yeniledik: bu haftadan itibaren ders, kurulda o hafta işlenen konular üzerinden bir saatlik canlı gösteri olarak yürür; ödev ve ön hazırlık yoktur. Ders planındaki Python konuları ileride, kod korkusu geçince, küçük parçalar hâlinde gelecek."
tags:
  - "pH"
  - "tampon"
  - "DNA"
  - "RNA"
  - "NotebookLM"
  - "doğrulama"
  - "halüsinasyon"
objectives:
  - "Aynı konuyu yapay zekaya farklı seviyelerde anlattırabilir ve kendi seviyesini söylemenin çıktıyı nasıl değiştirdiğini görür."
  - "Yapay zekanın ürettiği sorular arasından hatalı olanı fark eder."
  - "Kaynağa bağlı bir aracın (NotebookLM) neden temiz kaynakla doğru, fotoğrafla yanlış çalıştığını açıklar."
tools:
  - "Gemini / Claude"
  - "NotebookLM"
---

## Bu hafta kurulda

Su, çözünürlük, asit ve bazlar; zayıf asitler, pH ve tamponlar; biyomoleküller; DNA ve RNA'nın moleküler yapısı; hücrenin yüzey farklılaşmaları; tıp etiğine giriş. Dersimiz bunların üzerine kuruldu; kurul sınavı 20 Kasım.

## Gösteride ne oldu

Geçen hafta hızlı gittik; bu hafta yavaşladık. Kimse bilgisayar getirmedi, kimse bir şey yüklemedi. Perdede üç şey yaptık.

**Aynı konu, üç dil.** En zor bulduğunuz konuyu (çoğunluk pH ve tamponlar dedi) yapay zekaya önce biyokimya dersi düzeyinde, sonra on yaşındaki bir çocuğa anlatır gibi, sonra da kurul sınavı cevabı gibi anlattırdık. Bilgi aynıydı, kıvam değişti. Buradan çıkan ders şu: araç sizin seviyenize iner, ama seviyeyi siz söylemek zorundasınız. "Anlat" demekle "1. sınıf tıp öğrencisine, 8 cümleyle anlat" demek arasındaki fark, aldığınız cevabın işe yarayıp yaramaması.

Sonra ona "emin misin?" dedik. Bikarbonat tamponunun pKa'sı 6,1'dir ve normal kanda bikarbonat/karbonik asit oranı yaklaşık 20'ye 1'dir; model bazen bu soruda direnir, bazen pes edip fikir değiştirir. İkisi de aynı dersi verir: siz itiraz edince cevabını değiştiren bir araca sınavda güvenmezsiniz, kitaba bakarsınız.

**Beş soru, biri bozuk.** DNA ve RNA yapısından beş çoktan seçmeli soru ürettirdik ve araca "birini bilerek hatalı yap" dedik. Sınıf olarak bozuk soruyu bulduk. Bu aracı sınava hazırlanırken kullanacaksınız; bozuk soruyu bulabildiğiniz gün kullanabilirsiniz, bulamadığınız gün o sizi kullanır.

**Anatomi notunda ne olmuştu?** Bir arkadaşınız geçen hafta anatomi notunu NotebookLM'e yüklemiş, araç yerleri karıştırmıştı. Aynı şeyi perdede yeniden yaptık: önce bir el yazısı notun fotoğrafı, sonra aynı konunun temiz metni. Fotoğrafta araç okuyamadığı yeri tahminle doldurdu; temiz metinde her cümlenin yanına kaynak numarası koydu. Yanlış olan araç değildi, ona verdiğimiz şeydi. Bu yüzden ders kitabı PDF'i, temiz bir sunum ya da yazılı not yükleyin; fotoğraf yüklemeyin.

> [!tanim] Kaynağa bağlı araç
> NotebookLM, yalnızca sizin yüklediğiniz belgelerden cevap verir ve her cümlesine hangi kaynaktan aldığını iliştirir. Genel sohbet botu ise hafızasından konuşur. Birincisi ders çalışmak için, ikincisi fikir almak için.

**Küçük bir sürpriz.** Geçen haftaki hesaplayıcıya, bu haftanın konusu olan Henderson-Hasselbalch denklemi için beş dakikada bir pH sekmesi ekletildi. pCO2'yi 60'a çekince "asidemi" dedi. Siz yazmadınız, ben de yazmadım; ne istediğimizi biliyorduk.

## Haftanın iki sorusu

Bu sorular 15 Ocak'taki vize havuzuna gider. Havuz sitede açık; sınavdaki sorular buradan çıkacak.

1. Bir sohbet botuna "emin misin?" dediğinizde cevabını değiştirmesi size ne söyler?
   A) Yeni bilgi öğrendiğini · B) İlk cevabın kesin yanlış olduğunu · C) Cevabın güvenilirliğini bağımsız bir kaynakla doğrulamanız gerektiğini · D) Modelin yorulduğunu · E) Soruyu yanlış sorduğunuzu
2. NotebookLM gibi "kaynağa bağlı" bir araç ile genel bir sohbet botu arasındaki temel fark nedir?
   A) Daha hızlı olması · B) Türkçe bilmesi · C) Yalnızca yüklenen kaynaklardan cevap verip her cümleye kaynağını iliştirmesi · D) Hiç hata yapmaması · E) Fotoğrafları daha iyi okuması

<details>
<summary>Cevaplar</summary>

1 — C. 2 — C.
</details>

## Telefonda iki dakikada deneyin (isteğe bağlı)

Ödev değil. Canınız isterse: herhangi bir sohbet aracına "Tıp fakültesi 1. sınıf öğrencisiyim, tampon çözeltiyi 10 yaşındaki çocuğa anlatır gibi 5 cümleyle anlat" yazın. Sonra "şimdi kurul sınavı cevabı gibi 4 maddeyle" deyin. Fark size yeter.

## Haftanın Özeti

Üç şey gördünüz: seviyeyi siz söylersiniz, bozuk soruyu siz bulursunuz, kaynağı siz verirsiniz. Üçü de sizin elinizde, aracın değil. Haftaya hücre zarı ve taşınım ile devam ediyoruz; yine bilgisayar gerekmiyor.
