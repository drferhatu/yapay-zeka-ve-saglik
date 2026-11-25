---
week: 10
title: "Retinator: Kodlayan Bir Göz Hekiminin Yirmi Yılı"
topic: "Tanımlayıcı istatistik ve olasılık sezgisi; sağlık ölçümlerinin yorumlanması"
description: "Bugün yalnızca bir hikâye anlatıyorum: asistanlığında gördüğü bir sorunu çözmek için aracı kendisi yapan, meslektaşlarının alaya aldığı, yirmi yıl sonra tıp tarihinde bir ilke imza atan bir göz hekiminin hikâyesi. Sonra konuşuyoruz. Bilgisayar yok, telefon yok, ödev yok."
module: m3
semester: 1
exam: false
status: hazir
changeNote: "II. Kurul'un ilk dersi. Bugün ne anket var ne oyun; yalnızca bir hikâye ve sohbet."
tags:
  - "Abràmoff"
  - "Retinator"
  - "diyabetik retinopati"
  - "otonom yapay zeka"
  - "FDA"
  - "sorumluluk"
  - "kodlayan hekim"
objectives:
  - "Otonom tanı kararı veren ilk yapay zeka sisteminin hangi klinik sorundan doğduğunu anlatır."
  - "Bir yapay zeka sisteminin onay alması için nasıl bir sınamadan geçtiğini kendi cümleleriyle özetler."
  - "Otonom bir sistem yanıldığında sorumluluğun kimde olması gerektiği sorusunu tartışır."
tools: []
resources:
  - title: "Abràmoff MD ve ark. Pivotal trial of an autonomous AI-based diagnostic system for detection of diabetic retinopathy in primary care offices. npj Digital Medicine 2018"
    url: "https://doi.org/10.1038/s41746-018-0040-6"
    note: "Hikâyedeki çalışma: 900 hasta, 10 birinci basamak merkezi, duyarlılık ve özgüllük sonuçları. Açık erişim."
  - title: "FDA basın duyurusu, 11 Nisan 2018: FDA permits marketing of artificial intelligence-based device to detect certain diabetes-related eye problems"
    url: "https://www.prnewswire.com/news-releases/fda-permits-marketing-of-artificial-intelligence-based-device-to-detect-certain-diabetes-related-eye-problems-300628218.html"
    note: "Onay duyurusunun tam metni; sistemin verdiği iki sonuç ve 'hekimin görüntüyü yorumlamasına gerek kalmadan' cümlesi burada."
  - title: "A Second Opinion (podcast), 30 Mart 2020: Dr. Michael Abràmoff ile söyleşi"
    url: "https://asecondopinionpodcast.com/a-second-opinion-with-dr-michael-abramoff/"
    note: "Neden başladığını, Retinator lakabını ve sorumluluk konusunu kendi ağzından anlatıyor."
  - title: "Entrepreneur Rx (podcast): Michael Abràmoff ile söyleşi"
    url: "https://www.johnshufeldtmd.com/michael-abramoff/"
    note: "2010'da FDA'ya ilk gidişini ve aldığı cevabı anlattığı söyleşi."
  - title: "Abràmoff MD, Tobey D, Char DS. Lessons Learned About Autonomous AI: Finding a Safe, Efficacious, and Ethical Path Through the Development Process. Am J Ophthalmol 2020;214:134-142"
    url: "https://doi.org/10.1016/j.ajo.2020.02.022"
    note: "Otonom yapay zekada sorumluluğun kimde olması gerektiğine dair görüşünü yazdığı makale."
  - title: "Wikipedia: Michael Abramoff"
    url: "https://en.wikipedia.org/wiki/Michael_Abramoff"
    note: "Doğum yeri, eğitim ve tarihler için; sayfada tarafsızlık uyarısı bulunduğunu not ederek kullandım."
---

## Bugün ne yapıyoruz?

Kurul sınavını geride bıraktınız, geçmiş olsun. Bugün sizden hiçbir şey istemiyorum; telefonlarınızı çıkarmanıza, oy vermenize, bir şey denemenize gerek yok. Yalnızca bir hikâye anlatacağım ve sonra biraz konuşacağız. İki hafta önce oynadığımız kart oyununun ilk kartını hatırlarsınız: Bir yapay zekanın, hekim görüntüye bakmadan "bu hastayı göz hekimine sevk et" diyebildiğini söyleyen kart gerçek çıkmıştı. Bugün o kartın arkasındaki insanı anlatıyorum, çünkü bu dersin başından beri "kodlayan hekim" derken kafamda canlanan kişilerden biri o.

