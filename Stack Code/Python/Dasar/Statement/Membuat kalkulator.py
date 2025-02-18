print (30 * '=')
print ('Kalkulator Sederhana'.center(30))
print (30 * '=')

Angka_1 = float(input('\nMasukan Angka pertama\t:'))
Operator = input('Masukan Oepratornya\t:')
Angka_2 = float(input('Masukan Angka kedua\t:'))

if Operator == '+':
    Hasil = Angka_1 + Angka_2
    print (f'{Angka_1} + {Angka_2} = {Hasil}')
    
elif Operator == '-':
    Hasil = Angka_1 - Angka_2
    print (f'{Angka_1} + {Angka_2} = {Hasil}')

elif Operator == '*':
    Hasil = Angka_1 * Angka_2
    print (f'{Angka_1} * {Angka_2} = {Hasil}')

elif Operator == '/':
    Hasil = Angka_1 / Angka_2
    print (f'{Angka_1} / {Angka_2} = {Hasil}')


else :
    print ('Yang benarlah inputnya, lelah gue cuk!!')






















