'''hai teman-teman!, kali ini kita akan melakukan program konversi antar suhu'''
# kita akan membuat yang sederhana
print ('----------Program Konversi Suhu CELCIUS----------')
# Konversi Celcius
C = float(input('Nominal Derajat Celcius:'))
R = (4/5) * C
K = C + 273
F = (9/5) * C + 32
print (f'Konversi Celcius    --> ', C, 'C')
print (f'Konversi Reamur     --> ', R, 'R')
print (f'Konversi Kelvin     --> ', K, 'K')
print (f'Konversi Fahrenheit --> ', F, 'F')
print ('      ----------Selesai----------')

print ('----------Program Konversi Suhu REAMUR----------')
R = float(input('Nominal Derajat Reamur:'))
C = (5/4) * R
K = C + 273
F = (9/4) * R + 32
print (f'Konversi Celcius    --> ', C, 'C')
print (f'Konversi Reamur     --> ', R, 'R')
print (f'Konversi Kelvin     --> ', K, 'K')
print (f'Konversi Fahrenheit --> ', F, 'F')
print ('      ----------Selesai----------')

print ('----------Program Konversi Suhu Kelvin----------')
K = float(input('Nominal Derajat Kelvin:'))
C = K -  273
R = 4/5 * (K - 273)
F = 9/5 * (K - 273) + 32
print (f'Konversi Celcius    --> ', C, 'C')
print (f'Konversi Reamur     --> ', R, 'R')
print (f'Konversi Kelvin     --> ', K, 'K')
print (f'Konversi Fahrenheit --> ', F, 'F')
print ('      ----------Selesai----------')

print ('----------Program Konversi Suhu Fahrenheit----------')
F = float(input('Nominal Derajat Fahrenheit:'))
C = 5/9 * (F - 32)
R = 4/9 * (F - 32)
K = 5/9 * (F - 32) + 273
print (f'Konversi Celcius    --> ', C, 'C')
print (f'Konversi Reamur     --> ', R, 'R')
print (f'Konversi Kelvin     --> ', K, 'K')
print (f'Konversi Fahrenheit --> ', F, 'F')
print ('      ----------Selesai----------')
print ('>>>>>>>>>>Program Selesai<<<<<<<<<<')