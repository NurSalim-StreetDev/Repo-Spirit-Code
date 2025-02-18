import matplotlib.pyplot as plt

Kelas = ['Kelas A', 'Kelas B', 'Kelas C', 'Kelas D']
Jumlah_Siswa = [25, 30, 20, 35]

plt.bar(Kelas, Jumlah_Siswa, color=['blue', 'orange', 'green', 'red'])

plt.title('Jumlah Siswa Di Setiap Kelas')
plt.xlabel('Kelas')
plt.ylabel('Jumlah Siswa')

plt.show()