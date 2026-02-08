# 🚂 10.1 Liste Kavramı: Veri Trenine Giriş

## 🎯 Neden Listelere İhtiyacımız Var?
Diyelim ki bir sınıftaki 5 öğrencinin not ortalamasını hesaplayacaksınız. Listeler olmasaydı her öğrenci için ayrı bir değişken tanımlamanız gerekirdi: `not1`, `not2`, `not3`, `not4`, `not5`.

**Problem:**
- 30 kişilik bir sınıf olsa 30 tane isim uydurmak zorunda kalırsınız.
- Bir öğrenci gelip “Notumu değiştirin” dese, hangi değişkene bakacağınızı şaşırırsınız.

## 🍱 Analoji: Beslenme Çantası / Tren Vagonu
Listeleri bir **Trenin Vagonları** gibi düşünebiliriz:

- Trenin adı **liste ismi**dir.
- Her vagonun içindeki yük ise **eleman**dır.
- En güzel tarafı: Tek bir lokomotif (liste adı) ile onlarca vagonu (veriyi) peşinizden sürükleyebilirsiniz.

## 💡 Global Vizyon: Dinamik Yapı
Listeler “statik” (sabit) değildir. İçine veri ekledikçe kendi kendine büyürler. Bir **Spotify Çalma Listesi** gibi; yeni şarkılar ekledikçe listeniz otomatik olarak uzar.

| Özellik | Değişken | Liste |
| :--- | :--- | :--- |
| **Kapasite** | Sadece 1 değer | Binlerce değer |
| **İsimlendirme** | Her veri için yeni isim | Tüm veriler için tek isim |
| **Veri Türü** | Genelde tek tür | Karışık türler bir arada olabilir |

> **MEB Notu:** Liste, birden fazla değeri tek bir değişken isminde saklamamızı sağlar ve programın daha pratik yazılmasını sağlar.
