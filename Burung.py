from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_paruh, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_paruh = jenis_paruh
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak()
        print("Jenis Paruh \t\t\t: ", self.jenis_paruh,
              "\nBunyi \t\t\t\t: ", self.bunyi)

# Membuat objek Ular
kakatua= Burung("Kakatua", "Biji-bijian", "Hutan", "Bertelur", "Paruh Bengkok", "keras dan melengking")
kakatua.cetak_burung()
print(" ")
pelikan = Burung("Pelikan", "Ikan", "Sungai", "Bertelur", "Paruh Berkantong", "gerutuan rendah dan singkat")
pelikan.cetak_burung()
print("")
pipit = Burung("Pipit", "Biji-bijian", "Padang rumput", "Bertelur", "Paruh pendek", "serangkaian nada kicauan")
pipit.cetak_burung()