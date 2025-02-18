def Tipe_data():

    a = input('Masukan data yang ingin anda tes\t:')
    # b = int(input('Masukan data yang ingin anda tes\t:'))
    # c = float(input('Masukan data yang ingin anda tes\t:'))
    # d = bool(input('Masukan data yang ingin anda tes\t:'))
    

    Data_1 = str
    Data_2 = int
    Data_3 = float
    Data_4 = bool

    if str == Data_1:
        print(f'tipe data dari yang anda masukan adalah {Data_1}')
    
    elif Data_2 == int:
        print(f'tipe data dari yang anda masukan adalah {Data_2}')

    elif float == Data_3:
        print(f'tipe data dari yang anda masukan adalah {Data_3}')
    
    elif bool == Data_4:
        print(f'tipe data dari yang anda masukan adalah {Data_4}')
    
    else:
        print('ERROR')

        
        
        

Tipe_data()