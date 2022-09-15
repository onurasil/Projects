from random import randint, randrange


hak = int(input("Lütfen hak sayınızı giriniz : "))
print("Lütfen 1 ile 10 arasında bir sayı yazınız")
puan = 100 / hak 
rastgele_sayi = randint(1,10)
sayac = 0

while hak>0 :
    hak -= 1 
   
    sayac += 1 
    tahmin = int(input("Sayı kaç : "))

    if tahmin == rastgele_sayi:
        print(f"Tebrikler sayıyı {sayac}.defada buldunuz:D.Puanınız : {100-((sayac-1)*puan)}")
        break
    elif tahmin<rastgele_sayi:
        print(f"Rastgele sayının altındasınız.")
        
    else:
        print(f"Rastgele sayının üstündesiniz.")

    if hak == 0 :
        print(f"hakkınız bitti.Tutulan sayı : {rastgele_sayi} ")    
    


