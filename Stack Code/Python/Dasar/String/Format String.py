'''Kita akan belajar Format string
'''

# contoh generic
#string
nama = 'Nur'
Format_str = f'Hello {nama}' 
print (Format_str)

#Boolean
boolean = True
Format_str = f'nilai Bool= {boolean}'
print (Format_str)

# Angka
angka = 2022
Format_str = f'tahun {angka}'
print (Format_str)

#Bilangan bulat
angka = 15
f_str = f'bilangan bulat {angka:d}'
print (f_str)

# kalau ribuan dan jutaan
angka = 20000000
f_str = f'ribuan {angka:,}'
print (f_str)

#kalau decimal gimana
angka = 2988.7088870756
f_str = f"decimal begini {angka:.3f}"
print (f_str)

#Menampilkan Leading zero
angka = 2988.7088870756
f_str = f"decimal begini {angka:0010.3f}"
print (f_str)

# Menampilkan + -
angka_minus = -105426
angka_plus = +103423658
fminus_str = f'minus {angka_minus:-0014.3f}'
fplus_str = f'plus {angka_plus:+00016.3%}' # tanda f terakhir artinta format vdecimal
print (fminus_str)
print (fplus_str)

#memformat persen
persen = 45 
fpersen_str = f'persen {persen:.2%}'
print (fpersen_str)

# adapat melakukan aritmatika di place holder
harga = 3000
jumlah = 5
f_str = f'total harga = Rp.  {harga * jumlah:,}'
print (f_str)

# format angnka lain (binary, octal, hexadecimal)
angka = 2252
f_binary = f'binary = {bin(angka)}'
f_octal = f'octal = {oct(angka)}'
f_hexa = f'hexadecimal {hex(angka)}'
print (f_binary)
print (f_octal)
print (f_hexa)