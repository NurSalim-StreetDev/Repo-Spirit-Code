print('Testing ingatan 1, tgl 7 maret 2023'.center(40,'='))
'''pertanyaannya gini, saya ngmabil input yang di batasi dengan str saja, jika tidak maka akan 
else '''
def pengenalan_type_data():
    masukan = str(input('Masukan data yang anda ingin cek!:')) #gimana caranya inputnya hanya str
    a = 'AAA'
    b = 'Item Di Temukan'
    if masukan == a: 
        print (b)
    else:
        print ('ERROR')
pengenalan_type_data()