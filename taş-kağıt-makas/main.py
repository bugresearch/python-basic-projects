import random

bilgisayar = 0
kullanici = 0

while 1==1:

    veri = int(input("Taş: 0, Kağıt: 1, Makas: 2 :"))
    data = ["Taş","Kağıt","Makas"]
    rastgele = random.randint(0,2)
    tahmin = data[rastgele]
    print("Tahminim:",tahmin)
    if veri == rastgele:
        print("Berabere")
    else:
        if veri == 0 and rastgele == 1:
            print("Ben Kazandım")
            bilgisayar+=1
        if veri == 1 and rastgele == 2:
            print("Ben Kazandım")
            bilgisayar += 1
        if veri == 2 and rastgele == 0:
            print("Ben Kazandım")
            bilgisayar += 1
        if veri == 0 and rastgele == 2:
            print("Sen Kazandım")
            kullanici += 1
        if veri == 1 and rastgele == 0:
            print("Sen Kazandım")
            kullanici += 1
        if veri == 2 and rastgele == 1:
            print("Sen Kazandım")
            kullanici += 1
    print("Bilgisayar",bilgisayar,"-",kullanici,"Kullanıcı")
    if kullanici == 3 or bilgisayar == 3:
        break
