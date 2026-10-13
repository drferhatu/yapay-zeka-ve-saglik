---
week: 4
title: "Ajan İş Başında: Hücre Zarı Simülatörü ve Doğru Soru Sormanın Dört Parçası"
topic: "Fonksiyonlar ve okunabilir kod; basit bir klinik hesaplayıcı geliştirme (ör. eGFR/risk skoru)"
description: "Bu hafta bir yapay zeka ajanının perdede, tek istemle, hücre zarında taşınımı oynatan bir simülatör yazmasını izliyoruz; sonra aynı konuyu dört parçalı istemle, kendi hocanızı oluşturarak ve sizi sınayan bir sorgulama simülasyonuyla çalışmanın yolunu görüyoruz. Bilgisayar gerekmiyor, ödev yok."
module: m1
semester: 1
exam: false
status: hazir
changeNote: ""
tags:
  - "ajan"
  - "hücre zarı"
  - "ozmoz"
  - "difüzyon"
  - "Na/K pompası"
  - "RTFC"
  - "istem"
  - "flash kart"
objectives:
  - "Sohbet botu ile ajan arasındaki farkı tek cümleyle söyler ve bir ajanın iş yapışını izlemiş olur."
  - "Bir istemi rol, görev, biçim ve bağlam parçalarıyla kurar; zayıf ve güçlü istemin farkını cevapta görür."
  - "Yapay zekayı kendini sınayan bir hoca gibi kullanmanın üç yolunu (sorgulama simülasyonu, flash kart, 'neden yanlış'lı sorular) tanır."
tools:
  - "Claude Code"
  - "Gemini / Claude / ChatGPT"
resources:
  - title: "OpenStax, Biology 2e — 5.2 Passive Transport"
    url: "https://openstax.org/books/biology-2e/pages/5-2-passive-transport"
    note: "Difüzyon, kolaylaştırılmış taşınım, ozmoz ve tonisite; simülatörün dayandığı metin."
  - title: "OpenStax, Biology 2e — 5.3 Active Transport"
    url: "https://openstax.org/books/biology-2e/pages/5-3-active-transport"
    note: "Sodyum-potasyum pompası adım adım; ikincil aktif taşınım."
  - title: "OpenStax, Anatomy and Physiology 2e — 3.1 The Cell Membrane"
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/3-1-the-cell-membrane"
    note: "Zar yapısı ve taşınım türlerinin klinik örneklerle özeti."
  - title: "OpenStax, Chemistry 2e — 20.1 Hydrocarbons ve 20.3 Aldehydes, Ketones, Carboxylic Acids, and Esters"
    url: "https://openstax.org/books/chemistry-2e/pages/20-3-aldehydes-ketones-carboxylic-acids-and-esters"
    note: "Fonksiyonel gruplar; tuzaklı sorunun doğrulandığı yer."
  - title: "OpenStax, Chemistry 2e — 3.3 Molarity"
    url: "https://openstax.org/books/chemistry-2e/pages/3-3-molarity"
    note: "Çözelti hazırlama ve derişim hesabı."
  - title: "Evolving Medic, MD — These AI Prompts Will Make Your Life SO EASY In Medical School (YouTube)"
    url: "https://www.youtube.com/watch?v=miDJLLlS_0s"
    note: "Bu haftaki istem taktiklerinin esinlendiği video; ilk on dakikası birinci sınıfa uygun, gerisi ileri yıllar için."
---

## Bu hafta kurulda ne var?

Bu hafta hücre zarının kendisini ve zarda taşınımı işliyorsunuz: difüzyon, ozmoz, kolaylaştırılmış taşınım, sodyum-potasyum pompası; yanında hücre iskeleti, organik kimyaya giriş ve fonksiyonel gruplar, çözelti hazırlama ve derişim hesabı, biyoistatistikte veri girişi ve tablo oluşturma, biyomoleküler sistemlerde enerji aktarımı. Bunların içinden birini tahmin ediyorum: zarda taşınım sizi zorluyor. Her yıl herkesi zorlar, çünkü kafada canlanmadan anlaşılmaz. Bugün onu canlandıracağız.

## Bugün ne yapıyoruz?

Geçen hafta üç şey söylemiştim: seviyeyi siz söylersiniz, bozuk soruyu siz bulursunuz, kaynağı siz verirsiniz. Bugün üstüne bir şey ekliyorum: doğru soru sormanın dört parçası var ve bunu bir kez öğrenince araç sizin için başka bir şeye dönüşüyor. Ama önce size bir şey göstereceğim, çünkü bu haftanın asıl sürprizi bir kelime: ajan.

### Ajan nedir, iş başında görelim