## Bir asistanın fark ettiği şey

Michael Abràmoff 1963'te Rotterdam'da doğuyor. Amsterdam Üniversitesi'nde tıp okuyor, ama aynı üniversitede enformasyon kuramı üzerine bir yüksek lisans da yapıyor; yani daha en baştan iki dünyaya birden ayağını basmış biri. Doksanlı yılların sonunda Utrecht'te göz hastalıkları asistanı ve diyabetli hastaların göz dibi muayenelerini yapıyor.

Diyabetin göze verdiği zarar sinsi ilerler. Yüksek kan şekeri retinanın ince damarlarını yıllar içinde bozar; hasta uzun süre hiçbir şey fark etmez, fark ettiğinde ise hasarın bir kısmı kalıcıdır. Oysa erken yakalandığında tedavisi vardır ve bu yüzden diyabetli herkesin yılda bir kez göz dibine baktırması istenir. Sorun şu ki hastaların ancak yarısı bunu yapar. Amerika için verilen rakamlar bunu açıkça gösteriyor: Diyabetik retinopati çalışma çağındaki yetişkinlerde körlüğün ve görme kaybının başta gelen nedeni ve her yıl yirmi dört binden fazla insan bu yüzden görmesini kaybediyor.

Abràmoff poliklinikte bunun iki yüzünü de görüyor. Yıllar sonra bir söyleşide anlattığına göre, muayeneye gelen hastaların bir kısmı çok geç geliyor, kalıcı hasar oluşmuş oluyor; bir kısmı ise çok erken geliyor, gözlerinde hiçbir şey yok, ama o randevu saatini dolduruyorlar. Yani uzmanın vakti, ona en az ihtiyacı olanlara gidiyor, en çok ihtiyacı olanlar ise sıraya girememiş oluyor. Ve genç asistan şunu düşünüyor: "Belki bir bilgisayar bu işi benim burada yaptığımdan daha iyi yapabilir."

Bu cümleyi kuran pek çok hekim vardır. Onu farklı kılan şey, cümlenin devamını kendisinin getirmesi. Bilgisayar mühendisliği geçmişi olduğu için işi birine havale etmiyor; asistanlığı sürerken makine öğrenmesi üzerine doktora yapıyor ve 1997'den itibaren göz dibi fotoğraflarını okuyan algoritmalar üzerinde çalışmaya başlıyor. Sonra Iowa Üniversitesi onu önce misafir araştırmacı olarak davet ediyor, ardından öğretim üyesi olarak yanında tutuyor. Hâlâ hastalarını gören bir retina uzmanı; ama poliklinik dışındaki saatlerinde kod yazıyor.

## "Retinator"

2010 yılı hikâyenin en zor yılı. Abràmoff o yıl iki şey yapıyor: Fikrini bir şirkete dönüştürüyor ve Amerikan ilaç ve cihaz kurumuna, FDA'ya gidip derdini anlatıyor. Kendi aktardığına göre söylediği şey şu: "Bir bilgisayarın tanı koymasını istiyorum." Aldığı cevap da kısa: "Mümkün değil." O güne kadar hiçbir yazılım, bir hekimin gözetimi olmadan tanı kararı verme yetkisi almamış; böyle bir şeyin nasıl sınanacağı, hangi ölçütle değerlendirileceği bile belli değil.

Aynı yıl meslektaşlarından da bir tepki geliyor. Johns Hopkins'in göz hastalıkları kürsüsünün başındaki, üstelik kendisinin yakın arkadaşı olan bir hoca, mesleğin çok okunan gazetelerinden Ophthalmology Times'da bir başyazı yazıyor. Başlığı: "The Retinator: Revenge of the Machines", yani "Retinator: Makinelerin İntikamı". Terminatör filmine gönderme yapan yazının derdi, bu işin göz hekimlerini işsiz bırakacağı. Lakap üzerine yapışıyor. Abràmoff o günleri anlatırken "o zaman çok sertti" diyor; düşünün, hem düzenleyici kurum kapıyı kapatmış hem de kendi meslektaşlarınız sizi bir bilimkurgu kötüsüne benzetiyor.

