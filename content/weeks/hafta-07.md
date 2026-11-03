---
week: 7
title: "Yapay Zeka Nedir, Ne Değildir? Tıpta Yapay Zeka Farkındalığı"
topic: "Pandas II: veri temizleme, eksik veri yönetimi, gruplama ve özetleme"
description: "Yarım saatlik, soru-cevapla akan bir ders: dil modeli aslında ne yapar, tıpta yapay zeka nerede ve ne zamandır var, nerede yanılıyor, hangi veriyi asla vermiyoruz. Bilgisayar yok, ödev yok; telefon yalnızca oy için."
module: m2
semester: 1
exam: false
status: hazir
changeNote: "Önlük töreni ve bayram arasının ardından ilk ders. Program yenilendi: bu hafta yarım saatlik bir farkındalık dersi; Python yok."
tags:
  - "yapay zeka nedir"
  - "dil modeli"
  - "halüsinasyon"
  - "radyoloji"
  - "sepsis"
  - "KVKK"
  - "empati"
objectives:
  - "Bir dil modelinin düşünmediğini, bir sonraki kelimeyi tahmin ettiğini ve bunun sonuçlarını tek cümleyle açıklar."
  - "Tıpta yapay zekanın hangi alanlarda yoğunlaştığını ve 'yeni' olanın ne olduğunu ayırt eder."
  - "Çalışır görünen bir sistemin doğru olmayabileceğini bir örnekle anlatır; hangi verinin bir sohbet aracına verilemeyeceğini bilir."
tools:
  - "Poll Everywhere"
resources:
  - title: "Ayers JW ve ark. Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum. JAMA Intern Med 2023;183(6):589-596"
    url: "https://doi.org/10.1001/jamainternmed.2023.1838"
    note: "Hekimlerin kimliği gizli cevapları puanladığı çalışma."
  - title: "Wong A ve ark. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Intern Med 2021;181(8):1065-1070"
    url: "https://doi.org/10.1001/jamainternmed.2021.2626"
    note: "Sepsis uyarı sisteminin bağımsız değerlendirmesi."
  - title: "FDA — Artificial Intelligence-Enabled Medical Devices listesi"
    url: "https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices"
    note: "Onaylı yapay zeka tıbbi cihazlarının güncel listesi; alan dağılımını buradan sayabilirsiniz."
  - title: "KVKK — Sağlık verileri"
    url: "https://www.kvkk.gov.tr/Icerik/6649/Saglik-Verileri"
    note: "Sağlık verisinin özel nitelikli kişisel veri olarak işlenme kuralları."
  - title: "Abdulnour RE ve ark. Educational Strategies for Clinical Supervision of Artificial Intelligence Use. N Engl J Med 2025;393:786-797"
    url: "https://doi.org/10.1056/NEJMra2503232"
    note: "Dil modellerinin neden 'anlıyor gibi' göründüğü ve bunun eğitimdeki riskleri."
---

## Bugün ne yapıyoruz?

İki haftalık aradan sonra sakin bir dersle dönüyoruz. Bugün bir şey yazmıyor, bir şey yüklemiyoruz; yarım saat boyunca soru soruyorum, siz telefonla oy veriyorsunuz, sonuç perdeye düşüyor ve her sonucun ardından bir hikâye anlatıyorum. Sorular sitede yok; onları derste göreceksiniz. Burada yalnızca hikâyeler ve kanıtları var, çünkü dersten sonra "hocam o çalışma neydi" diye soracak olanlar için tek bir yer olsun istedim.

Altı haftadır yapay zekayı kullanıyoruz; bugün bir adım geri çekilip ne olduğuna bakıyoruz. Dersin tamamı beş hikâyeden oluşuyor.

## Birinci hikâye: sihir yok, çok iyi bir tahmin var

ChatGPT'ye bir soru yazdığınızda arkada neler oluyor? Bir dil modeli düşünmüyor, bilmiyor, anlamıyor; önündeki metne bakıp bir sonraki kelimenin ne olacağını tahmin ediyor. Bunu milyarlarca sayfa metinden öğrendi ve o kadar iyi yapıyor ki bize anlıyor gibi geliyor. Üstelik her seferinde en olası kelimeyi seçmiyor, biraz da zar atıyor; aynı soruya iki kez sorduğunuzda iki farklı cevap almanızın sebebi bu.

