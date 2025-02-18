class Mahasiswa:
    def __init__(self, nama, nim):
        self._nama = nama
        self._nim = nim

    def info(self):
        pass


class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, nim, jurusan):
        super().__init__(nama, nim)
        self._jurusan = jurusan

    def info(self):
        return f"Mahasiswa Baru - Nama: {self._nama}, NIM: {self._nim}, Jurusan: {self._jurusan}"


class MahasiswaLama(Mahasiswa):
    def __init__(self, nama, nim, semester):
        super().__init__(nama, nim)
        self._semester = semester

    def info(self):
        return f"Mahasiswa Lama - Nama: {self._nama}, NIM: {self._nim}, Semester: {self._semester}"


def input_mahasiswa():
    jenis = input("Jenis mahasiswa (baru/lama): ")
    nama = input("Nama: ")
    nim = input("NIM: ")
    tanggal = int(input("masukkan tanggal : "))

    if jenis.lower() == "baru":
        jurusan = input("Jurusan: ")
        return MahasiswaBaru(nama, nim, jurusan)
    elif jenis.lower() == "lama":
        semester = int(input("Semester: "))
        return MahasiswaLama(nama, nim, semester)
    else:
        print("Jenis mahasiswa tidak valid.")
        return None


# List untuk menyimpan data mahasiswa
data_mahasiswa = []

try:
    while True:
        print("\nMenu:")
        print("1. Input mahasiswa")
        print("2. Tampilkan data mahasiswa")
        print("3. Keluar")

        pilihan = input("Pilihan: ")

        if pilihan == "1":
            mahasiswa = input_mahasiswa()
            if mahasiswa:
                data_mahasiswa.append(mahasiswa)
                print("Data mahasiswa berhasil ditambahkan.")
        elif pilihan == "2":
            print("\nData Mahasiswa:")
            for mahasiswa in data_mahasiswa:
                print(mahasiswa.info()) 
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

except:
    print("Terjadi kesalahan dalam program.")

finally:
    print("\nTerima kasih telah menggunakan program ini.")