# -*- coding: utf-8 -*-
# KONU: 10.1 Liste Kavramı (List Concept)
# AMAÇ: Değişkenlerin karmaşasından kurtulup listelerin düzenine geçmek.

# -------------------------------------------------------------------------
# 1. SENARYO: LİSTESİZ YÖNTEM (Hantal ve Yorucu)
# -------------------------------------------------------------------------
not1 = 85
not2 = 90
not3 = 70
not4 = 100
not5 = 45

ortalama_eski = (not1 + not2 + not3 + not4 + not5) / 5
print("Eski Yöntemle Ortalama:", ortalama_eski)

# -------------------------------------------------------------------------
# 2. SENARYO: LİSTELİ YÖNTEM (Modern ve Dinamik)
# Tek bir isim (notlar) altında tüm vagonları topluyoruz.
# -------------------------------------------------------------------------
notlar = [85, 90, 70, 100, 45]  # Köşeli parantez [] ile liste oluşturulur.

kac_ogrenci = len(notlar)       # Trenin kaç vagonu olduğunu sayar

# Not: Bu derste "sum()" kullanmıyoruz. Toplamı şimdilik elle topluyoruz.
toplam_puan = notlar[0] + notlar[1] + notlar[2] + notlar[3] + notlar[4]

ortalama_yeni = toplam_puan / kac_ogrenci

print("-" * 30)
print("Liste Kullanılan Yöntem:")
print("Öğrenci Sayısı :", kac_ogrenci)
print("Yeni Ortalama  :", ortalama_yeni)

# -------------------------------------------------------------------------
# 3. ÖNEMLİ ÖZELLİK: KARIŞIK VAGONLAR
# Listeler içine sadece sayı değil; metin veya doğru/yanlış da alabilir.
# -------------------------------------------------------------------------
karisik_vagon = ["Mehmet", 2026, True, 3.14]
print("\nKarışık Verilerimiz:", karisik_vagon)
