# Hafta 3 · 7 Ekim · "Yeniden başlıyoruz" — gösteri senaryosu

Öğretim üyesi notu. Öğrenci hiçbir şey getirmiyor, yüklemiyor; sadece izliyor, telefonla oy veriyor. Perdede siz, bir sohbet aracı (Gemini ya da Claude), NotebookLM ve Claude Code var. Süre 60 dakika, kalan süre serbest.

Kurulda bu hafta: su, çözünürlük, asit-baz; zayıf asit/baz, pH ve tamponlar; biyomoleküller; DNA ve RNA'nın moleküler yapısı; hücrenin apikal/yan/bazal yüzey farklılaşmaları; tıp etiğine giriş; madde ve enerji taşınımı.

## Ders öncesi (10 dk)
- Sohbet aracını yeni bir sohbetle açın; yazı boyutunu büyütün.
- NotebookLM'de iki defter hazır olsun: **A** "Temiz kaynak": aşağıdaki pH/tampon metnini (ya da ders kitabından ilgili sayfanın PDF'ini) yüklü. **B** "Fotoğraf": herhangi bir el yazısı not sayfasının telefon fotoğrafı yüklü (sizin eski bir notunuz da olur; içerik tampon olmak zorunda değil, "notum" olsun yeter).
- Claude Code'u geçen haftaki hesaplayıcı klasöründe başlatın (`DenemeProgram/` ya da depodaki `public/araclar/`).
- Poll Everywhere: 2 soru (aşağıda).

## 0–5 · Açılış: "Bu hafta kurulda ne vardı?"
Tek yansıda haftanın konuları. Poll 1: **"Bu hafta hangisi en zor geldi?"** şıklar: pH ve tamponlar / DNA–RNA yapısı / Hücre yüzey farklılaşmaları / Asit-baz / Hiçbiri, ben iyiyim.
Söylenecek cümle: "Geçen hafta hızlı gittik, bugün yavaşlıyoruz. Bugün kimse bir şey yazmayacak; ben yapacağım, siz 'yanlış' diye bağıracaksınız."

## 5–25 · "Anlat bana": aynı konu, üç dil
En çok oy alan konuyla (büyük ihtimalle pH/tamponlar) gidin. Sırasıyla yapıştırın:

```
Tıp fakültesi 1. sınıf öğrencisiyim. "Tampon çözelti nedir ve kanın pH'ını nasıl sabit tutar?" konusunu, biyokimya dersinde anlatıldığı düzeyde, 8 cümleyle Türkçe anlat. Henderson-Hasselbalch denklemini de yaz.
```
```
Aynı şeyi 10 yaşındaki bir çocuğa anlatır gibi, günlük hayattan bir benzetmeyle, 5 cümleyle anlat.
```
```
Şimdi bunu kurul sınavında çıkacak bir sorunun cevabı gibi, en fazla 4 maddeyle, tanım ve anahtar kelimelerle özetle.
```
Sınıfa: "Hangisi işinize yaradı?" Mesaj: aynı bilgi, üç kıvam; aracın işi sizin seviyenize inmek, sizin işiniz seviyeyi söylemek.

**Hata yakalama anı.** Yapıştırın:
```
Bikarbonat tampon sisteminde pKa değeri nedir ve normal arteriyel kanda HCO3-/H2CO3 oranı kaçtır? Kısa cevap ver.
```
Beklenen doğru: pKa ≈ 6,1; oran ≈ 20:1 (pH 7,4). Model çoğu zaman doğru verir; o zaman şunu sorun:
```
Emin misin? pKa'yı 6,1 yerine 7,4 yazan kaynaklar da var, hangisi doğru ve neden?
```
İyi bir model direnir, kötü günündeyse pes eder. İki hâl de ders: "Siz 'emin misin' deyince fikir değiştiren bir araca sınavda güvenir misiniz? Doğrusu kitapta: 6,1 ve 20:1."