Bu tahmin mekanizmasının bir sonucu daha var: model, cevabı o an internetten bulmuyor. Eğitim verisinin bir bitiş tarihi var ve arama modu açılmadıkça hafızasından konuşuyor. Bilmediği bir şeyi sorduğunuzda susmuyor, aynı akıcılıkla uydurmaya devam ediyor; ismi halüsinasyon. NEJM'de geçen ay okuduğumuz derleme bu "anlıyor gibi görünme" hâlinin tıp eğitimi için neden tehlikeli olduğunu anlatıyordu: ileri sınıf tıp öğrencilerinin üçte birinden fazlası, modelin klinik senaryolara verdiği hatalı cevapları fark edememişti.

> [!tanim] Dil modeli
> Metnin nasıl devam edeceğini tahmin eden olasılıksal bir model. Anlamaz, hatırlamaz, araştırmaz; ama tahmini o kadar iyidir ki konuşuyor sanırsınız. Bu yüzden doğrulama işi hep sizde kalır.

## İkinci hikâye: tıpta yapay zeka yeni değil, yeni olan dil modeli

EKG cihazının kâğıdın üstüne kendi yazdığı yorumu hepiniz göreceksiniz: "sinüs ritmi, sol ventrikül hipertrofisi düşündürür" gibi. Bu yorum on yıllardır var ve bir tür otomatik örüntü tanıma; yani sağlıkta yapay zeka denen şeyin eski bir akrabası. Glukometre ise ölçer, öğrenmez; o bir yapay zeka değil. Aradaki fark, sistemin kuralı kendisinin veriden çıkarıp çıkarmadığı.

Bugün onay almış yapay zeka tıbbi cihazlarına bakarsanız ezici çoğunluğun radyolojide olduğunu görürsünüz; Amerikan ilaç ve cihaz kurumu FDA'nın listesinde dörtte üçe yakını görüntü işleyen sistemler. Üç dalga hâlinde anlatıyoruz: önce görüntü analizi, sonra tahmin ve karar destek, en son üretken yapay zeka. Son dalga en hızlı yayılan ve en az denetlenen olanı.

## Üçüncü hikâye: hekimler kimin yazdığını bilmeden puanladı

2023'te bir grup araştırmacı internette halka açık bir foruma yazılmış gerçek hasta sorularını aldı. Her soruya iki cevap vardı: biri gönüllü bir hekimin forumda verdiği cevap, diğeri sohbet botunun ürettiği. Üç hekimden oluşan bir jüri, hangisini kimin yazdığını bilmeden cevapları kalite ve empati açısından puanladı.

Sonuç çoğu hekimi rahatsız etti: değerlendirmelerin yaklaşık yüzde 79'unda jüri sohbet botunun cevabını tercih etti; sohbet botunun cevapları çok daha sık "empatik" bulundu. Peki bu, sohbet botunun hekimden iyi olduğu anlamına mı geliyor? Hayır. Bunlar bir forumdaki yazılı sorulardı; muayene yok, öykü yok, sorumluluk yok ve hekim cevapları gönüllü, aceleyle yazılmış kısa notlardı. Hikâyenin dersi şu: akıcı ve sıcak yazmak, doğru yazmak değildir. Model, üslubu mükemmel bir şekilde taklit edebilir; içeriği yine sizin kontrol etmeniz gerekir.

## Dördüncü hikâye: çalışıyor görünen sistem

Amerika'da yüzlerce hastanede kullanılan bir elektronik hasta kaydı sistemi, yatan hastalarda sepsis riskini erkenden haber veren bir uyarı modeliyle geliyordu. Üretici firmanın kendi verilerine göre model gayet iyi çalışıyordu. 2021'de Michigan Üniversitesi'nden bir ekip bu modeli kendi hastanesinde, yaklaşık otuz sekiz bin hastada bağımsız olarak test etti.

Sonuç: model, sepsis gelişen hastaların yaklaşık üçte ikisini kaçırdı; buna karşılık tüm yatan hastaların yaklaşık beşte birinde alarm verdi. Yani hem kaçırıyor hem de hemşireyi gereksiz alarmlarla yoruyordu. Üstelik alarmların çoğu, klinisyenin zaten fark ettiği hastalarda ve zaten fark ettikten sonra geliyordu. Bu çalışmadan sonra sistem gözden geçirildi.

