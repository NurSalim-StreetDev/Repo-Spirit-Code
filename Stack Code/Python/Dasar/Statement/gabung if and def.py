print ('Lupa Password'.center(40,'='))
#contoh
def password ():
    password_1 = 210301
    password_2 = 210302
    NIM_1 = 220180124
    NIM_2 = 220180125
    NIM =int(input('Masukan NIM anda\t:'))
    if NIM == NIM_1:
        print (f'Password anda adalah {password_1}')
    elif NIM == NIM_2:
        print (f'Password anda adalah {password_2}')
    elif NIM != NIM_1 or NIM_2 :
        print ('Maaf anda siapa ya!')

password ()
