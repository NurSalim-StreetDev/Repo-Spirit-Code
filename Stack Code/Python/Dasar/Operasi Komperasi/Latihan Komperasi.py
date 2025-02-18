'''Baiklah kawan sekarang kita akan melakukan studi ulang dalam operasi komperasi'''
'''nilai komperasi akan menujukan hasil bool'''
# Terdapat beberapa komperasi seperti <, >, =, <=, >=, ==, !=, is, is not

# pertama adalah operaso Komperasi <
print ('----------Lebih kecil dari (<)----------')
a = 5
b = 7
hasil_dari_1 = a < b
hasil_dari_2 = a < 5
hasil_dari_3 = a < 3
print ('a < b = ', hasil_dari_1)
print ('a < 5 = ', hasil_dari_2)
print ('a < 3 = ', hasil_dari_3)
# lebih kecil dari nilai pembandingnya tidak boleh sama

print ('----------Lebih besar dari (>)----------')
a = 8
b = 7
hasil_dari_1 = a > b
hasil_dari_2 = a > 5
hasil_dari_3 = a > 9
print ('a > b = ', hasil_dari_1)
print ('a > 5 = ', hasil_dari_2)
print ('a > 9 = ', hasil_dari_3)
# lebih besar dari nilai pembandingnya tidak bisa sama besar jadi false
print ('----------Lebih besar dari (==)----------')
a = 8
b = 7
hasil_dari_1 = a == b
hasil_dari_2 = a == 5
hasil_dari_3 = a == 8
print ('a == b = ', hasil_dari_1)
print ('a == 5 = ', hasil_dari_2)
print ('a == 9 = ', hasil_dari_3)
# jadi sama dengan adalah nilai pembanding yang membandingkan 2 nilai yang berbeda atau sama

print ('----------Lebih besar dari (!=)----------')
a = 8
b = 7
hasil_dari_1 = a != b
hasil_dari_2 = a != 5
hasil_dari_3 = a != 8
hasil_dari_4 = a != 9
print ('a != b = ', hasil_dari_1)
print ('a != 5 = ', hasil_dari_2)
print ('a != 8 = ', hasil_dari_3)
print ('a != 9 = ', hasil_dari_4)
# tidak sama akan membandingkan nilai yang tidak sama maka akn trure

print ('----------kurang sama dari (<=)----------')
a = 8
b = 7
hasil_dari_1 = a <= b
hasil_dari_2 = a <= 5
hasil_dari_3 = a <= 8
hasil_dari_4 = a <= 9
print ('a <= b = ', hasil_dari_1)
print ('a <= 5 = ', hasil_dari_2)
print ('a <= 8 = ', hasil_dari_3)
print ('a <= 9 = ', hasil_dari_4)\
# kurang sama merupakan pembading yang dimilai dari nilai sama yang senilai

print ('----------kurang sama dari (>=)----------')
a = 8
b = 7
hasil_dari_1 = a >= b
hasil_dari_2 = a >= 5
hasil_dari_3 = a >= 8
hasil_dari_4 = a >= 9
print ('a >= b = ', hasil_dari_1)
print ('a >= 5 = ', hasil_dari_2)
print ('a >= 8 = ', hasil_dari_3)
print ('a >= 9 = ', hasil_dari_4)
# besar sama akan akan membandingkan nilai
# dari sma dengan dirinya sampai lebih besar

print ('----------kurang sama dari (is)----------')
a = 8
b = 7
hasil_dari_1 = a is b
hasil_dari_2 = a is 5
hasil_dari_3 = a is 8
hasil_dari_4 = a is 9
print ('a is b = ', hasil_dari_1)
print ('a is 5 = ', hasil_dari_2)
print ('a is 8 = ', hasil_dari_3)
print ('a is 9 = ', hasil_dari_4) 
# tidak sma akan memperlihatkan nilai yang tidak sejajar dengan dirinya 

print ('----------kurang sama dari (is not)----------')
a = 8
b = 7
hasil_dari_1 = a is not  b
hasil_dari_2 = a is not  5
hasil_dari_3 = a is not  8
hasil_dari_4 = a is not  9
print ('a is not  b = ', hasil_dari_1)
print ('a is not  5 = ', hasil_dari_2)
print ('a is not  8 = ', hasil_dari_3)
print ('a is not  9 = ', hasil_dari_4)
# kesimpulan is not adalah indikasi perintah untuk menyatakan pertidaksamaan suatu nilai
