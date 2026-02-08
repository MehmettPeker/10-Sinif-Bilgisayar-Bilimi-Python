# 🚂 10.1 Liste Kavramı: Veri Trenine Giriş

!!! tip "Dersin Özeti"
    Bu bölümde, onlarca veriyi **tek bir isim altında** nasıl toplayacağımızı ve programlarımızı nasıl daha **akıllı ve düzenli** hale getireceğimizi öğreneceğiz.

---

## 🍱 Neden Listelere İhtiyacımız Var?

Bir sınıftaki 5 öğrencinin not ortalamasını hesaplamak istediğinizi düşünün.  
Listeler olmasaydı, her öğrenci için ayrı bir oda (değişken) tutmanız gerekirdi:

=== "Kod"
    ```python
    not1 = 85
    not2 = 90
    not3 = 70
    # ... bu böyle uzayıp giderdi!
    ```

!!! warning "Zorluk"
    Öğrenci sayısı 100 olduğunda 100 tane isim uydurmak imkansızdır.  
    İşte burada **Listeler** devreye girer.

---

## 🎨 Analoji: Veri Treni (Vagon Mantığı)

Listeyi bir **Lokomotif**, içindeki her veriyi ise bir **Vagon** gibi düşünebiliriz.

- **Tek İsim:** Tüm trenin tek bir adı vardır → `notlar`
- **Esnek Kapasite:** İhtiyacımız olduğunda yeni vagonlar ekleyebiliriz
- **Farklı Yükler:** Bir vagon elma taşırken diğeri kömür taşıyabilir  
  (Farklı veri tipleri bir arada olabilir)

---

## 💻 Kod Üstünde Görelim

Listeler köşeli parantez `[]` ile oluşturulur ve elemanlar virgülle ayrılır.

=== "Kod"
    ```python
    # Bir alışveriş sepeti oluşturalım
    sepet = ["Ekmek", "Süt", "Yumurta", 2026]

    print("Sepet içeriği:", sepet)
    ```

=== "Çıktı"
    ```text
    Sepet içeriği: ['Ekmek', 'Süt', 'Yumurta', 2026]
    ```

!!! important "Biliyor muydunuz?"
    Python'da bir listenin içine hem metin (`"Mehmet"`),  
    hem tam sayı (`2026`), hem de ondalıklı sayı (`3.14`) koyabilirsiniz.

---

## 📊 Listelerin Gücü: Hızlı Analiz

Listenin içindeki veriler üzerinde saniyeler içinde analiz yapabilirsiniz:

=== "Kod"
    ```python
    puanlar = [85, 90, 70, 100, 60]

    print("Öğrenci Sayısı:", len(puanlar))
    print("En Yüksek Not:", max(puanlar))
    print("Not Toplamı  :", sum(puanlar))
    ```

=== "Çıktı"
    ```text
    Öğrenci Sayısı: 5
    En Yüksek Not: 100
    Not Toplamı  : 405
    ```

=== "Açıklama"
    - `len()` → vagonları sayar
    - `max()` → en büyük değeri bulur
    - `sum()` → tüm değerleri toplar

---

## 🧠 Sıra Sende!

!!! caution "Görev"
    Kendi **Haftalık Harcama** listenizi oluşturun.

    - İçine 7 tane sayısal değer ekleyin
    - `sum()` fonksiyonu ile toplam harcamanızı ekrana yazdırın
