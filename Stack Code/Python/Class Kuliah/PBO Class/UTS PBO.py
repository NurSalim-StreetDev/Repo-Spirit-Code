'''Contoh Polimorfism'''
print('Hasil Polimorfism')
class Shape:
    def Gambar(self):
        pass

class Lingkaran(Shape):
    def Gambar(self):
        return "Drawing sebuah Lingkaran"

class Segitiga(Shape):
    def Gambar(self):
        return "Drawing sebuah Segitiga"

class Segiempat(Shape):
    def Gambar(self):
        return "Drawing sebuah Segiempat"

class Panah(Shape):
    def Gambar (self):
        return "Drawing sebuah Panah"

class Garis (Shape):
    def Gambar(self):
        return "Drawing sebuah garis"

shapes = [Lingkaran(), Segitiga(), Segiempat(), Panah(), Garis()]
for shape in shapes:
    print(shape.Gambar())


class Contoh:
    def __init__(self):
        self.publik = "Ini adalah atribut publik"
        self._terlindungi = "Ini adalah atribut terlindungi"
        self.__pribadi = "Ini adalah atribut pribadi"

    def metode_publik(self):
        print("Ini adalah metode publik")

    def _metode_terlindungi(self):
        print("Ini adalah metode terlindungi")

    def __metode_pribadi(self):
        print("Ini adalah metode pribadi")


objek = Contoh()

print(objek.publik)
print(objek._terlindungi)
# print(objek.__pribadi) # Ini akan menimbulkan AttributeError

objek.metode_publik()
objek._metode_terlindungi()
# objek.__metode_pribadi()  # Ini akan menimbulkan AttributeError
