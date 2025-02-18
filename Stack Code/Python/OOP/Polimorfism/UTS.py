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

Shapes = [Lingkaran(), Segitiga(), Segiempat(), Panah(), Garis()]
for shape in Shapes:
    print(shape.Gambar())
