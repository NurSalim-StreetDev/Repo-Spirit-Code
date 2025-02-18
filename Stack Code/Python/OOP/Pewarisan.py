class ibu:
    def methodIbu(self):
        print ('ini adalah Method Ibu')

class anak (ibu):
    def methodAnak(self):
        print ('ini adalah Method Anak')

p = ibu()
p.methodIbu()

b = anak()
b.methodAnak()
b.methodIbu()