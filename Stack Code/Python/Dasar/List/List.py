## ---LIST---##

#kumpulan data number
#contoh
data_angka = [1,2,3,4,5]
print (data_angka)

#kumpulan data string
nama_siswa = ['salim', 'ucup', 'kami']
print (nama_siswa)

#kumpulan boolean
data_bool = [True, False, False, True]
print (data_bool)

#data campuran
campuran_ya = [1,True, 'salim', 'ucup', 6]
print (campuran_ya)

#cara alternatif membuat list
data_range = range(0,10,2)
data_list = list(data_range)
print (data_list)

#membuat list dengan for loop atau list comprehensif
list_for = [i for i in range (0,10)]
print (list_for)

#list dengan for if
list = [i for i in range(0,10) if i != 5]
print (list)

#list genap
list_genap = [i for i in range(10) if i%2 ==0 ]
print(list_genap)

#list ganjil
list_genap = [i for i in range(10) if i%2 !=0 ]
print(list_genap)

#list perpangkatan 2
list_genap = [i**2 for i in range(10) if i%2 ==0 ]
print(list_genap)

#lagi
lsir__ = [i for i in range(10) if i != 5]
print(lsir__)
