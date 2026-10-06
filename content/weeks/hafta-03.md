---
week: 3
title: "Yeniden Başlıyoruz: Araç Senin Seviyene İner, Kaynağı Sen Verirsin"
topic: "Python temelleri II: listeler, sözlükler, döngüler ve koşullar; hasta kayıtlarıyla çalışma"
description: "Bu hafta kimse kod yazmıyor, kimse bilgisayar getirmiyor. Kurulda gördüğünüz pH ve tamponlar ile DNA–RNA konularını yapay zekaya üç ayrı dilde anlattırıyoruz, ürettiği beş sorudan bozuk olanı birlikte buluyoruz ve kaynağa bağlı bir aracın temiz metinle neden doğru, bozuk metinle neden yanlış çalıştığını görüyoruz."
module: m1
semester: 1
exam: false
status: hazir
changeNote: "Ders akışını sizin yükünüze göre yeniledik. Bu haftadan itibaren ders, kurulda o hafta işlenen konular üzerinden bir saatlik canlı bir gösteri; ödev yok, ön hazırlık yok, bilgisayar getirmek gerekmiyor. Ders planındaki Python konuları ileride, kod korkusu geçtikten sonra, küçük parçalar hâlinde gelecek."
tags:
  - "pH"
  - "tampon"
  - "DNA"
  - "RNA"
  - "NotebookLM"
  - "doğrulama"
  - "halüsinasyon"
objectives:
  - "Aynı konuyu yapay zekaya farklı seviyelerde anlattırır ve kendi seviyesini söylemenin çıktıyı nasıl değiştirdiğini görür."
  - "Yapay zekanın ürettiği sorular arasından hatalı olanı fark eder."
  - "Kaynağa bağlı bir aracın (NotebookLM) temiz kaynakla neden doğru, bozuk kaynakla neden yanlış çalıştığını açıklar."
tools:
  - "Gemini / Claude"
  - "NotebookLM"
---

## Bu hafta kurulda ne var?

Bu hafta kurulda su ve çözünürlükten başlayıp asit-bazlara, zayıf asitlere, pH'a ve tamponlara geçiyorsunuz; yanında biyomoleküller, DNA ve RNA'nın moleküler yapısı, hücrenin yüzey farklılaşmaları ve tıp etiğine giriş var. Kurul sınavı 20 Kasım'da. Bugünkü dersi tam bu konuların üzerine kuruyorum, çünkü bu dersin işe yaradığını görmenizin en kısa yolu, sizi şu an uğraştıran konuda işe yaraması.

## Bugün ne yapıyoruz?

Geçen hafta hızlı gittim, bunu biliyorum. Bugün yavaşlıyoruz. Kimse bir şey yazmayacak, kimse bir şey yüklemeyecek; perdede ben ve bir yapay zeka aracı olacağız, siz de yanlış bir şey gördüğünüzde "yanlış" diye bağıracaksınız. Dersin sonunda sadece üç şeyi aklınızda tutmanızı istiyorum: aracın seviyesini siz belirlersiniz, bozuk soruyu siz bulursunuz ve kaynağı siz verirsiniz. Gerisi ayrıntı.

Önce şunu oylayalım: bu hafta hangisi en zor geldi? pH ve tamponlar mı, DNA ile RNA'nın yapısı mı, hücre yüzey farklılaşmaları mı, yoksa hiçbiri, gayet iyisiniz? Çoğunluk ne derse onunla başlıyoruz; aşağıdaki istemleri pH için yazdım, başka konu çıkarsa adını değiştirmek yeter.

### Aynı konu, üç dil

Şimdi aynı konuyu aynı araca üç kez anlattıracağım. İlkinde biyokimya dersi düzeyinde, ikincisinde on yaşındaki bir çocuğa anlatır gibi, üçüncüsünde kurul sınavında çıkacak bir sorunun cevabı gibi. Bilgi aynı kalacak, kıvamı değişecek; siz de hangisinin işinize yaradığını söyleyeceksiniz.

```text
Tıp fakültesi 1. sınıf öğrencisiyim. "Tampon çözelti nedir ve kanın pH'ını nasıl sabit tutar?" konusunu, biyokimya dersinde anlatıldığı düzeyde, 8 cümleyle Türkçe anlat. Henderson-Hasselbalch denklemini de yaz.
```

```text
Aynı şeyi 10 yaşındaki bir çocuğa anlatır gibi, günlük hayattan bir benzetmeyle, 5 cümleyle anlat.
```

