x = int(input("Birinci Sayı: "))
y = int(input("İkinci Sayı: "))
z = int(input("Üçüncü Sayı Sayı: "))

enbuyuk = x
enkucuk = x

if y > enbuyuk:
    enbuyuk = y

if z > enbuyuk:
    enbuyuk = z

if enkucuk > y:
    enkucuk = y

if enkucuk > z:
    enkucuk = z


print("En Büyük Değer: "+str(enbuyuk))
print("En Küçük Değer: "+str(enkucuk))
