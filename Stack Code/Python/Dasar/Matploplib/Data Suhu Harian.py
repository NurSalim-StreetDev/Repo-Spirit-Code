import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'Suhu': [30, 32, 33, 31, 29, 28, 30]
}

# Buat DataFrame
df = pd.DataFrame(data)

# Buat Grafik Garis
plt.plot(df['Hari'], df['Suhu'], marker='o', linestyle='-', color='b')

# Tambahkan Judul dan Label Sumbu
plt.title('Perubahan Suhu Harian Selama Seminggu')
plt.xlabel('Hari')
plt.ylabel('Suhu (°C)')

# Tampilkan Grafik
plt.show()
