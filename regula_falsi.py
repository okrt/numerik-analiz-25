import time
def regula_falsi(f, alt_sinir, ust_sinir, tolerans=0.001, maksimum_iterasyon=1000):
    """
    Regula Falsi (Yanlış Pozisyon) yöntemi ile verilen fonksiyonun kökünü yaklaşık olarak bulur.
    
    Parametreler:
    f : function -> Kökü bulunacak fonksiyon.
    alt_sinir : float -> Aralığın alt sınırı.
    ust_sinir : float -> Aralığın üst sınırı.
    tolerans : float (varsayılan: 0.001) -> Hata toleransı.
    maksimum_iterasyon : int (varsayılan: 1000) -> Maksimum iterasyon sayısı.
    
    Dönüş:
    float -> Yaklaşık kök değeri veya None.
    """
    iterasyon = 0
    baslangic_zamani = time.time()
    
    if f(alt_sinir) * f(ust_sinir) >= 0:
        print("Hata: Belirtilen aralıkta fonksiyonun işareti değişmiyor. Kök bulunamayabilir.")
        return None
    
    for _ in range(maksimum_iterasyon):
        iterasyon += 1
        kok_tahmin = (alt_sinir * f(ust_sinir) - ust_sinir * f(alt_sinir)) / (f(ust_sinir) - f(alt_sinir))
        fonksiyon_degeri = f(kok_tahmin)
        
        print(fonksiyon_degeri)
        
        if abs(fonksiyon_degeri) < tolerans:
            print(f"İterasyon sayısı: {iterasyon}, Süre: {time.time() - baslangic_zamani} saniye")
            print("Yaklaşık Kök Bulundu!")
            return kok_tahmin
        
        if f(alt_sinir) * fonksiyon_degeri < 0:
            ust_sinir = kok_tahmin
        else:
            alt_sinir = kok_tahmin
    
    print("Maksimum iterasyon sayısına ulaşıldı, kök bulunamadı.")
    return None


# Örnek fonksiyon tanımlanıyor
def ornek_fonksiyon(x):
    return x**3 + 4*x**2 - 10

# İkiye bölme yöntemi ile kök bulma işlemi gerçekleştiriliyor
kok = regula_falsi(ornek_fonksiyon, 1, 2, tolerans=0.01, maksimum_iterasyon=1000)

print("Kök=", kok)