```text
Şimdi bunu kurul sınavında çıkacak bir sorunun cevabı gibi, en fazla 4 maddeyle, tanım ve anahtar kelimelerle özetle.
```

Buradan çıkaracağınız ders basit ama kıymetli: araç sizin seviyenize iner, fakat seviyeyi siz söylemek zorundasınız. "Anlat" demekle "birinci sınıf tıp öğrencisine, sekiz cümleyle anlat" demek arasındaki fark, aldığınız cevabın işe yarayıp yaramaması arasındaki fark.

Şimdi aynı araca bir tuzak kuruyorum. Bikarbonat tamponunun pKa değeri 6,1'dir ve normal kanda bikarbonat/karbonik asit oranı yaklaşık 20'ye 1'dir; bunu kitabınızdan biliyorsunuz. Araca soruyorum, büyük ihtimalle doğru söyleyecek. Sonra ona itiraz edeceğim:

```text
Bikarbonat tampon sisteminde pKa değeri nedir ve normal arteriyel kanda HCO3-/H2CO3 oranı kaçtır? Kısa cevap ver.
```

```text
Emin misin? pKa'yı 6,1 yerine 7,4 yazan kaynaklar da var; hangisi doğru ve neden?
```

İyi bir model burada direnir ve "6,1, çünkü 7,4 tamponun değil kanın pH'ıdır" der. Kötü gününde ise pes edip fikir değiştirir. İkisi de bize aynı dersi veriyor: siz itiraz edince cevabını değiştiren bir araca sınavda güvenmezsiniz, kitaba bakarsınız. Doğrulama dediğimiz şey bu kadar basit.

### Beş soru, biri bozuk

Şimdi bu aracı sınava hazırlanırken nasıl kullanacağınızı göstereceğim ve aynı anda neden gözünüzü dört açmanız gerektiğini. DNA ve RNA'nın yapısından beş soru ürettireceğim; ama araca "birini bilerek bozuk yap, hangisi olduğunu söyleme" diyeceğim. Bozuk olanı birlikte bulacağız.

```text
Tıp fakültesi 1. sınıf biyokimya kurulu için "DNA ve RNA'nın moleküler yapısı" konusundan 5 çoktan seçmeli soru yaz; her soru 5 şıklı, tek doğru cevaplı, Türkçe. Cevap anahtarını en sona koy. Soruların biri bilerek hatalı olsun (yanlış cevap anahtarı ya da iki doğru şık); hangisi olduğunu söyleme.
```

Soruları tek tek perdeye alıyorum, siz el kaldırarak ya da telefonla cevaplıyorsunuz, sonunda bozuk olanı arıyoruz. Bu aracı sınava hazırlanırken gerçekten kullanacaksınız; bozuk soruyu bulabildiğiniz gün kullanabilirsiniz, bulamadığınız gün o sizi kullanır.

### Kaynağı sen verirsin

Geçen hafta bazılarınızdan şunu duydum: ders notunu bir araca yükleyip sorduğunuzda yanlış cevaplar almışsınız. Bu çok sık olur ve çoğu zaman suçlu araç değil, ona verdiğimiz şeydir. Bunu perdede göstermek için elimde aynı tampon konusunun iki sürümü var. Biri temiz, düzgün yazılmış bir metin; diğeri aynı metnin bulanık bir fotoğraftan okunmuş gibi bozulmuş hâli, harfleri kaymış, satırları kopmuş, 6,1'i "6.l" olmuş.

- [Temiz kaynak](/materyal/hafta-03/tampon-temiz.txt)
- [Bozuk kaynak](/materyal/hafta-03/tampon-bozuk.txt) (bilerek bozulmuştur)

İkisini NotebookLM'de ayrı defterlere yüklüyorum ve her ikisine aynı soruyu soruyorum:

```text
Bu kaynağa göre bikarbonat tamponunun pKa değeri nedir, normal bikarbonat/karbonik asit oranı kaçtır ve pH nasıl hesaplanır? Her cümlenin kaynağını göster.
```

