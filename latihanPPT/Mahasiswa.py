from Dosen import *
from Person import *

class Mahasiswa(Person):
    # Properti tambahan untuk Mahasiswa
    prodi = ""
    semester = 0

    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester

    def cetak(self):
        super().cetak()
        print("Prodi\t\t:", self.prodi,
              "\nSemester\t:", self.semester,
              "\n-------------------------------")

# Contoh penggunaan
# Pastikan kelas Person sudah terdefinisi sebelumnya
# mahasiswa1 = Mahasiswa("Budi", "Laki-laki", 20, "Teknik Informatika", 3)
# mahasiswa1.cetak()
m1 = Mahasiswa('Siti Aminah', 'Wanita', 20, 'SI', 3)
m2 = Mahasiswa('Budi Santoso', 'Pria', 23, 'TI', 5)

m1.cetak()
m2.cetak()