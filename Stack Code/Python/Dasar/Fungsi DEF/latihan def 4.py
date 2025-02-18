# def huruf_kecil ():
#     a = 'SALIM'
#     hasil_2 = a.lower()
#     hasil = len(a)
#     print (hasil)
#     print (hasil_2)

# huruf_kecil ()

# def kalkulator ():
#     a =input(int())
#     b =input(int())
#     c = a + b 
#     print (c)
# kalkulator ()

# Name_1 = 'Nur'
# Password_1 = 210301
# User_1 = Name_1 or Password_1

# Name_2 = 'Baba'
# Password_2 = 210302
# User_2 = Name_2 or Password_2

# Name_3 = 'Asta'
# Password_3 = 210303
# User_3 = Name_3,Password_3


def input_user ():
    Input_nama= str(input('Masukan Username\t:'))
    Input_password= int(input('Masukan Pasword anda\t:'))
    return Input_nama,Input_password

#selanjutnya hitung luas dan kelliling
def User_1(Nama,Password):
    Nama     = 'Nur'
    Password = 210301
    return Nama,Password

def User_2(Nama,Password):
    Nama     = 'Baba'
    Password = 210302
    return Nama,Password

def Utama():
    masukan = input_1,input_2 = input_user()
    Data_1 = User_1(input_1,input_2)
    Data_2 = User_2(input_1,input_2)
    if masukan == Data_1 :
        print ('oke')
    elif masukan == Data_2 :
        print ('oke_2')
Utama()