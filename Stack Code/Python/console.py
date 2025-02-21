import matplotlib.pyplot as plt

# Data dengan beberapa outliers
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 50]

plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Box Plot with Outliers')
plt.xlabel('Values') 

plt.show()
