#ADAM ASMACA 

import random as rand 

sözcükler = ["kuşbaşı","çorba","lahmacun","kanat","köfte","pilav","ciğer",
             "işkembe","şırdan","hamburger","iskender","cantik","tantuni"]

kelime_bul = rand.choice(sözcükler),
kelime = kelime_bul[0]
kelime = kelime.upper()

harf_listesi = []
harf_listesi.extend(kelime)
harf_göster = []
harf_göster.extend(kelime)

for i in range(len(harf_göster)):
    harf_göster[i] = "__"
print(harf_göster)

hata = 0
hak = 5

while hak > 0:
    tahmin = input("Bir harf tahmin edin: ")
    tahmin = tahmin.upper()

    if len(tahmin) == 1 and tahmin.isalpha(): 
        if tahmin in harf_listesi:
            for i in range(len(harf_listesi)):
                if harf_listesi[i] == tahmin:
                    harf_göster[i] = tahmin
                    harf_listesi[i] = "*"
            print(harf_göster)
        else:
            hak -= 1
            hata += 1
            print("Yanlış tahmin! Kalan hakkınız:", hak)

        if hata == 5:
            print("Oyunu kaybettiniz! Doğru kelime:", kelime)
            break

        if "".join(harf_göster) == kelime:
            print("Tebrikler! Doğru kelimeyi buldunuz:", kelime)
            break
    else:
        print("Geçersiz giriş! Lütfen sadece 1 harf girin.")
        
        
        
        
        
        
        
        