Şimdiye kadar kullandığımız araçlar soru sorunca cevap veriyordu. Ajan ise iş yapıyor: ne istediğinizi alıyor, plan kuruyor, dosya açıyor, kod yazıyor, çalıştırıp hatasını görüyor, düzeltiyor ve bitince size haber veriyor. Arada "şunu yapayım mı?" diye soruyor, siz onaylıyorsunuz. Tıpta bunun karşılığı yakında şöyle olacak: "şu hastanın son üç kan gazını karşılaştır, trendi çiz, kılavuzla kıyasla" diyeceksiniz ve bunu yapacak. Bugün bunun küçük bir hâlini izliyoruz.

Perdede Claude Code'a tek bir istem veriyorum ve bu haftanın konusunu oynatan bir simülatör yazmasını istiyorum. Siz beş dakika boyunca planını, dosyayı oluşturmasını, bir hatasını düzeltmesini izleyeceksiniz; bittiğinde karekodu yansıtacağım ve herkes telefonundan oynayacak. Hazır bir sürümü de sitede duruyor; canlı sahne aksarsa oraya geçeriz, aksamazsa ikisini karşılaştırırız.

```text
Tıp fakültesi 1. sınıf öğrencileri için, telefonda çalışan, tek dosyalık (HTML+CSS+JS, dış bağımlılık yok), Türkçe bir "Hücre Zarı Simülatörü" yap. Üç sekme:
1) Ozmoz: bir eritrosit; hipotonik (%0,45 NaCl), izotonik (%0,9) ve hipertonik (%3) ortam seçilince hücre şişsin/sabit kalsın/büzüşsün, su yönünü oklarla göster, hipotonikte aşırı şişince hemoliz uyarısı ver.
2) Difüzyon: zarın iki yanındaki tanecik sayısını sürgüyle ayarlayayım; tanecikler rastgele hareket etsin, zarı belli olasılıkla geçsin, net akışın çoktan aza olduğunu ve fark kapandıkça yavaşladığını canlı sayılarla göster; geçirgenlik sürgüsü olsun.
3) Sodyum-potasyum pompası: 6 adımı tek tek ilerleteyim (3 Na+ bağlanır, ATP fosforiler, dışa açılır ve Na+ bırakır, 2 K+ bağlanır, defosforilasyon, K+ içeri); sayaçlar: atılan Na+, alınan K+, harcanan ATP; "ATP var" kutusunu kapatınca pompa dursun ve nedenini açıklasın.
Her sekmede "Neden böyle?" açıklama kutusu ve klinik bağlantı (serum fizyolojik neden %0,9, digoksin, alveolde gaz değişimi), altında açık erişimli kaynak (OpenStax Biology 2e 5.2 ve 5.3). Kod okunabilir olsun: Türkçe yorumlar, her bölüm ayrı. Basitleştirilmiş model olduğunu belirt.
```

Hazır sürüm: [Hücre Zarı Simülatörü](/araclar/hucre-zari-simulatoru). Ozmoz sekmesinde eritrositi hipotonik ortama koyup hemolizi görün; pompa sekmesinde ATP'yi kapatıp ne olduğunu okuyun. Serum fizyolojiğin neden %0,9 olduğu sorusunun cevabı ilk sekmede.

> [!tanim] Sohbet botu ile ajan
> Sohbet botu bir soruya bir cevap verir. Ajan bir hedefi alır, adımlara böler, araç kullanır (dosya, kod, arama), sonucu kontrol eder ve bitirene kadar devam eder. Güçlü olduğu kadar dikkat ister: ajan sizin yetkinizle iş yapar, bu yüzden ona ne yapabileceğini siz belirlersiniz ve her adımını okursunuz.

### Doğru sorunun dört parçası

Şimdi herkesin yarın kullanabileceği şeye geliyoruz. İyi bir istemin dört parçası var: rol, görev, biçim, bağlam. İngilizcede RTFC diye kısaltıyorlar; biz Türkçesini kullanalım, "rol, görev, biçim, bağlam". Perdede aynı konuyu iki kez soruyorum, önce zayıf, sonra güçlü:

```text
Hücre zarında taşınımı anlat.
```

```text
Hücre biyolojisi dersi veren, benzetmelerle anlatmayı seven bir hoca gibi davran. Görevin: hücre zarında taşınım türlerini (basit difüzyon, kolaylaştırılmış difüzyon, ozmoz, birincil ve ikincil aktif taşınım) birbirinden ayırt etmemi sağlamak. Biçim: her tür için bir satır tanım, bir günlük hayat benzetmesi, bir tıbbi örnek; sonunda beş satırlık karşılaştırma tablosu. Bağlam: tıp fakültesi 1. sınıf öğrencisiyim, kurul sınavım 20 Kasım'da, bu konuda en çok aktif ve pasif taşınımı karıştırıyorum.
```

