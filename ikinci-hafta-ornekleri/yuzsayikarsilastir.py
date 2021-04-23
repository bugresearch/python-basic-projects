x = int(input("Bir Sayı Giriniz: "))
enbuyuk = x
enkucuk = x
sayac =  1

while (100 > sayac):
    x = int(input("Bir Sayı Giriniz: "))
    if enkucuk > x:
        enkucuk = x
    if enbuyuk < x:
        enbuyuk = x
    sayac+= 1

print(enbuyuk)
print(enkucuk)
