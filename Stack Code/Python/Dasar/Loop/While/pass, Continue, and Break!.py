# Contoh pass
a = 0 
while a < 5:
    a += 1
    print (f'Infiniti Loop {a}')
    if a == 3:
        pass # perintah pass akan membuat operasi aksi di atasnya di abaikan
print ('Finish')

print ('Akhir Dari Program 1'.center(30,'='))
# contoh Copntinue 1
a = 0
while a < 5:
    a += 1
    if a == 3:
        print (f'Kondisi Khusus dari bilangan {a} ')
        continue # disini akan loncat ke kondisi awal atau home
    print (f'Infiniti Loop {a}') # pada bagian ini print pada loop ke 3 akan hilang

print ('Finish!')
print ('Akhir Dari Program 2'.center(30,'='))

# contoh Copntinue 2 bedanya
a = 0
while a < 5:
    a += 1
    print (f'Infiniti Loop {a}') # disini loop ke 3 akan ada
    if a == 3:
        print (f'Kondisi Khusus dari bilangan {a} ')
        continue

print ('Finish!')
print ('Akhir Dari Program 2'.center(30,'='))

# contoh Break !!!