Burada vazgeçebilirdi. Vazgeçmedi, ama inat da etmedi; yaptığı şey bence hikâyenin en öğretici kısmı. Eleştiriyi ciddiye aldı ve şunu sordu: Bu sistemin güvenilir olduğunu, ona hiç güvenmeyen birine nasıl kanıtlarım? FDA ile yıllar süren bir çalışmaya girdi ve sınavın kurallarını birlikte yazdılar. Sistemin karşısına en zor rakip konacaktı: Wisconsin'deki uzman okuma merkezinin, özel eğitimli fotoğrafçılarla ve çok daha gelişmiş görüntüleme yöntemleriyle koyduğu tanı. Sistem bir göz kliniğinde değil, aile hekimliği muayenehanelerinde sınanacaktı. Kamerayı uzmanlar değil, o muayenehanelerin kendi çalışanları, kısa ve standart bir eğitimden sonra kullanacaktı. Ve başarı sınırı deneme başlamadan önce ilan edilecekti: Duyarlılık, yani hastalığı olanları yakalama oranı, yüzde 85'in; özgüllük, yani hastalığı olmayanlara doğru biçimde "temiz" deme oranı, yüzde 82,5'in üzerinde çıkmazsa sistem başarısız sayılacaktı. Bu iki kelimeyi birazdan, sonuçları gördüğümüzde açacağım.

## 11 Nisan 2018

Deneme 2017'nin ocak ayından temmuz ayına kadar sürdü. Amerika'nın farklı yerlerindeki on birinci basamak merkezinde, daha önce retinopati tanısı almamış dokuz yüz diyabetli hasta çalışmaya alındı. Sonuçlar açıklandığında sistem, önceden konmuş bütün sınırları aşmıştı: Hastalığı olanların yüzde 87,2'sini yakalamış, hastalığı olmayanların yüzde 90,7'sine doğru biçimde "temiz" demişti. Hastaların yüzde 96'sında, uzman olmayan çalışanların çektiği fotoğraflar değerlendirmeye yetecek kalitedeydi.

### Duyarlılık ve özgüllük: İki ayrı soru, iki ayrı hata

Bu iki kelimeyi tıp hayatınız boyunca duyacaksınız, o yüzden burada biraz duralım. Bir tarama testine aslında iki ayrı soru sorarız. Birincisi: Hasta olanları kaçırıyor mu? İkincisi: Sağlam olanları boşuna telaşa veriyor mu? Duyarlılık birinci sorunun, özgüllük ikinci sorunun cevabıdır ve bir testin iyi olup olmadığını anlamak için ikisine birden bakmak gerekir.

Evinizdeki duman dedektörünü düşünün. İyi bir dedektörün iki özelliği olmalı. Gerçekten yangın çıktığında mutlaka ötmeli; ötmezse başka hiçbir özelliğinin önemi kalmaz. Bu onun duyarlılığıdır. Ama ekmek kızarttığınız her sabah da ötmemeli; öterse bir süre sonra pilini çıkarırsınız ve asıl yangın gününde dedektörünüz olmaz. Bu da özgüllüğüdür. Birincisi kötü olan dedektör yangını kaçırır, ikincisi kötü olan dedektör ise kendini kullanılmaz hâle getirir.

Şimdi aynı gözle retinopati sistemine bakalım. Duyarlılığı yüzde 87,2 çıktı. Bunun anlamı şu: Gözünde gerçekten hafiften ileri retinopati olan yüz diyabetliyi bu sisteme gösterirseniz, yaklaşık seksen yedisine "göz hekimine sevk edin" der; on üçünü ise kaçırır ve onlara "on iki ay sonra tekrar gelin" der. Özgüllüğü yüzde 90,7 çıktı. Gözünde böyle bir sorun olmayan yüz diyabetliyi gösterirseniz, yaklaşık doksan birine doğru biçimde "temiz" der; dokuzunu ise gerek olmadığı hâlde göz hekimine yollar.

