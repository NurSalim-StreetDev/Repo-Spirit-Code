'''Belajar sedikit tapi bukit'''
# pertama Copy Dictionery
print('\nContoh copy Dic\n')
Teman_Teman = {
    'Lim':'Salim',
    'Ky':'Frizky',
    'No':'Rino',
    'Mas':'Dimas',
    'Ny':'Fanny'
}

Kawan = Teman_Teman.copy() #pakai copy bakalan tidak berubah karena menjadi 2 hal yang berbeda
print(f'Teman-Teman : {Teman_Teman}\n')
print(f'Kawan : {Kawan}\n')

Teman_Teman['Lim'] = 'Salim Telah Dicopy' #Copy adalah menyalin item lain tanpa merubah item dasar, beda denan clonning
print(f'Teman-Teman : {Teman_Teman}\n')
print(f'Kawan : {Kawan}\n')

# Kedua adlah POP Dic bakalan mengambil dan nilangin yang di awal
print('\n\nContoh POP Dic\n')
Data_Lim = Kawan.pop('Lim')
print(f'Data_Lim : {Data_Lim}\n')
print(f'Kawan : {Kawan}|n')

#Pop Item Dic adalah mengambil data Terakhir
print('\n\nContoh POP Item')
Data_Terakhir = Kawan.popitem()
print(f'Data Terakhir {Data_Terakhir}\n')
print(f'Kawan {Kawan}\n')