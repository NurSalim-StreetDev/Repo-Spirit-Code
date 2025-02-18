# anda tahu list array di akses dengan menggunakan index seperti
list = ['ucup','dadang','salim']
print(list[2])

#apa beda dictionery dengan list
''' Perbedaan ada pada indentifiernya dimana list menggunakan index yang menggurutkan dari 0
sedangkan dictioneri menggunakan -> key secara langsung di data dan bisa menggunakan cutom kita sendiri'''
#begini Dic
Dictio = {
    'L':'Lim', # formatnya 'key':'Value'
    'A':'Abang',
    'B':'Babang',
    'Number':100, #juga bisa membuat string
    'list':list, #juga bisa memasukan list ke dalmnya
}
#sehingga ketika kita ingin mengeprint key tertentu pada dic tinggal panggl keynya
print(Dictio['L'])
print(Dictio['Number'])
print(Dictio['list'])
'''Dictionery berguna untuk membuat sebuah data yang punya struktur'''