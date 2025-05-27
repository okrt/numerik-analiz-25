import math
from prettytable import PrettyTable

def newton_ileri_farklar(x_degerleri, y_degerleri, x_aralik):
    n = len(x_degerleri)
    h = x_degerleri[1] - x_degerleri[0]  # Sabit adım

    # Fark tablosu
    fark_tablosu = [y_degerleri.copy()]
    for i in range(1, n):
        kolon = [fark_tablosu[i-1][j+1] - fark_tablosu[i-1][j] for j in range(n - i)]
        """
        kolon = []
        for j in range(n - i):
            fark = fark_tablosu[i-1][j+1] - fark_tablosu[i-1][j]
            kolon.append(fark)
        fark_tablosu.append(kolon)
        """
        fark_tablosu.append(kolon)

    # u hesabı
    u = (x_aralik - x_degerleri[0]) / h

    # Interpolasyon sonucu
    sonuc = y_degerleri[0]
    u_terim = 1
    for i in range(1, n):
        u_terim *= (u - (i - 1))
        sonuc += (u_terim * fark_tablosu[i][0]) / math.factorial(i)

    # Tabloyu yazdır
    tablo = PrettyTable()
    basliklar = ["x", "f(x)"] + [f"Δ^{i}y" for i in range(1, n)]
    tablo.field_names = basliklar
    for i in range(n):
        satir = [x_degerleri[i], y_degerleri[i]]
        for j in range(1, n):
            if i < len(fark_tablosu[j]):
                satir.append(round(fark_tablosu[j][i], 6))
            else:
                satir.append("")
        tablo.add_row(satir)

    print(tablo)
    print(f"\nYaklaşık f({x_aralik}) = {round(sonuc, 6)}")

# Örnek veri
x_degerleri = [1.0, 1.1, 1.2, 1.3, 1.4]
y_degerleri = [1.000, 1.233, 1.488, 1.762, 2.056]
x_aralik = 1.25

newton_ileri_farklar(x_degerleri, y_degerleri, x_aralik)
