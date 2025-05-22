x_degerleri = [1, 2, 3, 4, 5]
y_degerleri = [2, 4, 5, 4, 5]
# Ortalama hesapla
toplam_x = 0
toplam_y = 0
adet = len(x_degerleri)
for i in range(adet):
    toplam_x += x_degerleri[i]
    toplam_y += y_degerleri[i]

ortalama_x = toplam_x / adet
ortalama_y = toplam_y / adet

# Eğim (b) hesapla
pay = 0
payda = 0
for i in range(adet):
    fark_x = x_degerleri[i] - ortalama_x
    fark_y = y_degerleri[i] - ortalama_y
    pay += fark_x * fark_y
    payda += fark_x * fark_x
egim = pay / payda

# Y-kesişimi (a) hesapla
kesisim = ortalama_y - egim * ortalama_x
print(f"En küçük kareler doğrusu: y = {kesisim:.2f} + {egim:.2f}x")

# Örnek tahmin
x_ornek = 4
y_tahmin = kesisim + egim * x_ornek
print(f"x = {x_ornek} için tahmin edilen y: {y_tahmin:.2f}")
