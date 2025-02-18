#macam ragam dictionery operation
Data_Dic ={
    'L':'Lim',
    'A':'Salim',
    'B':'Buya',
}
#pertrama panjang Dictionery
LENDICT = len(Data_Dic) # ingat kesepakatan programmer konstant name di py dengan huruf besar semua
print(f'Panjang Data Dic: {LENDICT}')

#Mengecek Exist
CEK = 'L'
CEKKY = CEK in Data_Dic
print(f'Apakah {CEK} ada dalam data dic : {CEKKY}')

#selanjutnya mengambil nilai Valule dengan menggunakan Get
print(Data_Dic.get('L'))
print(Data_Dic.get('kiss')) # mengembalikan nilai NONE sehingga no Erroe
print(Data_Dic.get('kk','Data Tidak ADA')) # penggunaaan Messege

#Selanjutnya Update Doc nya
Data_Dic['L'] = 'Lim and Lim'
print(Data_Dic)

