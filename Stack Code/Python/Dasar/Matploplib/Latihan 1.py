import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Penjualan': [1200, 1400, 1450, 1600, 1900, 2000, 2000, 2200, 2500, 3000, 5000, 5000]
}

df = pd.DataFrame(data)

plt.plot(df['Bulan'], df['Penjualan'], marker='o', linestyle='-', color='b')

plt.title('Perubahan Penjualan Bulanan Baju')
plt.xlabel('Bulan')
plt.ylabel('Penjualan (PCS)')

# Tampilkan Grafik
plt.show()
