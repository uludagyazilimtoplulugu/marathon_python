# Araba Markalarından Oluşan Bir Adam Asmaca Oyunu
## Oyunun Oynanışı    
Oyuna başlamak için terminale `python adam_asmaca.py` yazmalısınız. 
Oyuna başladığınızda 10 tane yanlış yapma hakkınız bulunuyor tek tek harf deneyebilir ve denediğiniz harfin kelimenin içinde olup olmadığını kontrol ettirebilirsiniz eğer doğru harfi bilirseniz alt tirelerden oluşmuş şekilde size verilen kelimenin ipucundan doğru harfler açılacak yanlış tahmin yaptığınızda ise hakkınız bir eksilecek dilerseniz kelimeyi direkt tahmin etmeye çalışabilirsiniz doğru bilirseniz oyun biticek ve sizi tebrik edecektir. Deneyip yanlış uyarısı aldığınız harfler oyunu oynarken liste şeklide gözükür tekrardan yazarsanız hakkınzdan eksilmez.

## Kodun Açıklaması
Başlangıçta ihtiyaç duyulan list ve değişkenleri tanımlandı

`tahmin = input("Lütfen bir harf girin: ").lower().strip()` kullanıcıdan tahmin edeceği harfi veya kelimeye alan başında veya sononda boşluk kullandıysa vaya büyük harf kullandıysa bunları yok sayan kod.

`secilmis = random.choice(kelimeler)` Kodu kelimeler listesinden rastgele bir eleman seçiyor, bu eleman kullanıcının tahmin etmeye çalıştığı kelime olacak

`while hak > 0:` Kullanıcın yanlış yapma hakkı sıfırdan büyük olduğu sürece dönmeye devam edecek bir döngü.

```
alt_tire_sayisi = 0
for i in range(len(secilmis)):
    if secilmis[i] in dogru_harfler:
        print(secilmis[i], end="")
    else:
        alt_tire_sayisi += 1
        print("_", end="")
```
Kullanıcıya başlangıçta kelimenin harf sayısı hakkında alt tirelerden oluşan bir ipucu veren ve tahmin ettiği doğru harflerin yerini gösteren bir döngü.

```
if alt_tire_sayisi == 0:
    print("Tebrikler oyunu kazandınız.")
    exit()
```
Kullanıcıya tek tek tahmin ederek oyunu kazandığında ekrana kazandığını bildiren ve kodun çalışmasını durduran bir kod.

```
if len(denenmis_harfler):
        print("denenmiş harfler: ", end="")
        for harf in denenmis_harfler:
            print(harf, end=", ")
```
Eğer kullanıcının denediği harf varsa daha önceden denemiş olduğu harfleri ekrana yazdıran kod.

```
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
```
Eğer kullanıcın tahmin ettiği kelime doğru olan kelimeyle aynı sayıda harf içeriyorsa keliminin doğruluğunu kontrol eden ve buna bağlı olarak kazandığını veya yanlış tahmin ettiğini belirten kod.

```
if not (tahmin in (alfabe + ek_karakter)):
    print("Lütfen geçerli bir karakter girin.")
    continue
```
Kullanıcının girdiği karakter daha önceden oluşturulan alfabe veya ek_karakter listinde yoksa uyarı veren kod.

```
if tahmin in denenmis_harfler:
    print("Bu harfi önceden denediniz.")
    continue
```
Denenen harfin tekrar kullanılmasını önleyen ve kullanıcıyı bunun hakkında bilgilendiren kod

```
if tahmin in secilmis:
    dogru_harfler.append(tahmin)
    print("Doğru tahmin.")
else:
    print("Yanlış harf tahmini yaptınız.")
    denenmis_harfler.append(tahmin)
    hak -= 1
```
Kullanıcının tahmin ettiği harfin doğruluğunu veya yanlışlığını kontrol eden ve sonucunu kullanıcıya bildiren aynı zamanda yanlış tahmin yapıldıysa hakkını 1 azaltan kod.

`print("Kelimeyi bulamadınız. Doğru kelime:", secilmis)` Kullanıcı kelimeyi bulamazsa kelimeyi kullanıcıya söyleyen kod.