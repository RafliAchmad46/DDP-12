from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.racun = racun
        
    def cetak_ular(self):
        super().cetak()
        print("Corak \t\t\t\t: ", self.corak,
              "\nRacun \t\t\t\t: ", self.racun)

# Membuat objek Ular
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Jepara", "Tidak Beracun")
anaconda.cetak_ular()
print("")
sanca = Ular("Sanca", "Tikus", "Rawa", "Bertelur", "Kembang", "Tidak Beracun")
sanca.cetak_ular()
print("")
kobra = Ular("Kobra", "Mamalia kecil", "Hutan", "Bertelur", "hitam dan bervariasi", "Beracun")
kobra.cetak_ular()
