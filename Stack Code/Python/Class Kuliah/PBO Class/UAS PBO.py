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
    tanggal_masuk = int(input("Masukkan tanggal : "))

    if jenis == "baru":
        jurusan = input("Jurusan: ")
        print("Data mahasiswa berhasil ditambahkan.")
        # data_mahasiswa.append(mahasiswa)
        # data_mahasiswa = []

        return MahasiswaBaru(nama, nim, jurusan)
    elif jenis == "lama":
        semester = int(input("Semester: "))
        return MahasiswaLama(nama, nim, semester)
    else:
        print("Pilihan yang Anda masukkan salah")
        return None


# List untuk menyimpan data mahasiswa

try:
    while True:
        print("\nMenu:")
        print("1. Input mahasiswa")
        print("2. Tampilkan data mahasiswa")
        print("3. Keluar")

        pilihan =input("Silahkan tentukan Pilihan: ")

        if pilihan == "1":
            Mahasiswa = input_mahasiswa()
            # print("Data mahasiswa berhasil ditambahkan.")
            # data_mahasiswa.append(mahasiswa)
            # data_mahasiswa = []

        elif pilihan == "2":
            print("\nSilahkan Masukkan Data Mahasiswa Lama:")
            mahasiswa = input_mahasiswa()
            for mahasiswa in data_mahasiswa:
                print(mahasiswa.info())
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")            

except:
    print("Terjadi kesalahan dalam program.")

finally:
    print("\nTerima kasih telah menggunakan")