İki cevabı yan yana görünce fark kendini anlatıyor. İlkinde ansiklopedi maddesi, ikincisinde size yazılmış bir ders alırsınız. Dört parçadan en çok atlanan bağlam; oysa "neyi karıştırıyorum" cümlesi cevabı en çok değiştiren cümle.

### Kendi hocanızı bir kez şekillendirin

Videoda bir asistanın kendine "ortopedi hocası" karakteri oluşturduğunu gördüm; aynı fikri birinci sınıfa uyarlıyorum. Bir sohbetin başına şu metni bir kez yazıyorsunuz, sonra o sohbette ne sorarsanız sorun o karakter cevap veriyor. ChatGPT'de buna özel GPT, Claude'da proje, Gemini'de "gem" deniyor; ama düz sohbette bile ilk mesaj olarak çalışır.

```text
Bundan sonra bu sohbette "Hücre Hocam" ol: hücre biyolojisi ve biyokimya öğreten, sabırlı, benzetmeleri seven, yanlış öğrenmeme asla izin vermeyen bir öğretim üyesi. Ben Fırat Üniversitesi Tıp Fakültesi 1. sınıf öğrencisiyim; şu an Hücre ders kurulundayım, sınav 20 Kasım. Her cevabında: önce bir cümlelik öz, sonra açıklama, sonunda "kendini sına" diye bir soru. Emin olmadığın bir bilgi varsa "bunu kitaptan doğrula" diye işaretle. Türkçe konuş.
```

Sonra ona bugünkü konudan üç soru soruyorum: sodyum-potasyum pompası neden elektrojeniktir, serum fizyolojik neden yüzde 0,9'dur, ikincil aktif taşınım ne demektir. Her cevabın sonundaki "kendini sına" sorusu, bu dersin iki hafta önce söylediği şeyi yapıyor: aracı size cevap veren değil, sizi sınayan bir şeye çeviriyor.

### Araç sizi sorguya çeksin

Klinikte "sorgulama" diye bir gelenek vardır; hoca gittikçe zorlaşan sorular sorar, takılınca ipucu verir. Bunu araca yaptırabilirsiniz ve sınava hazırlanmanın en etkili yollarından biri bu. Perdede öğrenci ben oluyorum, siz cevapları bağırıyorsunuz:

```text
Hücre biyolojisi hocası gibi davran ve beni hücre zarında taşınım konusunda sorguya çek. Temel kavramlardan başla, her doğru cevapta soruyu biraz zorlaştır. Takılırsam önce ipucu ver, yine bilemezsem açıkla ve nedenini söyle. Her seferinde tek soru sor, cevabımı bekle. Beş soru sonra bana bir değerlendirme ve en zayıf olduğum noktayı yaz.
```

Buna iki kardeş istem daha ekliyorum; ikisi de aktif hatırlamaya dayanıyor, yani tanımayı değil hatırlamayı zorluyor:

```text
Tıp eğitimcisi gibi davran. Hücre zarında taşınım konusundan 10 flash kart hazırla. Ön yüz: tanıma değil hatırlama gerektiren bir soru. Arka yüz: kısa cevap ve bir cümlelik klinik bağlantı. Tablo biçiminde ver.
```

```text
Kurul sınavı soru yazarı gibi davran. Hücre zarında taşınımdan 5 çoktan seçmeli soru yaz; her soru 5 şıklı, kısa bir klinik senaryoyla başlasın. Her sorunun altında doğru şıkkın neden doğru, diğer dört şıkkın neden yanlış olduğunu bir cümleyle açıkla.
```

"Neden yanlış" kısmı bu istemin en değerli yeri; yanlış şıkların açıklaması, doğru şıkkın açıklamasından daha çok öğretir.

### Doğrulama anı

Her hafta bir kez aracı yakalıyoruz. Bu hafta fonksiyonel gruplardan tuzaklı bir soru soruyorum ve cevabı OpenStax Kimya ile kontrol ediyoruz:

```text
Aldehit ile keton arasındaki fark nedir? Karbonil grubu aldehitte zincirin ortasında, ketonda uçta bulunur, değil mi? Kısa cevap ver.
```

Sorudaki iddia bilerek ters: karbonil aldehitte uçtadır (en az bir hidrojene bağlı), ketonda iki karbon arasındadır. İyi bir araç "hayır, tersi" der; kötü gününde sizin yanlışınızı onaylar. Yine aynı ders: soruya yanlış bilgi gömerseniz araç onu doğru sanabilir, kitap sanmaz.

## Haftanın cep kartı

Beş istem, hepsi dört parçalı, hepsi bu haftanın konularına yazılmış. Telefonunuza kopyalayın; sınava kadar işinize yarar.

