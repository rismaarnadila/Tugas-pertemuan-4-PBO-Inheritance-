class motor: 
    def __init__(self, warna, tahun, merk):
        self.warna = warna
        self.tahun = tahun
        self.merk = merk

    def printname(self):
        print(self.warna)
        print(self.tahun)
        print(self.merk)

class matic(motor):
    def __init__(self, warna, tahun, merk): 
        motor.__init__(self, warna, tahun, merk) 
        self.produk = "Vario"
    
    def tampilanmatic (self):
        print("Jenis Matic : ", self.produk)
        print("Merk        :", self.merk)
        print("Warna       :", self.warna)
        print("Tahun       :", self.tahun)

class manual(motor):
    def __init__(self, warna, tahun, merk): 
        motor. __init__(self, warna, tahun, merk) 
        self.produk = "Supra X"
    
    def tampilanmanual(self): 
        print("Jenis Manual : ", self.produk)
        print("Merk         :", self.merk)
        print("Warna        :", self.warna)
        print("Tahun        :", self.tahun)

x = matic ("Putih", 2018, "Yamaha")
y = manual("Biru", 2010, "Honda")

x.printname()
print("***************")
y.printname()