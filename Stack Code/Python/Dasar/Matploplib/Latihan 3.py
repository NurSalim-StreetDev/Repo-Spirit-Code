
import matplotlib.pyplot as plt

labels = ['Laki-laki', 'Perempuan']
jumlah_siswa = [15, 10]

plt.pie(jumlah_siswa, labels=labels, autopct='%1.1f%%', startangle=90, colors=['blue', 'pink'])

plt.title('Distribusi Jenis Kelamin di Kelas')

plt.axis('equal')  
plt.show()
