
1. `import random`: Bu satır, kodumuzda rastgele sayılar veya öğeler seçmek için kullanılan `random` modülünü içe aktarıyor.

2. `kelimeler`: Bu liste, oyunda kullanılacak olan kelimeleri içeriyor.

3. `secilmis = random.choice(kelimeler)`: Bu satır, `kelimeler` listesinden rasgele bir kelime seçer ve `secilmis` değişkenine atar.

4. `hak = 10`: Bu değişken, oyuncunun kaç hakkının olduğunu belirtir. Oyuncu her yanlış tahminde bir hakkını kaybeder.

5. `bilinen_harfler = set(kelimedeki_harfler)`: Bu satır, oyuncunun doğru tahmin ettiği harfleri takip eden bir küme oluşturur.

6. `kelimedeki_harfler = set(secilmis)`: Bu satır, seçilen kelimenin içindeki benzersiz harfleri içeren bir küme oluşturur.

7. `while hak > 0:`: Bu satır, oyuncunun hakkı olduğu sürece bir döngü başlatır.

8. `for harf in secilmis:`: Bu döngü, seçilen kelimenin her harfi için bir kontrol sağlar.

    a. `if harf in bilinen_harfler:`: Eğer harf, daha önce bilinen harfler kümesinde ise, harfi ekrana yazdırır.

    b. `else:`: Bilinen harfler kümesinde olmayan harfler için alt çizgi (_) ekrana yazdırır.

9. `print()`: Her harfin yazılmasının ardından bir satır boşluk ekler.

10. `tahmin = input("Bir harf giriniz: ").lower()`: Kullanıcıdan bir harf girmesini ister. Girişi küçük harfe çevirir.

11. `if len(tahmin) != 1 or not tahmin.isalpha():`: Girilen harfin uzunluğunu kontrol eder ve bir harf olup olmadığını kontrol eder.

12. `print("Lütfen geçerli bir harf giriniz.")`: Geçerli bir harf girilmediyse uyarı mesajı yazdırılır.

13. `if tahmin in bilinen_harfler:`: Girilen harfin daha önce girilip girilmediğini kontrol eder.

14. `print("Bu harfi zaten girdiniz. Tekrar deneyin.")`: Eğer harf zaten girildiyse uyarı mesajı yazdırılır.

15. `if tahmin in kelimedeki_harfler:`: Girilen harfin seçilen kelimenin içinde olup olmadığını kontrol eder.

16. `bilinen_harfler.add(tahmin)`: Doğru tahmin edilen harfi `bilinen_harfler` kümesine ekler.

17. `print("Doğru Tahmin!")`: Doğru tahmin edilen bir harf olduğunda oyuncuya bilgi verir.

18. `if bilinen_harfler == kelimedeki_harfler:`: Eğer oyuncu tüm harfleri doğru tahmin ettiyse, oyunu kazandığını bildirir ve döngüden çıkar.

19. `else:`: Eğer oyuncu tüm harfleri doğru tahmin etmediyse, yanlış tahmin sayısını bir azaltır.

20. `print(f"Kalan hakkınız: {hak}")`: Kalan hak sayısını ekrana yazdırır.

21. `if hak == 0:`: Eğer oyuncunun hakları bitmişse, oyunu kaybettiğini ve doğru kelimeyi gösterir.
