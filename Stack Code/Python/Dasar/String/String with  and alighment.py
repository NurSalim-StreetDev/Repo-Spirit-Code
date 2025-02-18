''' With and Multiline'''
# String standard
Nama = 'Nur Salim'
Kelas = 'A4'
umur = 18
tinggi = 175
# contoh pengggunaan enter \n
data =f'Nama = {Nama}\nKelas = {Kelas} \nUmur = {umur} \nTinggi = {tinggi}'
print (data)

a = 'SELESAI'.center(25,'-')
print (a)
# ini adalh pengunaa data multiline and triplets and meratakan atau mempercantik hasil
data = f'''Nama   = {Nama:>9}
Kelas  = {Kelas:>9}
Umur   = {umur:>9}
Tinggi = {tinggi:>9}
'''
print (data)