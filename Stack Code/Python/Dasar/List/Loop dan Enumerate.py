'''kali ini kita akan mengulangi cara menglooping data list'''

print('For')
Angka = [5,6,4,8,1]
for i in Angka:
    print(f'Angka {i}')
Nama = ['salim','Dufu']
for i in Nama:
    print(f'Nama {i}')

print('\nFor dan range')
Angka = [5,6,4,8,1]
Hitung = len(Angka)
for i in range(Hitung):
    print(f'Angka {Angka[i]}')

print('\nWhile')
Angka = [5,6,4,8,1]
Hitung = len(Angka)
a = 0
while a < Hitung:
    print(f'Angka {Angka[a]}')
    a += 1

print('\nPrint Comprehension')
Angka = [5,6,4,8,1]
[print(f'Angka {i}') for i in Angka]

print('\nLoop dan Enumerate')
Angka = [5,6,4,8,1]
for Index,Data in enumerate(Angka):
    print(f'Index {Index} Data {Data}')

print('\nUji Coba pangkat')
Angka = [5,6,4,10,1]
[print(f'Angka {i**2}') for i in Angka]

print('\nComprehensive dan Enumerate')
Angka = [5,6,4,10,9]
[print(f'Index {Index} Angka {i**2}' for Index,i in enumerate(Angka))]
