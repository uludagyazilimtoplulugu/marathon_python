import random
kelimeler = ["Ford", "Audi", "BMW", "Chevrolet", "Citroen", "Dacia", "Fiat", "Honda", "Hyundai",
            "Iveco", "Jeep", "KIA", "Mazda", "Mercedes", "Nissan", "Opel", "Peugeot",
            "Renault", "Seat", "Skoda", "Toyota", "Volkswagen", "Volvo", "TOGG", "Ferrari", "Tesla"]
hak = 10
alfabe = "abcçdefgğhıijklmnoprsştuüvyz"
ek_karakter = "wxq"
secilmis = random.choice(kelimeler).lower()
dogru_harfler = []
denenmis_harfler = []
while hak > 0:
    tahmin = input("Lütfen bir harf girin: ").lower().strip()
    alt_tire_sayisi = 0
    
    for i in range(len(secilmis)):
        if secilmis[i] in dogru_harfler:
            print(secilmis[i], end="")
        else:
            alt_tire_sayisi += 1
            print("_", end="")
    print()
    if alt_tire_sayisi == 0:
        print("Tebrikler oyunu kazandınız.")
        exit()
    print(hak, "hakkınız var")

    if len(denenmis_harfler):
        print("denenmiş harfler: ", end="")
        for harf in denenmis_harfler:
            print(harf, end=", ")
        print()

    print()
    if len(tahmin) != 1:
        if len(tahmin) == len(secilmis):
            if tahmin == secilmis:
                print("Tebrikler. Kelimeyi doğru tahmin ettiniz.")
                exit()
            else:
                print("Kelimeyi doğru tahmin edemediniz.")
                hak -= 1
                continue
        else:
            print("Lütfen tek harf girin ya da kelimeyi tahmin edin.")
            continue

    if not (tahmin in (alfabe + ek_karakter)):
        print("Lütfen geçerli bir karakter girin.")
        continue

    if tahmin in denenmis_harfler:
        print("Bu harfi önceden denediniz.")
        continue

    if tahmin in secilmis:
        dogru_harfler.append(tahmin)
        print("Doğru tahmin.")
    else:
        print("Yanlış harf tahmini yaptınız.")
        denenmis_harfler.append(tahmin)
        hak -= 1

print("Kelimeyi bulamadınız. Doğru kelime:", secilmis)
