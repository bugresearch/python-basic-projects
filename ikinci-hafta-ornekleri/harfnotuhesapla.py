x = int(input("Vize Notunuzu Giriniz: "))
y = int(input("Final Notunuzu Giriniz: "))

ortalama = (x*4 + y*6)/10

if ortalama > 90:
    print("A")
elif ortalama > 80:
    print("B")
elif ortalama > 70:
    print("C")
elif ortalama > 60:
    print("D")
else:
    print("F")

print("Ortalama: "+str(ortalama))
