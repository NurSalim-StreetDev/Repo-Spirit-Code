class Hewan: 
    def __init__(self, name):   
        self.name = name         
    def suara(self):              
        raise NotImplementedError("Subclass must implement abstract method")

class Kucing(Hewan):
    def suara(self):
        return 'Meow!'

class Srigala(Hewan):
    def suara(self):
        return 'Wuarr! Wuarr!'

animals = [Kucing('Ken'),
           Kucing('Tara'),
           Srigala('wolfin')]

for Hewan in animals:
    print (Hewan.name + ': ' + Hewan.suara())