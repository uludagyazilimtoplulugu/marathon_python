import random

kelimeler = ["elma", "muz", "kedi", "kuş", "bilgisayar", "modül", "python", "java", "mouse"]

def play_game():
    oyuncu_adı = input("oyuncu adı: ")
    print("başarılar", oyuncu_adı)
    kelime = random.choice(kelimeler)
    tahmin_harf = []
    deneme_hakkı = 10

    while deneme_hakkı > 0:
        tahmin_kelime = ''
        for harf in kelime:
            if harf in tahmin_harf:
                tahmin_kelime += harf
            else:
                tahmin_kelime += '_'

        print(f"Tahmin edilen kelime: {tahmin_kelime}")
        print(f"Kalan deneme hakkı: {deneme_hakkı}")

        tahmin = input("Bir harf tahmin et: ").lower() #lower() komutu girilen harfin küçük olmasını sağlıyor çünkü python'da büyük ve küçük harfler farklı

        if len(tahmin) != 1: # != komutu girilen değerin uzunluğunun 1'e eşit olup olmadığını kontrol eder
            print("Lütfen sadece bir harf gir.")
            continue

        if tahmin in tahmin_harf:
            print("Bu harfi zaten buldun, başka bir harf dene.")
            continue

        if tahmin in kelime:
            tahmin_harf.append(tahmin)
        else:
            deneme_hakkı -= 1
            print("Yanlış tahmin")

        tahmin_kelime = ''
        for harf in kelime:
            if harf in tahmin_harf:
                tahmin_kelime += harf
            else:
                tahmin_kelime += '_'
        if '_' not in tahmin_kelime:
            print("Tebrikler! Cevap:", kelime)
        
            break

    if deneme_hakkı == 0:
        print(f"Deneme hakkın bitti. Doğru kelime: {kelime}")

play_game()
