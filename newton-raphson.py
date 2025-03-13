import time
def newton_raphson(f, f_turev, baslangic_tahmini, tolerans=0.001, maksimum_iterasyon=1000):
    """
    Newton-Raphson yöntemi ile verilen fonksiyonun kökünü yaklaşık olarak bulur.
    
    Parametreler:
    f : function -> Kökü bulunacak fonksiyon.
    f_turev : function -> Fonksiyonun türevi.
    baslangic_tahmini : float -> Başlangıç noktası.
    tolerans : float (varsayılan: 0.001) -> Hata toleransı.
    maksimum_iterasyon : int (varsayılan: 1000) -> Maksimum iterasyon sayısı.
    
    Dönüş:
    float -> Yaklaşık kök değeri veya None.
    """
    iterasyon = 0
    baslangic_zamani = time.time()
    x = baslangic_tahmini
    
    for _ in range(maksimum_iterasyon):
        iterasyon += 1
        fonksiyon_degeri = f(x)
        turev_degeri = f_turev(x)
        
        if abs(fonksiyon_degeri) < tolerans:
            print(f"İterasyon sayısı: {iterasyon}, Süre: {time.time() - baslangic_zamani} saniye")
            print("Yaklaşık Kök Bulundu!")
            return x
        
        if turev_degeri == 0:
            print("Hata: Türev sıfıra eşit, Newton-Raphson yöntemi başarısız oldu.")
            return None
        
        x = x - fonksiyon_degeri / turev_degeri
    
    print("Maksimum iterasyon sayısına ulaşıldı, kök bulunamadı.")
    return None

# Örnek fonksiyon ve türev tanımlanıyor
def ornek_fonksiyon(x):
    return x**3 + 4*x**2 - 10

def ornek_fonksiyon_turev(x):
    return 3*x**2 + 8*x

tahmini_kok_nr = newton_raphson(ornek_fonksiyon, ornek_fonksiyon_turev, 1.5, tolerans=0.01, maksimum_iterasyon=1000)
print("Newton-Raphson Kök=", tahmini_kok_nr)