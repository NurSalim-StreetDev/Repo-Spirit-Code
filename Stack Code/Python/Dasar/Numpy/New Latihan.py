import numpy as np

a = [[1,2,3,4,5,6,7,8,9,0]]
print(a)

A = np.arange(10)
print(A)

print('elemen ke 0 dari A adalah', A[0])
print('elemen ke 7 dari A adalah', A[7])
print('elemen ke terakhir dari A adalah', A[-1])

print('\nselanjutnya array 2d\n')

B = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(B[0])
print(B[0,2])
print(B[-1])
print(B[-1,2])

print('\n slicing mengambil nilai dalam array dengan rentang tertentu')

C = np.arange(10)
print('Elemen dari 5 dari array C adalah ', C[0:5])
print('Elemen dari 4 sampai akhir dari array C adalah ', C[4:])
print('Elemen dari 5 dari array C adalah ', C[0:4])

print('\n slicing multidimensi\n')

D = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(D[1:,])
print(D[1:,1:])
print(D[-2:,])


print('\nLatihan Pengolahan data')

nilai_mahasiswa = np.array([75, 80, 92, 60, 88, 77, 90, 83, 70, 85])

nilai_minimal = np.min(nilai_mahasiswa)
print(f'Nilai Minimal: {nilai_minimal}')

nilai_maksimal = np.max(nilai_mahasiswa)
print(f'Nilai Maksimal: {nilai_maksimal}')

nilai_rata_rata = np.mean(nilai_mahasiswa)
print(f'Nilai Rata-rata: {nilai_rata_rata:.2f}')

standar_deviasi = np.std(nilai_mahasiswa)
print(f'Standar Deviasi: {standar_deviasi:.2f}')
    nilai_total = np.sum(nilai_mahasiswa)
print(f'Nilai Total: {nilai_total}')