## 25–40 · "Sınava hazırla": beş soru, biri bozuk
```
Tıp fakültesi 1. sınıf biyokimya kurulu için "DNA ve RNA'nın moleküler yapısı" konusundan 5 çoktan seçmeli soru yaz; her soru 5 şıklı, tek doğru cevaplı, Türkçe. Cevap anahtarını en sona koy. Soruların biri bilerek hatalı olsun (yanlış cevap anahtarı ya da iki doğru şık); hangisi olduğunu söyleme.
```
Soruları tek tek perdeye alın; sınıf telefonla ya da el kaldırarak cevaplasın. Sonunda bozuk soruyu birlikte bulun. Söylenecek cümle: "Bu aracı sınava hazırlanırken kullanacaksınız; bozuk soruyu bulabildiğiniz gün kullanabilirsiniz, bulamadığınız gün o sizi kullanır."

## 40–50 · Vay anı: iki sahne

**Sahne 1 — Anatomi olayının yeniden canlandırması (NotebookLM).**
Geçen hafta bir arkadaşınız anatomi notunu yükledi, araç yerleri karıştırdı. Neden? Defter B'yi (fotoğraf) açın, sorun: "Bu nottaki ana kavramları listele." Çıktı bulanık ya da uydurma olacaktır. Sonra Defter A'yı (temiz metin) açın, aynı soruyu sorun; her cümlenin yanında kaynak numarası çıkar. Cümle: "Araç fotoğrafı okuyamıyor, boşluğu tahminle dolduruyor. Temiz metin verirseniz kaynağını gösterir. Yanlış olan araç değil, beslediğimiz şeydi." (Doğrulama alışkanlığı: çıkan her cümlede kaynak numarasına tıklayın, bir tanesini birlikte kontrol edin.)

**Sahne 2 — Hesaplayıcıya canlı bir sekme (Claude Code, 5 dk).**
```
public/araclar/klinik-hesaplayici.html dosyasına altıncı bir sekme ekle: "pH (Henderson-Hasselbalch)". Girdiler: pKa (varsayılan 6,1), HCO3- (mmol/L, varsayılan 24), pCO2 (mmHg, varsayılan 40). Hesap: H2CO3 = 0,03 × pCO2; pH = pKa + log10(HCO3-/H2CO3). Sonuç: pH iki ondalıkla; 7,35'in altı "asidemi", 7,45'in üstü "alkalemi", arası "normal"; ayrıca HCO3-/H2CO3 oranını göster (normalde yaklaşık 20:1). Mevcut tasarımı ve kod üslubunu koru; kaynak olarak Henderson-Hasselbalch ve standart fizyoloji metnini yaz.
```
Çalışınca pCO2'yi 60 yapın: asidemi. Cümle: "Beş dakikada, bu haftanın konusu, çalışan bir araç. Siz yazmadınız, ben de yazmadım; ama ne istediğimizi biliyorduk."

## 50–60 · Haftanın iki sorusu (vize havuzuna gider, perdede)
1. Bir sohbet botuna "emin misin?" dediğinizde cevabını değiştirmesi size ne söyler?
   A) Yeni bilgi öğrendiğini B) İlk cevabın kesin yanlış olduğunu **C) Cevabın güvenilirliğini bağımsız bir kaynakla doğrulamanız gerektiğini** D) Modelin yorulduğunu E) Soruyu yanlış sorduğunuzu
2. NotebookLM gibi "kaynağa bağlı" bir araç ile genel bir sohbet botu arasındaki temel fark nedir?
   A) Daha hızlı olması B) Türkçe bilmesi **C) Yalnızca yüklenen kaynaklardan cevap verip her cümleye kaynağını iliştirmesi** D) Hiç hata yapmaması E) Fotoğrafları daha iyi okuması

Kapanış cümlesi: "Bugün üç şey gördünüz: seviyeyi siz söylersiniz, bozuk soruyu siz bulursunuz, kaynağı siz verirsiniz. Üçü de sizin elinizde, aracın değil. Ödev yok. Haftaya hücre zarıyla devam."

## Yedek plan
- İnternet yoksa: sitedeki Hafta 3 sayfasında üç dildeki anlatım ve beş soru hazır metin olarak duruyor; perdeye alıp aynı tartışmayı yapın.
- Claude Code kota: sahne 2'yi atlayın, "haftaya ekleyeceğim" deyin.
