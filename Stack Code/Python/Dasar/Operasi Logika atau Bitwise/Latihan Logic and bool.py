''' kali ini adalah logika dari beberapa  boolean'''
# terdapat beberapa logika di boolean
# ada not, or, and, xor

# pertama not
print ('----------Not----------')
a = True
c = not a
print ('hasil dari not a = ', c)
# jadi penggunaan dari not adalah membalikan bool nilai dari suatu variabel yang dari true jadi false atau sebaliknya

print ('----------or----------') # ada banyak
a = True
b = False
hasil_1 = a or b
hasil_2 = a or a
hasil_3 = b or a
hasil_4 = b or b
print ('hasil', a, 'or', b, '=', hasil_1)
print ('hasil', a, 'or', a, '=', hasil_2)
print ('hasil', b, 'or', a, '=', hasil_3)
print ('hasil', b, 'or', b, '=', hasil_4)
# or adalah pembanding variabel atau literasi yang memilih satu kemungkinan prioritas
#prioritas 1. kalu ada trus utamakan= true. 2. keduanya true maka true. 3. kalu keduanya false maka akan dipiilih false itu sendiri

print ('----------and----------') # ada banyak
a = True
b = False
hasil_1 = a and b
hasil_2 = a and a
hasil_3 = b and a
hasil_4 = b and b
print ('hasil', a, 'and', b, '=', hasil_1)
print ('hasil', a, 'and', a, '=', hasil_2)
print ('hasil', b, 'and', a, '=', hasil_3)
print ('hasil', b, 'and', b, '=', hasil_4)
# ingat operator and kedua pembanding harus sama atau akan bakalan false

print ('----------Xor----------') # ada banyak
a = True
b = False
hasil_1 = a ^ b
hasil_2 = a ^ a
hasil_3 = b ^ a
hasil_4 = b ^ b
print ('hasil', a, '^', b, '=', hasil_1)
print ('hasil', a, '^', a, '=', hasil_2)
print ('hasil', b, '^', a, '=', hasil_3)
print ('hasil', b, '^', b, '=', hasil_4)
# nah ini susah, Xor akan true jika hanya salah satunya ada true bukan keduanya
# semua ini juga bisa dibilang sebagai buku keadilan dan panduan anak IT