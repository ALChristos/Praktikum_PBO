"""Class Relationship"""

"""Asosiasi"""
# class Nasabah:
#     def __init__(self, Nama, NoRek):
#         self.nama = Nama
#         self.rek = NoRek
        
#     def TarikTunai(self, atm, Jumlah):
#         atm.saldo -= Jumlah
        
# class MesinATM:
#     def __init__(self, IDATM, Lokasi, SaldoKas):
#         self.id = IDATM
#         self.lokasi = Lokasi
#         self.saldo = SaldoKas
    
# dapa = Nasabah("Dapa", "1234")
# ATMPusat = MesinATM("Pusat", "Samarinda", 50000000)

# dapa.TarikTunai(ATMPusat, 1000)

# print(f"{ATMPusat.saldo}")

"""Agregasi"""
# class Bank:
#     def __init__(self, NamaBank, Kode):
#         self.NamaBank = NamaBank
#         self.kode = Kode
#         self.karyawan = []
        
#     def TambahKaryawan(self, Karyawan):
#         self.karyawan.append(Karyawan)
        
# class Karyawan:
#     def __init__(self, Nama, NIP, Posisi):
#         self.nama = Nama
#         self.NIP = NIP
#         self.posisi = Posisi
        
# bank = Bank("Mandiri", "0001")
# udin = Karyawan("Udin", 123, "Manager")

# bank.TambahKaryawan(udin)
# print(bank.karyawan[0].nama)
# print(bank.karyawan[0].NIP)
# print(bank.karyawan[0].posisi)
        
        
"""Komposisi"""  
class Bank:
    def __init__(self, NamaBank, Kode):
        self.NamaBank = NamaBank
        self.kode = Kode
        self.karyawan = []
        
    def TambahKaryawan(self, Nama, Nip, Posisi):
        KaryawanBaru = Karyawan(Nama, Nip, Posisi)
        self.karyawan.append(KaryawanBaru)
        
class Karyawan:
    def __init__(self, Nama, NIP, Posisi):
        self.nama = Nama
        self.NIP = NIP
        self.posisi = Posisi
        
# 1. Buat dulu objek bank-nya
bank = Bank("Mandiri", "0001")
# 2. Panggil method dari objek tersebut
bank.TambahKaryawan("Udin", "123", "Manager")
# 3. Cetak dari objek tersebut
print(bank.karyawan[0].nama) 
