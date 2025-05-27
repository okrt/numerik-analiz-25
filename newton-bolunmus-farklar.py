def bolunmus_farklar(x, y):
    """
    Newton bölünmüş farklar katsayılarını hesaplar

    Argümanlar:
    x: x değerlerinin bir listesi
    y: y yani f(x) değerlerinin bir listesi

    Döndürür:
    list: katsayıları döndürür.
    """
    n_sayisi = len(x)
    katsayilar = [y[0]]

    for adim in range(1, n_sayisi):
        farklar = []
        for satir in range(n_sayisi - adim):
            fark = (y[satir + 1] - y[satir]) / (x[satir + adim] - x[satir])
            farklar.append(fark)
        katsayilar.append(farklar[0])
        y = farklar

    return katsayilar


def interpolate(istenen, x, katsayilar):
    n = len(x)
    interpolatasyon_degeri = katsayilar[0]

    for i in range(1, n):
        terim = katsayilar[i]
        for j in range(i):
            terim *= (istenen - x[j])
        interpolatasyon_degeri += terim

    return interpolatasyon_degeri

def polynomial(katsayilar, x):
    """
    Fonksiyonu string olarak döndürür.

    Argümanlar:
    katsayilar: bolunmus farklar metoduyla hesaplanmis katsayilar
    x: kullanilan degerlerin bir listesi

    Döndürür:
    str: fonksiyonun yazılı hali
    """

    n = len(katsayilar)
    polinom_str = str(katsayilar[0])

    for i in range(1, n):
        terim = str(katsayilar[i])
        for j in range(i):
            terim += "*(x - {})".format(x[j])
        polinom_str += " + " + terim

    return polinom_str



x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
"""
x = [-5, -1, 0, 2]
y = [-2,6,1,3]
"""
katsayilar = bolunmus_farklar(x, y)
print("Bulunan katsayilar", katsayilar)
polinom = polynomial(katsayilar, x)
print("Üretilen polinom: ",polinom)
interp_yapilacak = 8
interpolasyon_sonucu = interpolate(interp_yapilacak, x, katsayilar)
print("Interpolasyona göre f(", interp_yapilacak, ")=", interpolasyon_sonucu)
