# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# # Contoh penggunaan
# arr = [5, 2, 4, 6, 1, 3]
# insertion_sort(arr)
# print("Hasil pengurutan:")
# print(arr)

def fungsi_kondisional(Nilai):
    if Nilai < 0:
        return "Nilai negatif"
    elif Nilai > 0:
        return "Nilai positif"
    else:
        return "Angka 0 jelaslah Positif"

def main():
    Y = True
    pengulangan_pertama = True  # Tambahkan variabel untuk mengidentifikasi pengulangan pertama
    while Y:
        try:
            if pengulangan_pertama:  # Cetak kata pembukaan atau judul hanya pada pengulangan pertama
                print('\n','Program Kondisi Angka'.center(50,'='))
                pengulangan_pertama = False  # Setel variabel ini ke False setelah pengulangan pertama

            Nilai = int(input('Silahkan Masukan Angka: '))
            hasil = fungsi_kondisional(Nilai)
            print('Hasil:', hasil)

            pilihan = input('Jika Anda selesai, ketik "N" (untuk melanjutkan, tekan Enter): ')
            if pilihan.lower() == 'n':
                Y = False
        except ValueError:
            print('Tolong masukkan angka yang valid.')

    print('Terimakasih Menggunakan Jasa Kami')

if __name__ == "__main__":
    main()




# while True:
#     try:
#         Nilai =int(input('Silahkan Masukan Angka\t:'))
#         if Nilai < 0:
#             print('Nilai Negatif')
#         elif Nilai > 0:
#             print('Nilai Positif')
#         # elif Nilai == 0:
#         #     print('0 Adalah Positif')
#         else:
#             print('Angka 0 adalah positif')
#     except:
#         print('Tolong masukan Angka Ya!')
#     finally:
#         print('Terimakasih')