Temiz defterde her cümlenin yanında kaynak numarası görürsünüz, tıklayınca metindeki yerini gösterir. Bozuk defterde ya "6.l" diye saçma bir değer gelir ya da araç okuyamadığı yeri hafızasından doldurur ve biz bunu kaynak numarasına tıklayınca anlarız. Ders şu: kaynağa bağlı araç, kaynağınız kadar iyidir. Ders kitabının PDF'ini, temiz bir sunumu ya da yazılı notu yükleyin; fotoğraf yüklemeyin. Ve ne yüklerseniz yükleyin, çıkan cümlenin kaynağına bir kez tıklayın.

> [!tanim] Kaynağa bağlı araç
> NotebookLM, yalnızca sizin yüklediğiniz belgelerden cevap verir ve her cümlesine hangi kaynaktan aldığını iliştirir. Genel sohbet botu ise hafızasından konuşur. Birincisi ders çalışmak için, ikincisi fikir almak için.

### Küçük bir sürpriz

Zaman kalırsa geçen haftaki hesaplayıcıya bu haftanın konusunu ekletiyorum: Henderson-Hasselbalch için bir pH sekmesi. Beş dakika sürüyor; pCO2'yi 60'a çekince "asidemi" demesini birlikte izliyoruz. Siz yazmadınız, ben de yazmadım; ne istediğimizi biliyorduk.

```text
public/araclar/klinik-hesaplayici.html dosyasına altıncı bir sekme ekle: "pH (Henderson-Hasselbalch)". Girdiler: pKa (varsayılan 6,1), HCO3- (mmol/L, varsayılan 24), pCO2 (mmHg, varsayılan 40). Hesap: H2CO3 = 0,03 × pCO2; pH = pKa + log10(HCO3-/H2CO3). Sonuç: pH iki ondalıkla; 7,35'in altı "asidemi", 7,45'in üstü "alkalemi", arası "normal"; ayrıca HCO3-/H2CO3 oranını göster (normalde yaklaşık 20:1). Mevcut tasarımı ve kod üslubunu koru; kaynak olarak Henderson-Hasselbalch denklemini ve standart bir fizyoloji metnini yaz.
```

## Haftanın iki sorusu

Her dersin sonunda iki soru soruyorum ve bu soruları olduğu gibi sitede bırakıyorum. 15 Ocak'taki vizede karşınıza çıkacak sorular bu havuzdan seçilecek; yani derse gelen ve bu sayfaya bir kez bakan hiç kimse sınavda sürprizle karşılaşmayacak. Sınav için endişelenmenize gerek yok, bu dersin amacı sizi sınamak değil.

1. Bir sohbet botuna "emin misin?" dediğinizde cevabını değiştirmesi size ne söyler?
   A) Yeni bilgi öğrendiğini · B) İlk cevabın kesin yanlış olduğunu · C) Cevabın güvenilirliğini bağımsız bir kaynakla doğrulamanız gerektiğini · D) Modelin yorulduğunu · E) Soruyu yanlış sorduğunuzu
2. NotebookLM gibi "kaynağa bağlı" bir araç ile genel bir sohbet botu arasındaki temel fark nedir?
   A) Daha hızlı olması · B) Türkçe bilmesi · C) Yalnızca yüklenen kaynaklardan cevap verip her cümleye kaynağını iliştirmesi · D) Hiç hata yapmaması · E) Fotoğrafları daha iyi okuması

<details>
<summary>Cevaplar</summary>

Birinci sorunun cevabı C: modelin fikir değiştirmesi, cevabın güvenilirliğini bağımsız bir kaynakla kontrol etmeniz gerektiğinin işaretidir. İkincinin cevabı da C: kaynağa bağlı araç yalnızca yüklediğiniz belgelerden konuşur ve her cümleye kaynağını iliştirir; bu onu hatasız yapmaz, ama kontrol edilebilir yapar.
</details>

## Telefonda iki dakikada deneyin

Bu bir ödev değil, canınız isterse: herhangi bir sohbet aracına "Tıp fakültesi 1. sınıf öğrencisiyim, tampon çözeltiyi on yaşındaki bir çocuğa anlatır gibi beş cümleyle anlat" yazın; cevabı alınca "şimdi kurul sınavı cevabı gibi dört maddeyle" deyin. Aradaki farkı görmek bugünkü dersin özeti.

## Haftanın Özeti

Bugün üç şey gördünüz: aracın seviyesini siz belirlersiniz, bozuk soruyu siz bulursunuz, kaynağı siz verirsiniz. Üçü de sizin elinizde, aracın değil. Haftaya hücre zarı ve taşınımla devam ediyoruz; yine bilgisayar gerekmiyor, yine bir saat.
