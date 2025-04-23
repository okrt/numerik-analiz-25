def ileri_fark_turev(f, x, h=1e-5):
    """
    İleri fark formülü kullanarak f fonksiyonunun x noktasındaki türevini hesaplar.
    
    Args:
    f (function): Türevi alınacak fonksiyon.
    x (float): Türev alınacak nokta.
    h (float, optional): Küçük bir adım değeri. Varsayılan değer 1e-5'tir.
    
    Returns:
    float: Hesaplanan türev değeri.
    """
    return (f(x + h) - f(x)) / h

# Örnek kullanım
if __name__ == "__main__":
    # Türevi hesaplanacak örnek fonksiyon
    def ornek_fonksiyon(x):
        return x**2  # f(x) = x^2 fonksiyonu

    # Türevin hesaplanacağı nokta
    x_nokta = 2.0

    # Türev hesabı
    turev_degeri = ileri_fark_turev(ornek_fonksiyon, x_nokta)

    print(f"f'({x_nokta}) ≈ {turev_degeri}")
