import datetime as dt
import os

Mahasiswa_Template = {
    'Nama' : 'Nur',
    'NIM' : '220180101',
    'Alamat' : 'padang',
    'Lahir' : dt.datetime(2001,5,28)
}

while True:
    Data_Mahasiswa = {}
    os.system('cls')
    print(f"{'Selamat Datang':^20}")
    print(f"{'Dalam Data Mahasiswa':^20}")
    print('='*20)

    Mahasiswa = dict.fromkeys(Mahasiswa_Template.keys())
    Mahasiswa['Nama'] = input("Nama Mahasiswa: ")
    Mahasiswa['NIM'] = int(input('NIM Masiswa: '))
    Mahasiswa['Alamat'] = input('Alamat Mahasiswa: ')

    TAHUN_LAHIR = int(input("Tahun Lahir: "))
    BULAN_LAHIR = int(input('Bulan Lahir: '))
    TANGGAL_LAHIR = int(input('Tanggal Lahir: '))

    Mahasiswa['Lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    Data_Mahasiswa.update({'key':Mahasiswa})
    for Mahasiswa in Data_Mahasiswa:
        Key = Mahasiswa

        Nama = Data_Mahasiswa [KEY] ['Nama']
        NIM = Data_Mahasiswa [KEY] ['NIM']
        Alamat = Data_Mahasiswa [KEY] ['Alamat']
        Lahir = Data_Mahasiswa [KEY] ['Lahir'].strftime("%x")
        print(f'{KEY:<6}'), {Nama:<17}, {NIM:<8}, {Alamat^10}, {Lahir:^10}