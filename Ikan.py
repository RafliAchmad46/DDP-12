from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bentuk_tubuh, corak):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bentuk_tubuh = bentuk_tubuh
        self.corak = corak
    def cetak_ikan(self):
        super().cetak()
        print("Bentuk tubuh  \t\t\t: ", self.bentuk_tubuh,
              "\nCorak \t\t\t\t: ", self.corak)

# Membuat objek Ular
koi= Ikan("Koi", "Cacing Sutra", "Air tawar", "Bertelur", "Memanjang, bulat lonjong, dan sedikit pipih ke samping", "Kombinasi merah atau orange")
koi.cetak_ikan()
print(" ")
discus = Ikan("Discus", "Cacing sutra", "Air tawar", "Bertelur", "Berbentuk pipih", "Corak indah seperti pola Batik Mega Mendung.")
discus.cetak_ikan()
print("")
cupang = Ikan("Cupang", "Cacing sutra", "Air tawar", "Bertelur", "Bentuk badan memanjang dan agak gepeng", "Kombinasi warna-warna cerah yang beragam")
cupang.cetak_ikan()