'''Terdapat tipe list dalam list yang digunakan untuk pengkolompokan data'''
#misal
List_1 = [1,2,3,4,5]
List_2 = [6,7,8,9,0]
List_3 = ['a','b','c','d','e']
List_2D = [List_1, List_2, List_3]
print(f'List 2D akan menjadi {List_2D}')


'''sehingga memiliki banyak kegunaan seperti'''
List_A = ['Salim',18,'Jepang']
List_B = ['Nur',25,'Amerika']
List_C = ['Azuli',45,'Somalia']
List_Anggota = [List_A,List_B,List_C]
'''untuk menampilkan hasilnya dengan benar maka bisa menggunakan Loop'''
for anggota in List_Anggota:
    print(f'Nama       :{anggota[0]}')
    print(f'Lahir      :{anggota[1]}')
    print(f'Negara Asal:{anggota[2]}\n')

print('\nselanjutnya kita akan mencoba membahs mengenai list nested copy yang memerlukan cara yang berbeda atau masalah reference')
#mari kita cpy
List_copy = List_Anggota.copy()
print(f'\nList copyan adalah{List_copy}')
print('disini kita akan mencoba merubah list A di indexs 0 dan lihat apakah data lama dan data copyan ikut berubah')
List_A[0] = 'Hujan'
print(f'\nList Anggota adalah{List_Anggota}')
print(f'List Copyan adalah{List_copy}')
print(f'disini data baru \ copyan malah ikut berubah, hal ini akan di bahas di Nested list cpy')