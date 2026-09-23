class Tenda:
    TotalTenda = 0
    BiayaPemasangan = 250000
    
    def __init__(self, IDTenda, Jenis, Harga, Stok):
        self.IDTenda = IDTenda
        self.Jenis = Jenis
        self.HargaTenda = Harga
        self.__StokTenda = Stok
        
        Tenda.TotalTenda += 1
        
    @property
    def Stok(self):
        return self.__StokTenda 
    
    @Stok.setter
    def Stok(self, NilaiBaru):
        if not isinstance(NilaiBaru, int) or NilaiBaru < 0:
            print(f"\nStok Untuk {self.Jenis} Yang Diinput Tidak Valid!!!")
        else:
            self.__StokTenda = NilaiBaru
            
    def TampilkanTenda(self):
        print(f"ID Tenda: {self.IDTenda}\nJenis Tenda: {self.Jenis}\nHarga Tenda: {self.HargaTenda}\nStok: {self.__StokTenda}")
        
    @classmethod
    def UbahBiayaPasang(cls, BiayaBaru):
        if not isinstance(BiayaBaru, int) or BiayaBaru < 0:
            print(f"\nHarga Baru Yang Dimasukan Tidak Valid!!!")
        else:
            cls.BiayaPemasangan = BiayaBaru
        
    @staticmethod
    def ValidasiIDTenda(IDTenda):
        return IDTenda.startswith("T-")
    

class KursiTamu:
    TotalKursi = 0
    BiayaTata = 150000
    
    def __init__(self, IDKursi, Merk, Harga, Stok):
        self.IDKursi = IDKursi
        self.Merk = Merk
        self.HargaKursi = Harga
        self.__StokKursi = Stok 
        
        KursiTamu.TotalKursi += 1
        
    @property
    def StokKursi(self):
        return self.__StokKursi
    
    @StokKursi.setter
    def StokKursi(self, NilaiBaru):
        if not isinstance(NilaiBaru, int) or NilaiBaru < 0:
            print(f"\nStok Kursi Untuk {self.Merk} Yang Diinput Valid!!!")
        else:
            self.__StokKursi = NilaiBaru
            print(f"Stok Kursi {self.Merk} Berhasil Diperbarui Dengan Jumlah {NilaiBaru}")
            
    def TampilkanKursi(self):
        print(f"ID Tenda: {self.IDKursi}\nJenis Tenda: {self.Merk}\nHarga Tenda: {self.HargaKursi}\nStok: {self.__StokKursi}")
            
    @classmethod
    def UbahBiayaTata(cls, BiayaBaru):
        if not isinstance(BiayaBaru, int) or BiayaBaru < 0:
            print(f"\nHarga Baru Yang Dimasukan Tidak Valid!!!")
        else:
            cls.BiayaTata = BiayaBaru
        
    @staticmethod
    def ValidasiIDKursi(IDKursi):
        return IDKursi.startswith("K-")
        

class Penyewa:
    TotalPenyewa = 0
    DendaTelat = 100000
    BatasSewa = 7
    
    def __init__(self, Nama, Kontak, Saldo):
        self.Nama = Nama
        self.Kontak = Kontak
        self.__Saldo = Saldo
        
        Penyewa.TotalPenyewa += 1
        
    @property
    def Saldo(self):
        return self.__Saldo
    
    @Saldo.setter
    def Saldo(self, SaldoBaru):
        if not isinstance(SaldoBaru, int) or SaldoBaru < 0:
            print(f"Saldo Tidak Valid!!!")
        else:
            self.__Saldo = SaldoBaru

    def SewaTenda(self, Tenda, Jumlah):
        print(f"Nama: {self.Nama}, Menyewa {Jumlah} Tenda {Tenda.Jenis}")
        if Tenda.Stok >= Jumlah:
            TotalBiaya = (Tenda.HargaTenda * Jumlah) + Tenda.BiayaPemasangan
            if self.__Saldo >= TotalBiaya:
                self.__Saldo -= TotalBiaya
                Tenda.Stok -= Jumlah
                print(f"Berhasil Menyewa Tenda!!! Sisa Saldo Anda({self.Nama}): Rp{self.__Saldo}")
            else:
                print(f"Saldo Tidak Cukup!!! (Butuh Rp{TotalBiaya})")
        else:
            print("Stok Tenda Tidak Cukup!!!")
            
    @classmethod
    def Peraturan(cls):
        print(f"Maksimal Sewa barang {cls.BatasSewa} Hari. Denda Rp{cls.DendaTelat}/Hari :)")

    @staticmethod
    def ValidasiKontak(NoKontak):
        Nomor = str(NoKontak)
        return Nomor.startswith("08")
    
"""Uji Coba"""
print("=== 1. INISIALISASI OBJEK (Minimal 2 per class) ===")
Tenda1 = Tenda("T-01", "VIP Tertutup", 150000, 5)
Tenda2 = Tenda("T-02", "Standar Terbuka", 80000, 2)
print(Tenda1.__dict__)
print(Tenda2.__dict__)
print("\n")

Kursi1 = KursiTamu("K-01", "Plastik + Cover", 5000, 100)
Kursi2 = KursiTamu("K-02", "Plastik", 2000, 200)
print(Kursi1.__dict__)
print(Kursi2.__dict__)
print("\n")

Penyewa1 = Penyewa("Budi", "081234", 1000000)
Penyewa2 = Penyewa("Siti", "089876", 100000)
print(Penyewa1.__dict__)
print(Penyewa2.__dict__)

print("\n=== 2. UJI INSTANCE METHOD ===")
Tenda1.TampilkanTenda()
Kursi1.TampilkanKursi()

print("\n=== 3. UJI CLASS METHOD & STATIC METHOD ===")
Tenda.UbahBiayaPasang(75000)
print(f"Format ID TND-01 Valid? {Tenda.ValidasiIDTenda(Tenda1.IDTenda)}")
print(f"Format ID KRS-01 Valid? {KursiTamu.ValidasiIDKursi(Kursi1.IDKursi)}")

print("\n=== 4. UJI SETTER & VALIDASI (Property) ===")
Kursi1.StokKursi = -10  
Kursi1.StokKursi = 90   
Penyewa1.Saldo = -50000 

print("\n=== 5. UJI INTERAKSI ANTAR OBJEK ===")
Penyewa1.SewaTenda(Tenda1, 2) 
Penyewa2.SewaTenda(Tenda2, 1) 
       