```text
Biyokimya hocası gibi davran. Fonksiyonel grupları (hidroksil, karbonil, karboksil, amino, fosfat, sülfhidril) ezberlemem için Türkçe bir ezber cümlesi ve her grup için tek cümlelik "hangi biyomolekülde görürsün" notu yaz. Tıp 1. sınıf öğrencisiyim; biçim: madde listesi.
```

```text
Laboratuvar asistanı gibi davran. Şu çözelti sorusunu adım adım çöz ama her adımda önce bana "sence sonraki adım ne?" diye sor, ben cevap verince devam et: 250 mL %0,9 NaCl hazırlamak için kaç gram NaCl gerekir ve bu kaç mmol/L'dir? (NaCl molar kütlesi 58,44 g/mol.)
```

```text
Tıp eğitimcisi gibi davran. Difüzyon ile ozmozu, prokaryot ile ökaryot hücreyi ve birincil ile ikincil aktif taşınımı üç ayrı karşılaştırma tablosunda ver; her tabloda 4 ölçüt, sonunda birer "sınavda karıştırılan nokta" uyarısı.
```

```text
Biyoistatistik asistanı gibi davran. Elimde 30 hastanın yaş, cinsiyet ve kan basıncı verisi var. Bu veriyi doğru girmek için bir tablo şablonu öner (sütunlar, veri türleri, eksik veri işareti) ve "sık yapılan 5 veri girişi hatası" listesi yaz. Tıp 1. sınıf öğrencisiyim, Excel kullanıyorum.
```

```text
Öğrenme bilimcisi gibi davran. 20 Kasım'daki Hücre kurul sınavına kadar 37 günlük, günde en fazla 45 dakikalık bir tekrar planı yap. Konular: hücre zarı ve taşınım, biyomoleküller, DNA-RNA yapısı, pH ve tamponlar, fonksiyonel gruplar. Aralıklı tekrar ilkesine göre her konu üç kez dönsün; haftada bir gün boş kalsın. Tablo biçiminde ver.
```

## Haftanın iki sorusu

Vize havuzuna giden iki soru; havuz sitede açık, sınavdaki sorular buradan seçilecek.

1. Bir yapay zeka "ajanı"nı sohbet botundan ayıran temel özellik nedir?
   A) Daha uzun cevap vermesi · B) Türkçe bilmesi · C) Bir hedefi adımlara bölüp araç kullanarak (dosya, kod, arama) sonuca kadar iş yapması · D) Hiç hata yapmaması · E) İnternete bağlı olması
2. "Hücre zarında taşınımı anlat" istemine göre, "Hücre biyolojisi hocası gibi davran; tıp 1. sınıf öğrencisiyim, aktif ve pasif taşınımı karıştırıyorum; her tür için tanım, benzetme ve tıbbi örnek ver" isteminin daha iyi sonuç vermesinin nedeni nedir?
   A) Daha uzun olması · B) Rol, görev, biçim ve bağlam içermesi · C) Büyük harf kullanması · D) Soru işareti içermemesi · E) İngilizce olması

<details>
<summary>Cevaplar</summary>

Birinci sorunun cevabı C: ajanı ajan yapan şey, hedefi adımlara bölüp araç kullanarak işi bitirmesidir; uzun cevap ya da internet bağlantısı tek başına bunu sağlamaz. İkincinin cevabı B: dört parça, yani rol, görev, biçim ve bağlam, aracın cevabı size göre biçimlendirmesini sağlar; uzunluk kendi başına bir şey kazandırmaz.
</details>

## Telefonda iki dakikada deneyin

Ödev değil: cep kartındaki ilk istemi, fonksiyonel gruplar için ezber cümlesini, telefonunuza yapıştırın. Çıkan cümleyi beğenmezseniz "daha komik olsun" deyin. İkinci sürüm genellikle akılda kalır.

## Haftanın Özeti

Bugün bir ajanın beş dakikada, tek istemle, bu haftanın konusunu oynatan bir simülatör yazmasını izlediniz ve onu telefonunuzda oynadınız. Sonra doğru soru sormanın dört parçasını gördünüz: rol, görev, biçim, bağlam. Bir kez kurduğunuz "Hücre Hocam" karakteri sizi sorguya çekebiliyor, flash kart hazırlıyor, yanlış şıkların neden yanlış olduğunu anlatıyor. Ve yine bir hata yakaladık: soruya yanlış bilgi gömerseniz araç onu doğru sanabilir, kitap sanmaz. Haftaya ders yok; önlük giyme töreninizi kutluyorum. 28 Ekim'de aminoasitler ve proteinlerle devam ediyoruz.
