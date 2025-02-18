 
#oke mari kita latihan serius
import os
#baiklah kaawan
os.system('cls')
# header
def judul ():    
    print ('Menghitung Luas dan Keliling'.center(40))
    print ('Persegi atau Kubus'.center(40))
    print (40 * '.')

#input User
def input_user ():
    Lebar_1= int(input('Masukan lebar persegi\t:'))
    Panjang_1 = int(input('Masukan panjang persegi\t:'))
    return Lebar_1, Panjang_1
#selanjutnya hitung luas dan kelliling
def Hasil_luas (Lebar_1, Panjang_1):
    return Lebar_1 * Panjang_1

def Hasil_keliling (Lebar_1, Panjang_1):
    return 2 * (Lebar_1 + Panjang_1)

#selanjutnya membuat output luas dan Keliling

# Membuat program Utama
running = True
while running:
    judul ()
    status =input('Apakah anda ingin menghitung? (Y/N)\t:') 
    if status == 'Y':
            Lebar, Panjang = input_user ()
            Luas = Hasil_luas (Lebar, Panjang)
            Keliling = Hasil_keliling (Lebar, Panjang)
            print (f'Luas persegi dari {Lebar} * {Panjang} = {Luas}')
            print (f'Keliling dari persegi dari 2 * {Lebar} + {Panjang} = {Keliling}\n')
    
    elif status == 'N':
         print ('\nTerimaksih telah mencoba\n\n')
         running = False
            
    # elif status != 'Y' and 'N':
    #     print ('\nMohon masukan Y or N\n\n')
    #     break 
    else :
        print ('\nMohon Inputkan Y or N\n\n')

print ('Program selesai'.center (40,'='))

