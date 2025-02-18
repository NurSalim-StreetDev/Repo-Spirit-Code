#Date and Time nmenggnakan data bawaan python
def cek_umur ():
    import datetime as dt
    print (' Menghitung umur anda ')

    Hari_ini = dt.date.today()
    print (f'Date : {Hari_ini}')

    print ('\nSilahkan Masukan tanggal lahir anda !\n')

    Tag = int(input('Masukan Tanggal lahir Anda\t: '))
    Bul = int(input('Masukan Bulan lahir Anda\t: '))
    Thn = int(input('Masukan Tahun lahir Anda\t: '))

    Data_lahir = dt.date(Thn,Bul,Tag)
    umur_hari = Hari_ini - Data_lahir 
    umur_bulan = (umur_hari.days % 365) // 30
    umur_tahun = umur_hari.days // 365

    print (f'\nData Kelahiran Anda adalah\t: {Data_lahir}\nDi Hari\t\t\t\t: {Data_lahir:%A}')
    print (f'Total umur Anda perhari adalah\t: {umur_hari.days} Hari')
    print (f'Total umur Anda perbulan adalah\t: {umur_bulan} Bulan')
    print (f'Total umur Anda pertahun adalah\t: {umur_tahun} Tahun')

cek_umur()




