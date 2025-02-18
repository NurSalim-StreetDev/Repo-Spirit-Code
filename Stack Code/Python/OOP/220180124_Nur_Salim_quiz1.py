class Lim:

    def methodLim1(self):
        print ('Ini adalah Method kelas Induk, Lim fungsi 1')

    def methodLim2(self):
        print ('Ini adalah Method kelas Induk, Lim fungsi 2')

    def methodLim3(self):
        print ('Ini adalah Method kelas Induk, Lim fungsi 3')


class NIM_220180124(Lim):

    def methodNIM1(self):
        print ('Ini adalah Method kelas Anak 1, NIM fungsi 1')
    
    def methodNIM2(self):
        print ('Ini adalah Method kelas Anak 1, NIM fungsi 2')
    
    def methodNIM3(self):
        print ('Ini adalah Method kelas Anak 1, NIM fungsi 3')


class Kelas(NIM_220180124):

    def methodKelas(self):
        print ('Ini adalah Method kelas Anak 2, Kelas fungsi 1')
    
    def methodKelas2(self):
        print ('Ini adalah Method kelas Anak 2, Kelas fungsi 2')

    def methodKelas3(self):
        print ('Ini adalah Method kelas Anak 2, Kelas fungsi 3')


class Angkatan(NIM_220180124):

    def methodAngkatan1(self):
        print ('Ini adalah Method kelas Anak 3, Angkatan fungsi 1')

    def methodAngkatan2(self):
        print ('Ini adalah Method kelas Anak 3, Angkatan fungsi 2')

    def methodAngkatan3(self):
        print ('Ini adalah Method kelas Anak 3, Angkatan fungsi 3')


Object1 = NIM_220180124()
Object1.methodLim1()

Object2 = NIM_220180124()
Object2.methodLim2()

Object3 = Kelas()
Object3.methodNIM1()

Object4 = Kelas()
Object4.methodNIM2()

Object5 = Angkatan()
Object5.methodNIM3()






            
        

        
