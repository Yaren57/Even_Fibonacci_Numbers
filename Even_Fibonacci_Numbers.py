toplam = 0
sayi1 = 1
sayi2= 2

while (sayi2<4000000) :
    sayi3 = sayi1 + sayi2
    if (sayi3 % 2) == 0:
        toplam += sayi3
    sayi1 = sayi2
    sayi2 = sayi3
print(toplam)