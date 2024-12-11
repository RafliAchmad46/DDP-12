from Mahasiswa import *
from Person import *  # Pastikan kelas Dosen tidak didefinisikan ulang di sini

class Dosen(Person):
    # Properti tambahan untuk Dosen
    gelar = ""
    jabatan = ""
    gaji = 0

    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan

    def setGaji(self, uang):
        self.gaji = uang  # Mengatur gaji baru

    def cetak(self):
        super().cetak()
        print("Gelar\t\t:", self.gelar,
              "\nJabatan\t\t:", self.jabatan,
              "\nGaji\t\t: Rp.", self.gaji,
              "\n-------------------------------")

# Membuat objek Dosen
d1 = Dosen('Sirojul Munir', 'Pria', 43, 'S.Si, M.Kom', 'LPPM')
d2 = Dosen('Henry Saptono', 'Pria', 44, 'S.Si, M.Kom', 'LTSI')

# Menggunakan fungsi yang ada di kelas
d1.setGaji(12000000)
d2.setGaji(10000000)

# Mencetak informasi dosen
d1.cetak()
d2.cetak()