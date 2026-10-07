"""Inheritance"""
class Animal:
    def __init__(self, Nama, Umur):
        self.nama = Nama
        self.umur = Umur

class Mamalia(Animal):
    def __init__(self, Nama, Umur, WarnaBulu):
        super().__init__(Nama, Umur)
        self.warna = WarnaBulu
        
    def makan(self):
        print(f"{self.nama} sedang makan")

class Reptiel(Animal):
    def __init__(self, Nama, Umur, Berbisa):
        self.berbisa= Berbisa
        
kucing = Mamalia("Oren", 2, "Hitam")
ular = Reptiel("Cobra", 2, True)

print(kucing.nama)
kucing.makan()
    
