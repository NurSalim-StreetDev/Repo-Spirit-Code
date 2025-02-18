'''
bagaimana jika bangyak argumen dan kita hanya ingin salah satu saja
'''

def macam (A1=1,A2=2,A3=3,A4=4,A5=5):
    return A1 +A2 + A3 + A4 + A5
print (macam (A4=5)) # dengan deflaut argumen dapat di rubah oleh input 
# sesuai densan prioritas python

input_angka = int(input('Masukan angka : '))
input_angka_1 = int(input('Masukan angka : '))

hasil = input_angka + input_angka_1
print (hasil)

