# umur yıldırım tarafından yazılmıştır.

import random

def kelime_sec():
    kelimeler = ["python", "programlama", "bilgisayar", "kodlama", "geliştirici", "yazılım", "sistem", "flutter", "ruby", "delphi"]
    return random.choice(kelimeler)

def oyunu_baslat():
    kelime = kelime_sec()
    dogru_tahminler = []
    yanlis_tahminler = []
    tahmin_hakki = 10 

    while tahmin_hakki > 0:
        tahmin_edilen_kelime = ""
        for harf in kelime:
            if harf in dogru_tahminler:
                tahmin_edilen_kelime += harf
            else:
                tahmin_edilen_kelime += "_"

        print("Tahmin Edilen Kelime: ", tahmin_edilen_kelime)
        print("Doğru Tahminler: ", dogru_tahminler)
        print("Yanlış Tahminler: ", yanlis_tahminler)
        print("Kalan Tahmin Hakkı: ", tahmin_hakki)

        tahmin = input("Bir Harf Tahmini Yapın: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen Sadece Bir Harf Girin")
            continue

        if tahmin in dogru_tahminler or tahmin in yanlis_tahminler:
            print("Bu Harfi Daha Önce Tahmin Ettiniz")
            continue

        if tahmin in kelime:
            print("Doğru Tahmin! ")
            dogru_tahminler.append(tahmin)
        else:
            print("Yanlış Tahmin! ")
            yanlis_tahminler.append(tahmin)
            tahmin_hakki -= 1

        if set(dogru_tahminler) == set(kelime):
            print("Tebrikler! Kelimeyi Doğru Tahmin Ettiniz! Kelime: ", kelime)
            break

    if tahmin_hakki == 0:
        print("Ne yazık ki tahmin hakkınız tükendi. Bir dahaki sefere bol şans! Doğru Kelime: ", kelime)

if __name__ == "__main__":
    oyunu_baslat()