Bu hikâyenin dersi dersin kendisi: bir sistemin "çalışıyor" görünmesi, doğru olduğu anlamına gelmez. Kimin, hangi hastalarda, hangi ölçütlerle test ettiğini sormayan hekim, alarmın peşinden gider. Modelin çıktısını sorgulayan hekim ise hasta güvenliğinin son halkasıdır.

> [!neden] Neden ilk sınıfta anlatıyoruz?
> Çünkü bu sistemleri siz kullanacaksınız. "Model dedi" cümlesini bir sonuç olarak değil, bir soru olarak duymayı şimdiden öğrenirseniz, ileride hangi sistem gelirse gelsin aynı soruyu sorarsınız: kim, nerede, nasıl test etti?

## Beşinci hikâye: hangi veriyi asla vermiyoruz

Kendi ders notunuzu bir sohbet aracına yükleyebilirsiniz; bu sizin notunuz. Ama arkadaşınızın tahlil sonucu, stajda gördüğünüz bir hastanın adının geçtiği not, bir hastanın görüntüsü: bunlar girmez. Türkiye'de kişisel verilerin korunması kanunu sağlık verisini "özel nitelikli kişisel veri" sayar; işlenmesi için açık rıza ya da kanunda sayılan özel koşullar gerekir ve bu veriyi yurt dışındaki bir sunucuya yüklemek başlı başına bir aktarımdır. "Nasılsa kimse görmüyor" düşüncesi yanlış: yüklediğiniz her şeyi en az bir şirket görüyor ve saklıyor olabilir.

Bu dersin ilk haftasında söylediğim kural değişmedi: açık ve anonim veri kullanırız, hasta verisini bulut araçlarına vermeyiz. Ayrıntısını 25. haftada konuşacağız ama kuralı bugünden ezberleyin.

## Ve kapanış

Dersin sonunda size ilk hafta sorduğum soruyu bir kez daha soruyorum: yapay zeka mesleğinizi elinizden alacak mı? Doğru cevabı yok; ama iki sonucu yan yana koyduğumuzda altı haftada neyin değiştiğini göreceğiz. Benim cevabım ilk günden beri aynı: almayacak, ama onu iyi kullanan meslektaşınız öne geçecek. Bu ders, o meslektaş olmak isteyenler için.

## Haftanın iki sorusu

Vize havuzuna giden iki soru; havuz sitede açık, sınavdaki sorular buradan seçilecek.

1. Bir dil modelinin "bilmediği bir konuda da akıcı biçimde cevap üretmesi" durumuna ne ad verilir ve buna karşı temel önlem nedir?
   A) Önyargı; modele itiraz etmek · B) Halüsinasyon; bağımsız bir kaynakla doğrulamak · C) Gecikme; daha uzun beklemek · D) Kesim tarihi; soruyu kısaltmak · E) Aşırı öğrenme; tekrar sormak
2. Aşağıdakilerden hangisi bir sohbet aracına yüklenebilir?
   A) Arkadaşınızın tahlil sonucu · B) Stajda gördüğünüz hastanın adı geçen not · C) Kendi ders notunuz · D) Bir hastanın röntgen görüntüsü · E) Servisteki hastaların listesi

<details>
<summary>Cevaplar</summary>

Birinci sorunun cevabı B: modelin bilmediğini de akıcı biçimde üretmesine halüsinasyon denir ve tek önlem bağımsız bir kaynakla doğrulamaktır. İkincinin cevabı C: yalnızca kendi notunuz; diğer dördü sağlık verisi ya da kişisel veri içerir ve bulut araçlarına verilmez.
</details>

## Haftanın Özeti

Bugün beş hikâye anlattık. Dil modeli düşünmez, tahmin eder; bilmediğini de uydurur. Tıpta yapay zeka yeni değil, yeni olan dil modelidir ve onaylı sistemlerin çoğu radyolojidedir. Hekimler kimin yazdığını bilmeden puanladığında sohbet botunu daha empatik buldu; bu, üslubun doğruluk anlamına gelmediğini gösterir. Yüzlerce hastanede çalışan bir sepsis uyarısı bağımsız testte vakaların çoğunu kaçırdı; çalışıyor görünmek doğru olmak değildir. Ve hasta verisi hiçbir sohbet aracına girmez. Haftaya kurul sınavına dokuz gün kala, sınava yapay zekayla nasıl çalışılır konusunu kısa tutarak konuşacağız.
