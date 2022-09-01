
import random # random modülünün içindeki bir fonksiyonu kullanarak random bir sayı üretip bu sayıyı tahmin etmeye çalışıcaz. 

import time # program 1 sn liğine bekleyecek. 

print("""
*****************

SAYI TAHMİN OYUNU 

1 ile 40 arasında sayıyı tahmin et. 
*****************
""")

rastgele_sayı = random.randint(1,40) # bu iki sayı dahil bir sayı üretecek. 

tahmin_hakki = 7

while True: # biz sayımızı tahmin edinceye kadar bu döngü dönecek. 
    tahmin = int(input("Tahmininiz:"))
    if (tahmin < rastgele_sayı):
        print("bilgiler sorgulanıyor.")
        time.sleep(1) #sleep fonksiyonuyla 1 saniye durdurduk. 
        print("Daha yüksek bir sayı söyleyin:")

        tahmin_hakki -= 1

    elif (tahmin > rastgele_sayı):
        print("Bilgiler sorgulanıyor.")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin.")

        tahmin_hakki -= 1
    
    else:
        print("Bilgiler sorgulanıyor.")
        time.sleep(1)
        print("Tebrikler sayınız:",rastgele_sayı)
        break
    if tahmin_hakki == 0:
        print("tahmin hakkınız bitti.")


