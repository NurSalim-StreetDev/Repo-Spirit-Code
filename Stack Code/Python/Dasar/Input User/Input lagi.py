'''MAri kita coba beberapa hal'''
print('-_' * 50)
print('Tutorial memasak nasi goreng'.center(50))
print('-_' * 50)

'''kita buat input yang di konversi ke interger dan string atau bahkan Boleean'''

Benar = True
while Benar:
    Masukan_Awal = input('Silahkan ketik\n:')
    try:
        Masukan_Angka = int(Masukan_Awal)
        Masukan_Huruf = str(Masukan_Awal)
        if Masukan_Angka > 0 or Masukan_Angka == 0:
            print(f'Angka {Masukan_Angka} yang Anda masukan adalah bilangan positif')
        elif Masukan_Angka < 0:
            print(f'Angka {Masukan_Angka} yang Anda masukan adalah bilangan negatif')
        elif Masukan_Awal == Masukan_Huruf:
            print ('Mohon Masukan Angka')
    except:
        print('Sepertinya Terjadi Kesalahan')
