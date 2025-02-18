
# # a = 'salim'
# # while i in a:
# #     print (a)
# j=int(input('Masukan nilai:'))
# a = 5*j
# b = 10*j
# c = a + b
# print (c)

# # kita akan menggunakan penerapan numpy as np
import numpy as np

a = [1,2,3,4,5]
b = [6,7,8,9,0]
np_a = np.array (a)
np_b = np.array (b)

np_2d = np.array ([a,b])

print ('hasil 1 ', np_a + np_b)
print (np_2d)
print ('hasil 3 ', np_2d.shape)
print ('hasil 4 ', np_2d [0])
print ('hasil 5 ', np_2d [0][2])
print ('hasil 6 ', np_2d [1,3])
print ('hasil 7 ', np_2d [:, 1:4])
print ('hasil 8 ', np_2d [1:, 1:4])

#numpy: basic Statistic!
import numpy as np

np_kota = np.array ([[12.5, 10.3], [23.44, 21.97], [25.65, 14.87], [15.45, 13.69]])

print (np_kota)
print (np.mean(np_kota))
print (np.mean(np_kota[:,0]))
print (np.mean(np_kota[:,1]))
print (np.std(np_kota [:,0]))
print (np.corrcoef(np_kota [:,0], np_kota [:,0]))