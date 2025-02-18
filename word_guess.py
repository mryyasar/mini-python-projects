import random

kelimeler={
    3: ["aşk", "buz", "can", "kuş", "çay", "bal", "yer", "yol"],
    4: ["masa", "lale", "elma", "yasa", "kara", "mavi"],
    5: ["kalem", "dünya", "ışık", "kumsal", "perde", "yıldız"],
    6: ["orman", "kumru", "dergi", "yazlık", "gölge", "yorgan"]
}

while True:
    try:
        uzunluk = int(input("Kaç harfli kelime istersiniz? (3,4,5,6): "))
        if uzunluk in kelimeler:
            break
        else:
            print("Lütfen 3,4,5 veya 6 giriniz.")
    except ValueError:
        print("Lütfen sayı giriniz.")

gizli_kelime=random.choice(kelimeler[uzunluk])
kelime_gizli = ["_"] * len(gizli_kelime)
print(" ".join(kelime_gizli))

hak=6
yanlış_tahminler=[]
doğru_tahminler=set()

print("\nKelime: " + " ".join(kelime_gizli))

while "_" in kelime_gizli and hak>0:
    tahmin=(input("\nBir harf tahmin et: ")).lower()
    
    if tahmin == "!":
        tam_tahmin=input("Kelimenin tamamını yaz: ").lower().strip()
        if tam_tahmin==gizli_kelime:
            kelime_gizli=list(gizli_kelime)
            break
        else:
            hak-=1
            print(f"\nYanlış kelime! Kalan hakkın: {hak}")
            continue


    if len(tahmin) !=1 or not tahmin.isalpha():
        print("Lütfen sadece **TEK BİR HARF** girin.")
        continue

    if tahmin in gizli_kelime:
        if tahmin in doğru_tahminler:
            print("\nBu harfi zaten doğru bildin.")
            continue
        doğru_tahminler.add(tahmin)

    if tahmin in gizli_kelime:

        for i in  range (len(gizli_kelime)):
            if gizli_kelime[i]== tahmin:
                kelime_gizli[i]= tahmin
        print("\nDoğru! Güncel kelime: " + " ".join(kelime_gizli))
    else:
        if tahmin not in yanlış_tahminler:
            hak-=1
            yanlış_tahminler.append(tahmin)
            print(f"\nYanlış! Kalan hakkın: {hak}", "\nGüncel kelime: " + " ".join(kelime_gizli))
        else:
            print("\nBu harfi zaten yanlış tahmin ettin.") 


if "_" not in gizli_kelime and hak>0:
    print("\nTebrikler kelimeyi bildin: ", gizli_kelime)
    
else:
    print("\n😞 Hakkın bitti! Kelime: " , gizli_kelime) 






    

