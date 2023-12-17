import random

words = ["elma", "armut", "kiraz", "muz", "visne", "seftali", "karpuz", "kavun", "cilek", "erik"]
dogru_harf = []

deneme = 3

kelime = random.choice(words)

print("kelime ",len(kelime), " harften olusmaktadir")

while deneme > 0:
    harf = input("harf girin: ")

    if harf in kelime:
       print("harf var")
       dogru_harf.append(harf)
       print("dogru tahminler: ", dogru_harf)
       if set(kelime) == set(dogru_harf):
            print("Tebrikler! Kelimeyi buldunuz: ",kelime)
    
    else:
      deneme -= 1
      print("harf yok")
      print("hak: ", deneme)

   
          
print("hak kalmadi. kelime: ", kelime)

