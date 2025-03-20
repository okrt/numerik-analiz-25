def gauss_seidel_yontemi(k, y, cozum_tahminleri):
    """
    Gauss-Seidel yöntemini kullanarak denklem sisteminin çözüm tahminlerini günceller.
    
    Parametreler:
    k : Katsayıların bulunduğu kare matris (liste listesi).
    y : Denklem sistemindeki eşitliğin sağ tarafındaki değerler (liste).
    cozum_tahminleri : Başlangıç çözüm tahminleri (liste).
    
    Fonksiyon, güncellenmiş çözüm tahminlerini döndürür.
    """
    n = len(k)
    yeni_tahminler = cozum_tahminleri.copy()
    
    for satir in range(n):
        satir_sonuc = y[satir]
        for sutun in range(n):
            if satir != sutun:
                satir_sonuc -= k[satir][sutun] * yeni_tahminler[sutun]
        yeni_tahminler[satir] = satir_sonuc / k[satir][satir]
    
    return yeni_tahminler

# Denklem sistemi:
# 8x1 + 3x2 - 3x3 = 14
# -2x1 - 8x2 + 5x3 = 5
# 3x1 + 5x2 + 10x3 = -8

katsayi_matris = [
    [8, 3, -3],
    [-2, -8, 5],
    [3, 5, 10]
]
y = [14, 5, -8]
cozum_tahminleri = [0, 0, 0]  # Başlangıç çözüm tahminleri

# Belirli sayıda iterasyon ile çözümün yakınsamasını gözlemleme ve hata oranını hesaplama
for iterasyon in range(10):
    onceki_tahminler = cozum_tahminleri.copy()
    cozum_tahminleri = gauss_seidel_yontemi(katsayi_matris, y, cozum_tahminleri)
    
    # Hata oranı: Her değişken için yeni ve eski tahminler arasındaki mutlak farkın maksimumu
    hata_orani = max(abs(yeni - eski) for yeni, eski in zip(cozum_tahminleri, onceki_tahminler))
    if hata_orani < 1e-3:
        break
    
    print(f"İterasyon {iterasyon+1}: Çözüm Tahminleri = {cozum_tahminleri}, Hata Oranı = {hata_orani}")