İki hatanın bedeli birbirinden farklıdır. Kaçırılan hasta, bir sonraki taramaya kadar hastalığı ilerlerken kendini güvende sanır; bu yüzden duyarlılık hasta güvenliğinin ölçüsüdür. Boşuna sevk edilen sağlam kişi ise bir randevu, bir yolculuk ve biraz endişeyle kurtulur gibi görünür, ama o randevu göz hekiminin sırasından düşer; yani Abràmoff'un asistanken gördüğü "boşuna gelen hasta" sorunu yeniden ortaya çıkar. Bu yüzden özgüllük de sistemin işe yarayıp yaramadığının ölçüsüdür ve FDA ikisine ayrı ayrı sınır koymuştur.

Yalnızca birine bakarak bir testi övmek çok kolaydır, buna da dikkat edin. Herkese "hastasın" diyen bir test hiç kimseyi kaçırmaz, duyarlılığı yüzde yüzdür, ama hiçbir işe yaramaz. Herkese "sağlamsın" diyen bir testin de özgüllüğü yüzde yüzdür. Size bir gün bir yapay zeka sistemi "yüzde doksan beş başarılı" diye anlatıldığında soracağınız soru bu yüzden hep aynı olmalı: Hangisi yüzde doksan beş ve öteki kaç?

> [!tanim] Duyarlılık ve özgüllük
> Duyarlılık: Hastalığı olanların yüzde kaçına test "hasta" diyor? Düşükse hasta kaçar. Özgüllük: Hastalığı olmayanların yüzde kaçına test "sağlam" diyor? Düşükse sağlam insanlar boşuna sevk edilir. İkisi birbirinin yerine geçmez; bir testi değerlendirirken ikisini birlikte isteyin.

11 Nisan 2018'de FDA duyurusunu yaptı. Duyurunun içindeki bir cümle, tıp tarihinde ilk kez kuruluyordu: Bu cihaz, "bir klinisyenin görüntüyü ya da sonucu ayrıca yorumlamasına gerek kalmadan tarama kararı veren" ilk cihazdı. Sistem iki cümleden birini söylüyor: ya "hafiften ileri diyabetik retinopati saptandı, göz hekimine sevk edin" ya da "hafiften ileri diyabetik retinopati yok, on iki ay sonra tekrar tarayın". Aile hekiminin odasında, göz hekimi olmadan, birkaç dakikada.

Bunun ne demek olduğunu bir hastanın gözünden düşünün. Diyabet kontrolüne gittiğiniz gün, aynı binada, ayrıca randevu almadan gözünüzün fotoğrafı çekiliyor ve çıkmadan sonucu öğreniyorsunuz. Göz hekiminin sırası ise gerçekten ona ihtiyacı olan hastalara kalıyor. Abràmoff'un asistanken gördüğü iki sorun, geç gelen hasta ve boşuna gelen hasta, aynı anda çözülüyor.

## Hata yaparsa kim sorumlu?

Hikâyenin benim en çok sevdiğim kısmı ise sonu. Otonom bir sistem yanıldığında hesabı kim verecek? Aile hekimi göz dibi okumayı bilmiyor; zaten sistem tam da bu yüzden orada. O hekimi, anlamadığı bir kararın sorumlusu yapmak adil olmaz. Abràmoff bu konuda net bir tutum aldı ve bunu hem söyleşilerinde hem de 2020'de yazdığı bir makalede savundu: Otonom yapay zekayı yapan, doğru ve amacına uygun kullanıldığı sürece onun verdiği zararın sorumluluğunu üstlenmelidir. Kendi şirketi için söylediği cümle şu: "Şirket olarak bu otonom yapay zekanın tıbbi sorumluluğunu üstleniyoruz, tıpkı bir hekimin üstlendiği gibi."

Bu cümlenin ağırlığını şöyle tartın: "sistemimiz çok iyi" demek kolaydır, "yanılırsa bedelini ben öderim" demek zordur. Bir aracın arkasında duran kişinin ona ne kadar güvendiğini anlamak isterseniz, sorumluluğu kimin üzerine yazdığına bakın.

Bir de küçük bir not: "Retinator" başyazısını yazan arkadaşının korktuğu şey olmadı. Abràmoff'un anlattığına göre süreç boyunca ne yaptıklarını açıkça paylaştılar ve göz hekimleri zamanla bu işin en büyük destekçisi oldu; sistemin sigorta tarafından ödenebilmesini sağlayan kodun çıkmasında da meslek örgütleri başı çekti. Çünkü sistem göz hekiminin hastasını elinden almıyor, tam tersine, tedavi edilmesi gereken hastayı bulup ona gönderiyor.

