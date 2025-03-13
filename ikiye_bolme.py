import time, math

def ikiye_bolme(f, alt_sinir, ust_sinir, tolerans=0.001, maksimum_iterasyon=1000):
    """
    İkiye bölme yöntemi ile verilen fonksiyonun kökünü yaklaşık olarak bulur.

    Parametreler:
    f : function -> Kökü bulunacak fonksiyon.
    alt_sinir : float -> Aralığın alt sınırı.
    ust_sinir : float -> Aralığın üst sınırı.
    tolerans : float (varsayılan: 0.001) -> Hata toleransı, yeterince küçük olunca işlem durur.
    maksimum_iterasyon : int (varsayılan: 1000) -> Maksimum iterasyon sayısı.

    Dönüş:
    float -> Yaklaşık kök değeri veya None (eğer kök bulunamazsa).
    """
    iterasyon = 0  # İterasyon sayacı
    baslangic_zamani = time.time()  # İşlem süresini ölçmek için başlangıç zamanı
    
    # İlk kontrol: Kökün belirtilen aralıkta olup olmadığını kontrol et
    if f(alt_sinir) * f(ust_sinir) >= 0:
        print("Hata: Belirtilen aralıkta fonksiyonun işareti değişmiyor. Kök bulunamayabilir.")
        return None
    
    # İkiye bölme yöntemi başlatılıyor
    for _ in range(maksimum_iterasyon):
        iterasyon += 1
        orta_nokta = (alt_sinir + ust_sinir) / 2  # Orta nokta hesaplanıyor
        fonksiyon_degeri = f(orta_nokta)  # Fonksiyonun orta noktadaki değeri hesaplanıyor
        
        print(fonksiyon_degeri)  # Debug amaçlı fonksiyon değeri yazdırılıyor
        
        # Eğer tam kök bulunursa
        if fonksiyon_degeri == 0:
            print(f"İterasyon sayısı: {iterasyon}, Süre: {time.time() - baslangic_zamani} saniye")
            print("Kesin Kök Bulundu!")
            return orta_nokta
        
        # Eğer kök tolerans seviyesine ulaştıysa
        elif abs(fonksiyon_degeri) < tolerans:
            print(f"İterasyon sayısı: {iterasyon}, Süre: {time.time() - baslangic_zamani} saniye")
            print("Yaklaşık Kök Bulundu!")
            return orta_nokta
        
        # Yeni aralığı belirle
        if f(alt_sinir) * fonksiyon_degeri < 0:
            ust_sinir = orta_nokta  # Kök alt aralıkta
        else:
            alt_sinir = orta_nokta  # Kök üst aralıkta
    
    print("Maksimum iterasyon sayısına ulaşıldı, kök bulunamadı.")
    return None

# Örnek fonksiyon tanımlanıyor
def ornek_fonksiyon(x):
    return x**3 + 4*x**2 - 10

# İkiye bölme yöntemi ile kök bulma işlemi gerçekleştiriliyor
kok = ikiye_bolme(ornek_fonksiyon, 1, 2, tolerans=0.01, maksimum_iterasyon=1000)

print("Kök=", kok)

