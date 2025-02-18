#Kali ini kita akan mengikuti contoh dari kleas terbuka

def Assignment(a): # hehe ini aku buat pakai fungsi
    print('Nilai A awal adalah', a)
    a += 1 
    print('Jika nilai A += 1 maka hasilnya', a)
    a -= 1
    print('Jika nilai A -= 1 maka hasilnya', a)
    a *= 2
    print('Jika nilai A *= 2 maka hasilnya', a)
    a /= 2
    print('Jika nilai A /= 2 maka hasilnya', a)

a = 10
Assignment(a)

a %= 3
print('Jika nilai A %= 3 maka hasilnya', a)

a = 10
a //= 3 # ingat ini flor division artinya berapa banyak bisa di bagi
print('Jika nilai A //= 3 maka hasilnya', a)


'''Selanjutnya kita coba pangkat'''
a = 10
a **= 3
print('Jika nilai A **= 3 maka hasilnya', a)


'''Mau Coba dari Boolean atau BItwisde'''
#OR
print('\nini OR')
a = True
print('Nilai A adalah', a)
a |= False
print('Nilai dari A |= False adalah', a)
#atau
a = False
print('\nNilai A adalah', a)
a |= False
print('Nilai A |= False adalah', a)
#atau
a = True
print('\nNilai A adalah', a)
a |= True
print('Nilai A |= True adalah', a)

#ini and
print('\nini and')
a = True
print('Nilai A adalah', a)
a &= False
print('Nilai dari A &= False adalah', a)
#atau
a = False
print('\nNilai A adalah', a)
a &= False
print('Nilai A &= False adalah', a)
#atau
a = True
print('\nNilai A adalah', a)
a &= True
print('Nilai A &= True adalah', a)

#ini Xor
print('\nini Xor')
a = True
print('Nilai A adalah', a)
a ^= False
print('Nilai dari A ^= False adalah', a)
#atau
a = False
print('\nNilai A adalah', a)
a ^= False
print('Nilai A ^= False adalah', a)
#atau
a = True
print('\nNilai A adalah', a)
a ^= True
print('Nilai A ^= True adalah', a)

#geser geser
a = 0b0100
print('\nnilai', format(a, '04b'))
a >>= 2
print('nilai a >>= 2 maka akan menjadi', format(a, '04b'))
a <<= 1
print('nilai a <<=  1 menjadi', format(a, '04b'))