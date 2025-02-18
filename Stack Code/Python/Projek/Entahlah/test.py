'''
Mari kita buat suatu yang super RUMIT
'''
# mari kita buat sebuah proyek gabungan darn semua yang 
# kita pelajari sejauh ini
#pertama adalah halaman judul dulu
def header ():
    import datetime as dt
    print ('\n')
    print ('Proyek Uji Coba Semuanya'.center(50))
    print ('Berupa Penyajian Data Analis'.center(50))
    print ('Harus Berhasil!!'.center(50))
    print ('-_' * 25)
    tgl = dt.date.today()
    print (f'Tanggal\t: {tgl}')

#Date and Time nmenggnakan data bawaan python
def cek_umur (Nama_klien):
    import datetime as dt
    print (f' Mari kita menghitung umur anda {Nama_klien}'.center(50))
    print ('dan angka harapan hidup Anda'.center(50))

    Hari_ini = dt.date.today()
    print (f'Date : {Hari_ini}'.center(50))

    print (f'\nSilahkan Masukan tanggal lahir anda {Nama_klien}!')

    Tag           = int(input('Masukan Tanggal lahir Anda\t: '))
    Bul           = int(input('Masukan Bulan lahir Anda\t: '))
    Thn           = int(input('Masukan Tahun lahir Anda\t: '))
    Harapan_hidup = int(input('Masukan harapan hidup di regional Anda: '))

    Data_lahir = dt.date(Thn,Bul,Tag)
    umur_hari = Hari_ini - Data_lahir 
    umur_bulan = (umur_hari.days % 365) // 30
    umur_tahun = umur_hari.days // 365
    Sisa_hidup_tahun = Harapan_hidup - umur_tahun

    print (f'\nData Kelahiran Anda adalah\t: {Data_lahir}\nDi Hari\t\t\t\t: {Data_lahir:%A}')
    print (f'Total umur Anda perhari adalah\t: {umur_hari.days} Hari')
    print (f'Total umur Anda perbulan adalah\t: {umur_bulan} Bulan')
    print (f'Total umur Anda pertahun adalah\t: {umur_tahun} Tahun')
    print (f'Total sisa hidup anda {Nama_klien} berdasaran regional anda adalah {Sisa_hidup_tahun} Tahun, {umur_bulan} Bulan, {umur_hari.days} Hari')
    print ('Terimakasih'.center(50))

def program_aplikasi(Audiens) :
        print (f'Selanjutnya {Audiens} berikut adalah :')
        print ('Aplikasi latihan dan Kondinganya beserta penjelasanya')
        print ('''
        A. Bintang Bentuk Segitiga siku-siku
        B. Bintang Bentuk Piramida
        C. Bintang Bentuk Piramida Terbalik
        D. Bintang Bentuk Belah Ketupat
        E. Bintang Bentuk Jam Pasir
        F. Selesai
        ''')
        Pilihan = str(input('Silahkan tentukan pilihan Anda\t: '))
        if Pilihan == 'A' :
            print ('Pilihan Bagus, Bintang Bentuk Segitiga Siku-Siku akan berbentuk seperti berikut')
            tinggi = 8
            for i in range (1,tinggi):
                print ('*' * i)
            print ('''
            Dengan bentuk kodinganya adalah 
            tinggi = 8
            for i in range (1,tinggi):
            print ('*' * i)
            ''')
        elif Pilihan == 'B' :
            print ('Pilihan Bagus, Bintang Bentuk Piramida akan berbentuk seperti berikut')
            tinggi = 8
            for i in range (tinggi) :
                print (('*' * (1+2*i)).center(tinggi*2))
            print ('''
            Dengan bentuk kodinganya adalah
            tinggi = 8
            for i in range (tinggi) :
            print (('*' * (1+2*i)).center(tinggi*2))
            ''')
        elif Pilihan == 'F' :
            print (f'Sampai jumpa lagi {Audiens}')
            
        return Audiens



def input_user():
    Input_nama= str(input('Mohon masukan Username anda\t: '))
    Input_password= int(input(f'Masukan Password anda {Input_nama}\t: '))
    return Input_nama,Input_password

#selanjutnya membuat data
def User_1(Nama,Password):
    Nama     = 'Nur'
    Password = 210301
    return Nama,Password

def User_2(Nama,Password):
    Nama     = 'Baba'
    Password = 210302
    return Nama,Password

def User_3(Nama,Password):
    Nama     = 'Salim'
    Password = 210303
    return Nama,Password

#ini adalah program utama
def Program_Utama():
    header()
    Masukan = input_1,input_2 = input_user()
    Data_1  = User_1(input_1,input_2)
    Data_2  = User_2(input_1,input_2)
    Data_3  = User_3(input_1,input_2)
    if Masukan == Data_1 or Masukan == Data_2 or Masukan == Data_3:
        print (f'Selamat Datang {input_1}\n')
        cek_umur(input_1)
        program_aplikasi (input_1)
    # elif Masukan == Data_2 :
    #     print (f'Selamat Datang {input_1}\n')
    #     cek_umur(input_1)
    # elif Masukan == Data_3 :
    #     print (f'Selamat Datang {input_1}\n')
    #     cek_umur(input_1)
    else :
        print ('Maaf Username atau Password yang anda masukan salah')


    
Program_Utama ()