> [!neden] Bu hikâyeyi neden anlatıyorum?
> Çünkü bu derste sizden hepinizin kod yazmasını beklemiyorum. Beklediğim şey daha sade: Poliklinikte, serviste, nöbette "bu böyle olmamalı" dediğiniz bir an gelecek ve o an birinizin, bunu çözecek aracı kimin yapacağını beklemek yerine kendisinin yapabileceğini bilmesini istiyorum. Abràmoff'un yirmi yılı, bir asistanın tek bir cümlesinden başladı.

## Birlikte konuşalım

Hikâyeyi bitirdikten sonra üç soru soracağım; doğru cevapları yok, sizin ne düşündüğünüzü merak ediyorum.

1. Sizin gördüğünüz ya da duyduğunuz, "taranabilir ama taranmıyor" denecek bir sağlık sorunu var mı? Ailenizde, çevrenizde, kendi şehrinizde?
2. Sistem yanılırsa sorumluluk onu yapanda olsun kuralı size adil geliyor mu? Peki aynı kural, hekimin önerisini dinlemeyip sistemi yanlış kullanan bir sağlık çalışanı için de geçerli olmalı mı?
3. Meslektaşlarınız sizi "Retinator" diye alaya alsa ne yapardınız? Abràmoff'un yaptığı gibi eleştiriyi ciddiye alıp kanıtın kurallarını birlikte yazmak size nasıl bir yol gibi görünüyor?

## Haftanın iki sorusu

Vize havuzuna giden iki soru; havuz sitede açık, sınavdaki sorular buradan seçilecek.

1. 2018'de FDA onayı alan ve hekim görüntüyü yorumlamadan tarama kararı veren ilk yapay zeka sistemi hangi hastalık için geliştirilmiştir?
   A) Glokom · B) Diyabetik retinopati · C) Katarakt · D) Yaşa bağlı makula dejenerasyonu · E) Retina dekolmanı
2. Otonom karar veren bir yapay zeka sistemi için, sistemin geliştiricisinin savunduğu sorumluluk ilkesi aşağıdakilerden hangisidir?
   A) Sorumluluk her zaman sistemi kullanan aile hekimindedir · B) Sorumluluk hastadadır · C) Sistem doğru ve amacına uygun kullanıldığında, verdiği zararın sorumluluğunu sistemi yapan üstlenmelidir · D) Yapay zeka sistemleri için sorumluluk söz konusu olamaz · E) Sorumluluk onay veren kurumdadır

<details>
<summary>Cevaplar</summary>

Birinci sorunun cevabı B: Sistem diyabetik retinopati taraması için geliştirildi ve 11 Nisan 2018'de onay aldı. İkincinin cevabı C: Abràmoff, otonom yapay zekayı yapanın, sistem doğru ve amacına uygun kullanıldığı sürece sorumluluğu üstlenmesi gerektiğini savundu ve kendi şirketi için bunu açıkça söyledi.
</details>

## Haftanın Özeti

Bugün tek bir hikâye anlattım. Hollandalı bir göz hastalıkları asistanı, diyabetli hastaların ya çok geç ya da boşuna geldiğini gördü ve bunu bir bilgisayarın daha iyi yapabileceğini düşündü. Mühendislik geçmişine güvenip aracı kendisi geliştirdi. 2010'da FDA "mümkün değil" dedi, bir meslektaşı onu "Retinator" diye yazdı. O ise eleştiriyi ciddiye alıp kanıtın kurallarını düzenleyici kurumla birlikte yazdı, sistemini dokuz yüz hastada, aile hekimliği odalarında, uzman olmayan çalışanların elinde sınadı ve önceden ilan edilmiş sınırları aştı. 11 Nisan 2018'de tıp tarihinde ilk kez bir yapay zeka, hekim görüntüye bakmadan tarama kararı verme yetkisi aldı; yapan kişi de yanılırsa sorumluluğu kendisinin üstleneceğini söyledi. Haftaya yine sakin bir dersle devam ediyoruz.
