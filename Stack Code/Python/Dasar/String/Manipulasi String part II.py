#Merubah case dari String
salam = 'bro'
print ('salam', salam)
salam = salam.upper() # Menjadi huruf tebal semua
print ('salam', salam)

alay = 'aku GiL a semua'
alay = alay.lower() # kecil normal semua huruf
print ('lower', alay)

#pengecekan dengan isX
#contoh pengecekan lowwer case
Vab = 'aku suka'
Cek_lower = Vab.islower() # jika nggak semua lower maka akan false
print (Vab, 'apakah ada lower', Cek_lower)
#buat upper juga gitu

# selamjutnya adalah isalfa menegecek apakah semua huruf
Vab = 'salim'
a = Vab.isalpha()
print ('hurufkah semua', a)
# selanjutnya adalah isalnum mengecek apakah ada huruf
Vab = 'salim'
a = Vab.isalnum()
print ('angkakah semua', a)
# isdecimal --> angka semua
Vac = 'salim1234'
a = Vac.isdecimal()
print ('decimalkah\n semua', a)
# isspace ---> mengecek spasi, tab, neewline, \n
Vac = 'salim hagasd'
a = Vac.isspace()
print ('sapsi adakah', a)
#is title -----> semua kata dimulai huruf besar
Vac = 'It Is Okay Not To Be Orkay'
a = Vac.istitle()
print ('besar semua kah', a)

#ngecek komponen menggunakan startwith ()  endswith ()  <---- kereeeen
print('\n\n\n')
start = 'Nur Salim Oppa'.startswith('Nur')
print ('star', start)
#endswith()
end = 'Nur salim Oppa'.endswith('Oppa')
print ('end', str(end))

#Komponen join()  split ()
pisah = ['aku', 'salim', 'suila', 'dan']
gabung = ','.join (pisah)
print (pisah)
print (gabung)
gabung = ' '.join (pisah)
print (gabung)
# pisahkan
gabung = 'salim suka makan pisang'
print (gabung.split(' '))

## Alokasi karakter rjust() ljust() centerjust()
kanan = 'Judul'.rjust(15)
print (kanan)
kiri = 'Judul'.ljust(15)
print (kiri)
tengah = 'Judul'.center(25)
print (tengah)
# kalau mau alokasi karakter dengan tanpa spasi aytau yang lain
tengah = 'Judul'.center(35,'-')
print (tengah)
# kebalikan atau menghilangkan  itu strip ()
tengah = 'Judul'.strip('-')
print (tengah)