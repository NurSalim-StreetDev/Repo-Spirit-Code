# kita akan menghitung jumlah entitas dalam list tertentu
#contoh
data_angka = [3,4,7,8,9,0,7,5,4,3,5,7,1,1,1,3,3,2,9,8]

jumlah_angka = data_angka.count(3)
jumlah_angka_1 = data_angka.count(7)

print (f'jumlah angka 3 adalah {jumlah_angka}')
print (f'jumlah angka 7 adalah {jumlah_angka_1}')

# selanjutnya menentukan index 
data = ['dudung','slam','jalan','ucup']

print (data)
index_dudung = data.index('dudung')
print (f'indexnya dudung adalah {index_dudung}')

# Bagaiman mengurutkan list
print (f'data angka sebelum di sort {data_angka}')
data_angka.sort()
print (f'data angka setelah di sort {data_angka}')