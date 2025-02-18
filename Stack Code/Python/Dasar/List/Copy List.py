'''Teknik menduplikat list dengan list baru'''

a = ['salim', 'Paulus', 'kita', 'otong']
print(f'nilai awal a {a}')
b = a
print(f'b = a sehingga b menjadi{b}')
'''contoh di atas adalah copy list yang membawa address sehingga jika a di rubah maka b akan mengikuti'''
# seperti
a[1] = 'babang'
b.sort()
print(f'nilai a berubah menjadi{a}')
b = a
print(f'maka b = a akan mengikuti perubahan a menjadi sama {b}')
'''keduanya saling terikat, sehingga jika b pun di rubah maka a juga berubah terlihat dari addres yang sama'''
#mari kita lihat addresnya
print('addres mereka sama dapat dilihat dari berikut')
print(f'Addres dari a adalah {hex(id(a))}')
print(f'Addres dari a adalah {hex(id(b))}')
print('mereka sama')
print('kesimpulanya, hal di atas bukan mengcopy dengan benar')





print('\n\n berikut cara mengcopy dengan benar sehingga menghasil addres baru yang independen')
c = a.copy()
print(f'Addres dari a adalah {hex(id(a))}')
print(f'Addres dari a adalah {hex(id(b))}')
print(f'Addres dari a adalah {hex(id(c))}') #disini addres c berbeda

print('seperti yang kalian lihat addres c sangat berbeda, sehingga kalau kita rubah')
c[1] = 'Yuyin'
print('kita rubah indexs 1 di c menjadi Yuyin sehingga c menjadi')

print(a)
print(b)
print(c) 
'''index c berhasil di rubah semenattra yang lain tetep sama'''
