class BarangSewa:
    def __init__(self, IDBarang, NamaBarang, HargaSewa, Stok):
        self.IDBarang = IDBarang
        self.NamaBarang = NamaBarang
        self._HargaSewa = HargaSewa 
        self.__Stok = Stok

    @property
    def Stok(self):
        return self.__Stok
        
    def KurangiStok(self, jumlah):
        if self.__Stok >= jumlah:
            self.__Stok -= jumlah
            return True
        return False

    def TampilkanInfo(self):
        print(f"ID: {self.IDBarang} | Nama: {self.NamaBarang} | Harga Sewa: Rp{self._HargaSewa} | Stok: {self.__Stok}")
        
        
class Tenda(BarangSewa):
    TotalTenda = 0
    BiayaPemasangan = 250000
    
    def __init__(self, IDTenda, Jenis, Harga, Stok, Kapasitas):
        super().__init__(IDTenda, Jenis, Harga, Stok)
        self.Kapasitas = Kapasitas
        
        Tenda.TotalTenda += 1
            
    def TampilkanInfo(self):
        super().TampilkanInfo()
        print(f"Kapasitas: {self.Kapasitas} Orang")
        print(f"Biaya Pemasangan: Rp{Tenda.BiayaPemasangan}")
        
        EstimasiBiaya = self._HargaSewa + Tenda.BiayaPemasangan
        print(f"Estimasi Biaya 1 Unit + Pasang Tenda: Rp{EstimasiBiaya}")
        
    @classmethod
    def UbahBiayaPasang(cls, BiayaBaru):
        if not isinstance(BiayaBaru, int) or BiayaBaru < 0:
            print(f"\nHarga Baru Yang Dimasukan Tidak Valid!!!")
        else:
            cls.BiayaPemasangan = BiayaBaru
        
    @staticmethod
    def ValidasiIDTenda(IDTenda):
        return IDTenda.startswith("T-")
    

class KursiTamu(BarangSewa):
    TotalKursi = 0
    BiayaTata = 150000
    
    def __init__(self, IDKursi, Merk, Harga, Stok, BahanKursi):
        super().__init__(IDKursi, Merk, Harga, Stok)
        self.BahanKursi = BahanKursi
        
        KursiTamu.TotalKursi += 1
            
    def TampilkanInfo(self):
        super().TampilkanInfo()
        print(f"Bahan Kursi: {self.BahanKursi}")
        print(f"Biaya Pemasangan: Rp{KursiTamu.BiayaTata}")
        
        EstimasiBiaya = self._HargaSewa + KursiTamu.BiayaTata
        print(f"Estimasi Biaya 1 Unit + Penataan Kursi: Rp{EstimasiBiaya}")
            
    @classmethod
    def UbahBiayaTata(cls, BiayaBaru):
        if not isinstance(BiayaBaru, int) or BiayaBaru < 0:
            print(f"\nHarga Baru Yang Dimasukan Tidak Valid!!!")
        else:
            cls.BiayaTata = BiayaBaru
        
    @staticmethod
    def ValidasiIDKursi(IDKursi):
        return IDKursi.startswith("K-")

class Admin:
    def __init__(self, NamaAdmin):
        self.NamaAdmin = NamaAdmin
    
    def Melayani(self, Penyewa):
        print(f"Admin {self.NamaAdmin} Menlayani Penyewa: {Penyewa.Nama}")
        Penyewa.AdminPelayan = self
        
        
class Penyewa:
    TotalPenyewa = 0
    DendaTelat = 100000
    BatasSewa = 7
    
    def __init__(self, Nama, Kontak, Saldo):
        self.Nama = Nama
        self.Kontak = Kontak
        self.__Saldo = Saldo
        
        Penyewa.TotalPenyewa += 1
        
        self.AdminPelayan = None
        self.BarangSewa = []
        self.Kartu = KartuMember(self.Nama)
        
    @property
    def Saldo(self):
        return self.__Saldo
    
    @Saldo.setter
    def Saldo(self, SaldoBaru):
        if not isinstance(SaldoBaru, int) or SaldoBaru < 0:
            print(f"Saldo Tidak Valid!!!")
        else:
            self.__Saldo = SaldoBaru

    def CekAdmin(self):
        if self.AdminPelayan != None:
            print(f"{self.Nama} Dilayani Oleh Admin {self.AdminPelayan.NamaAdmin}")
            
    def SewaTenda(self, Tenda, Jumlah):
        print(f"Nama: {self.Nama}, Menyewa {Jumlah} Tenda {Tenda.NamaBarang}")
        if Tenda.Stok >= Jumlah:
            TotalBiaya = (Tenda._HargaSewa * Jumlah) + Tenda.BiayaPemasangan
            if self.__Saldo >= TotalBiaya:
                self.__Saldo -= TotalBiaya
                
                Tenda.KurangiStok(Jumlah) 
                print(f"Berhasil Menyewa Tenda!!! Sisa Saldo Anda({self.Nama}): Rp{self.__Saldo}")
                
                self.BarangSewa.append({"Item": Tenda, "Jumlah": Jumlah})
            else:
                print(f"Saldo Tidak Cukup!!! (Butuh Rp{TotalBiaya})")
        else:
            print("Stok Tenda Tidak Cukup!!!")
    
    def CekBarangSewa(self):
        print(f"Barang Yang Disewa Oleh {self.Nama}:") 
        No = 0
        for i in self.BarangSewa:
            No += 1
            print(f"{No}. {i["Jumlah"]} {i["Item"].NamaBarang}")
            
    def CekKartuMember(self):
        self.Kartu.InfoKartu()
            
    @classmethod
    def Peraturan(cls):
        print(f"Maksimal Sewa barang {cls.BatasSewa} Hari. Denda Rp{cls.DendaTelat}/Hari :)")

    @staticmethod
    def ValidasiKontak(NoKontak):
        Nomor = str(NoKontak)
        return Nomor.startswith("08")


class KartuMember:
    def __init__(self, NamaMember):
        self.NamaMember = NamaMember
        
        self.Poin = 100
        
    def InfoKartu(self):
        print(f"Kartu Member Milik {self.NamaMember}, Memiliki Poin Member Sebesar: {self.Poin}")
    
    
    
"""Uji Coba"""
Admin1 = Admin("Om Bram")

Tenda1 = Tenda("T-01", "Tenda VIP Tertutup", 150000, 5, 300)
Tenda2 = Tenda("T-02", "Tenda Standar Terbuka", 80000, 2, 100)

Kursi1 = KursiTamu("K-01", "Kursi + Cover", 5000, 100, "Rangka Stainless")
Kursi2 = KursiTamu("K-02", "Kursi Biasa", 2000, 200, "Rangka Plastik")

Penyewa1 = Penyewa("Budi", "081234", 1000000)
Penyewa2 = Penyewa("Siti", "089876", 100000)

print("=== 1. PEMBUKTIAN ASOSIASI ===")
Admin1.Melayani(Penyewa1)
Penyewa1.CekAdmin()
print("\n")

print("=== 2. PEMBUKTIAN AGREGASI & KOMPOSISI ===")
Penyewa1.SewaTenda(Tenda1, 2)
Penyewa1.CekBarangSewa()
Penyewa1.CekKartuMember()
print("\n")

print("=== 3. PEMBUKTIAN PEWARISAN & OVERRIDING ===")
Tenda1.TampilkanInfo()
print(f"Sisa Stok Tenda Di Gudang: {Tenda1.Stok}\n")

Kursi1.TampilkanInfo()
print(f"Sisa Stok Kursi Di Gudang: {Kursi1.Stok}\n")
