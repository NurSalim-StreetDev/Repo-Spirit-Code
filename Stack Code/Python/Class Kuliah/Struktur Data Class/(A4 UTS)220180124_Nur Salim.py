
'''Tugas Ulangan Akhir Tengah Semester '''
print('\nNama : Nur Salim')
print('Kelas: A4')
print('NIM  : 220180124')
print('Jawaban UTS MK Struktur Data'.center(40,'-'))
print( )
Right       = 0
Left        = 6
Up          = 1
Tulisan     = ''
Tingkatan   = 1
Color_Right = '\033[91m'
Color_Up    = '\033[92m'

while Up >= 1 and Up <= 6:
    for i in range(Right):
        Tulisan += Color_Right + '*'
    Tulisan += ' '
    Right += Tingkatan

    for i in range(Left):
        Tulisan += '\033[0m* '
    Left -= Tingkatan

    for i in range(Up):
        Tulisan += Color_Up + '*'
    Tulisan += '\n'
    Up += Tingkatan

    if Left == 0:
        Tingkatan = -1
        Left += 1
        Right -= 1
        Up -= 1
        Color_Right = '\033[94m'
        Color_Up = '\033[93m'

print(Tulisan)
print('Program Selesai'.center(40,'-'))
print( )