'''
Mari kita lakukan manipulasi pada str
'''

Nama = 'Nur Salim'
a = Nama.count('a')
print (a)

# selamjutnya adalah Index
print ('index huruf 0', Nama[0])
print ('index huruf 0,2,4,6', Nama [0:8:2])
# penggunaan in
b = 'lim'
status = b in Nama
print (b, 'ada dalam', Nama, 'status', status)

# Min and Max
print ('paling Besar',  max(Nama))
print ('paling kecil', min(Nama))

#Entahlah
c = ord(' ')
print ('code untuk spasi', str(Nama))
data = 12
print ('char untuk c 12', chr(data))

#singel quote
data = 'salim'
print ('ini adalah singel quote', data)

# membuat ' menjadi string
data = 'jum\'at'
print (data)

#Back slash
data = 'C:\\salim\\halaman'
print (data)

#\t
data = 'Nur \t Salim'
print (data)

#New line  \n
print (' baris satu, \n brias 2')

# rows
print (r'dhwaikbrcw8rhwir34bo9nrtcghm-qa\\\\n')

#Multi line print
print ('''
ayo jangan alri sendiri
mari sama makan 
pisdang
''')

