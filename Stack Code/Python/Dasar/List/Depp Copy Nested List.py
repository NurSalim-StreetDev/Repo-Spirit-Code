'''Kita akan mencoba cara mengambil data dalam nested list'''
Data_A = [1,2]
Data_B = [3,4]

Data_2d = [Data_A,Data_B]
Data_Copy = Data_2d.copy()
print(f'\nData 2D {Data_2d}')
print(f'Data Copy {Data_Copy}')

'''Lihat apa yang terjadi kalau kita merubah salah satu data'''
print('\nData setelah di rubah:')
'''maka data copy di list juga akan ikut berubah'''

'''cara agar kita dapat mengcopy list dengan nyaman yaitu pakai deepcopy'''
from copy import deepcopy

Data_2d = [Data_A,Data_B]
Data_deep = deepcopy(Data_2d)


Data_A[0] = 5 
print(f'\nData 2D {Data_2d}')
print(f'Data Copy {Data_Copy}')
print(f'Data Deep {Data_deep}')

''' Sekrang sekarang kita akan mengambil addres'''
print(f'\nAddres dari Data_2D {hex(id(Data_2d))}')
print(f'Addres dari Data_Copy {hex(id(Data_Copy))}')
print(f'Addres dari Data Deep{hex(id(Data_deep))}')


