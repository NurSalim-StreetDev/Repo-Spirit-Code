listkota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makasar']

for kota in enumerata(listkota):
    print (i, Kota)
    
# 0 sampai 4
for i in range (5):
    print ('Perulanagn ke-',i)
    
#10 sampai 15
for i in range (10,16):
    print ('Perulanagn ke-',i)

#Bilangan genap kelipatan 2
for i in range (2,12,2):
    print ('Perulanagn bilangan genap ke-',i)

#Bilangan Ganjil kelipatan 2
for i in range (1,12,2):
    print ('Perulanagn bilangan ganjil ke-',i)
    
for i in range (10,20):
    # hentikan jika i == 15
    if (i == 15):
        break
    print(i)
    
#continue
for i in range (10,20):
    # hentikan jika i == 15
    if (i == 15):
        Continue
    print(i)

# for... else
listkota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makasar']

for kota in (listkota):
    print (i, Kota)
else :
    print ('tidak ada lagi item yang tersisa')