#ada data
data = ['salim','ucup','nur','hakim']

#mengambil data
data_1 = data[0]
print(f'data pertama index 0 adalah = {data_1}')
data_2 = data[3]
print(f'data pertama index 3 adalah = {data_2}')

#cara mengambil info jumlah menggunakan len
panjang_data = len(data)
print (f'panjang list dari variabel data adalah {panjang_data}')

#Manipulasi listnya
#Menambahkan item sesuai posisi
print (f'\n data sebelum di rubah{data}')
data.insert(1,'otong')
print (f'setelah insert {data}')

#menggunakan append yang langsung menambahkan di akhir data
data.append('jejeng')
print (data)

#Memnggabungkan list denganlist
data_baru = ['gilang','rizky','huja','kiki']
data.extend(data)
print(f' data baru \n{data}')
panjang_data = len(data)
print (f'panjang data {panjang_data}')