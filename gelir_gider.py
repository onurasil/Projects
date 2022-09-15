def gelir_gider():
    while True:
        maas = int(input("Maaşınız : "))
        kira = int(input("Kira : "))
        su = int(input("Su faturası  : "))
        elektrik = int(input("Elektrik faturası  : "))
        internet = int(input("İnternet faturası  : "))
        tel = int(input("Telefon faturası  : "))
        yol = int(input("Yol masrafı  : "))
        mutfak = int(input("Mutfak giderleri : "))
        toplam_masraf = kira + su + elektrik + internet + tel + yol + mutfak
        net_kalan = maas - toplam_masraf
        if net_kalan > 0:
            print (f"Bu ay harcama limitini aşmadınız ve hala harcayabileceğiniz {net_kalan} TL'niz hesabınızda bulunmaktadır.")
            break
        else:
            print(f"Bu ay harcama limitini {net_kalan} Tl kadar aştınız.Harcamalarınıza dikkat edin !")
            continue
            
            
gelir_gider()






    
