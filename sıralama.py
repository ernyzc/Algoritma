a = int(input("lütfen 1. sayiyi giriniz : "))
b = int(input("lütfen 2. sayiyi giriniz : "))
c = int(input("lütfen 3. sayiyi giriniz : "))
d = int(input("lütfen 4. sayiyi giriniz : "))
e = int(input("lütfen 5. sayiyi giriniz : "))
dizi = [a,b,c,d,e,]

dizi.sort(reverse=True)
print(dizi)
küme = str(dizi)
dosya = open("C:\Ogrencisiralama.txt","w")
dosya.write(küme)
dosya.close()
