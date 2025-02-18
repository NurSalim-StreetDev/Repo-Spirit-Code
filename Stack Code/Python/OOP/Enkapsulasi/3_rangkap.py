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
