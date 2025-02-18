import datetime

Mahasiswa_4 = {
    'Nama' : 'Ucup Serucup',
    'NIM' : '220180124',
    'Alamat' : 'Samarinda',
    'Lahir' : datetime.datetime(2002,3,21)
}

Mahasiswa_3 = {
    'Nama' : 'Nur Salim',
    'NIM' : '220180123',
    'Alamat' : 'PAdang',
    'Lahir' : datetime.datetime(2001,5,10)
}

Mahasiswa_2 = {
    'Nama' : 'Dadang',
    'NIM' : '220180122',
    'Alamat' : 'Jakarta',
    'Lahir' : datetime.datetime(2003,10,17)
}

Mahasiswa_1 = {
    'Nama' : 'Kentong',
    'NIM' : '220180121',
    'Alamat' : 'Bengkulu',
    'Lahir' : datetime.datetime(2001,3,21)
}

Data_Mahasiswa = {
    'MAHASISWA_1' : Mahasiswa_1,
    'MAHASISWA_2' : Mahasiswa_2,
    'MAHASISWA_3' : Mahasiswa_3,
    'MAHASISWA_4' : Mahasiswa_4
}

print('{:^15}{:^15}{:^10}{:^15}{:^10}'.format('Kunci', 'Nama', 'NIM', 'Alamat', 'Lahir'))
print('-'*60)

for Mahasiswa in Data_Mahasiswa:
    KEY = Mahasiswa

    Nama = Data_Mahasiswa[KEY]['Nama']
    NIM = Data_Mahasiswa[KEY]['NIM']
    ALAMAT = Data_Mahasiswa[KEY]['Alamat']
    LAHIR = Data_Mahasiswa[KEY]['Lahir'].strftime('%x')

    print(f'{KEY:<15}{Nama:<15}{NIM:<10}{ALAMAT:<15}{LAHIR:<10}')