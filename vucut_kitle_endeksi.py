def vki(boy,kilo):
    boy = float(boy)
    kilo = int(kilo)
    sonuc = (kilo)/(boy**2)
    if (sonuc < 18.5):
        print(f"Vücut kitle endeksiniz {sonuc}.Zayıf kategorisindesiniz.")
    elif (sonuc < 30):
        print(f"Vücut kitle endeksiniz {sonuc}.Normal kategorisindesiniz.")
    elif (sonuc < 40):
        print(f"Vücut kitle endeksiniz {sonuc}.Obez kategorisindesiniz.")
    elif (sonuc < 50):
        print(f"Vücut kitle endeksiniz {sonuc}.Morid Obez kategorisindesiniz.")
    elif (sonuc > 50):
        print(f"Vücut kitle endeksiniz {sonuc}.Süper Obez kategorisindesiniz.")
boy = float(input("Lütfen boyunuzu giriniz : "))
kilo = int(input("Lütfen kilonuzu giriniz : "))

sonuc = vki(boy,kilo)
print(sonuc)    