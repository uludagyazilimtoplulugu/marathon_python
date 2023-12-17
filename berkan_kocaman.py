import random

kelimeler = ["kedi", "köpek", "inek", "domuz", "tavşan", "bozkurt"]
secilmis = random.choice(kelimeler)
hak= 10
kelimedeki_harfler = []
bilinen_harfler = []
bilinen_harfler = set(kelimedeki_harfler)
kelimedeki_harfler = set(secilmis)


while hak > 0:
    for harf in secilmis:
        if harf in bilinen_harfler:
            print(harf, end="")
        else:
            print("_", end="")
    print()

    tahmin = input("Bir harf giriniz: ").lower()
    if len(tahmin) != 1 or not tahmin.isalpha():
        print("Lütfen geçerli bir harf giriniz.")
        continue

    if tahmin in bilinen_harfler:
        print("Bu harfi zaten girdiniz. Tekrar deneyin.")
        continue

    if tahmin in kelimedeki_harfler:
        bilinen_harfler.add(tahmin)
        print("Doğru Tahmin!")

        if bilinen_harfler == kelimedeki_harfler:
            print(f"Kelimeyi buldunuz: {secilmis}")
            print("Oyunu Kazandınız!")
            break
    else:
        print("Yanlış Tahmin.")
        hak -= 1

    print(f"Kalan hakkınız: {hak}")

if hak == 0:
    print(f"Oyunu kaybettiniz. Doğru kelime: {secilmis}")
