'''Terapat perbedaan dalam dalam List, Tuples, dan Set'''

#List punya index dan bisa di rubah
ListA = [1,2,3,4,5]
print(ListA[1])
ListA.append(1)
print(ListA)

#Tuple dia punya index tapi tidak bisa di rubah atau sentuh
TupleA = (1,2,3,4,5)
print(TupleA[1])
# TupleA.append(10) #hal ini akan membuat hasilnya error karerena 
#tidak ada assisghment nya
# print(TupleA)

#Set adalah daftar himpunan atau sekumpulan dimana dia tidak punya index tapi dapat di modifikasi
setA = {1,2,3,4,5}
# adalah daftar tidak ada urutan dan unik dan setiap elemen tidak bisa di ganti
