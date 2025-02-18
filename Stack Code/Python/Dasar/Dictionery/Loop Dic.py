''' Kita melakkan operasi Loop di Dictionery'''
Kawan = {
    'key':'suka',
    'anomali':'makan',
    'Lim':'Malam',
    'pisang':'Coklat',
 }

for k in Kawan: 
    print(k) #ini hanya akan menghasilkan key

k = Kawan.keys()
print(f'ini bakalan keys nya dict {k}') 

for key in Kawan.keys():
    print(f'print menggunakan get(key) {Kawan.get(key)}')

for Value in Kawan.values():
    print(Value)

Items = Kawan.items() # ini bentuk item jadi jamak
print(Items)

for item in Kawan.items():
    print(f'ini loop nya{item}')

for key,value in Kawan.items():
    print(f'loop jamak dengan key {key} dan Value {value}')