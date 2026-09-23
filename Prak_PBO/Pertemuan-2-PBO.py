"""Enkapsulasi"""
# # class RekeningBankTanpaEncapsulation:
# #     def __init__(self, pemilik, saldo):
# #         self.pemilik = pemilik
# #         self.__saldo = saldo

# # rekening = RekeningBankTanpaEncapsulation("Budi", 100000)
# # rekening.saldo = -500000 # tidak ada yang mencegah ini
# # print(rekening.saldo) # -500000, data jadi tidak valid

"""Public"""
# class Nasabah:
#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo
        
# # nama = input("Masukan Nama Anda: ")
# # saldo = input("Masukan Saldo Anda: ")

# user = Nasabah("Van", 100)
# print(f"Nama: {user.nama}, Saldo: {user.saldo}")

"""Protected"""
# class Karyawan:
#     def __init__(self, nama, gaji):
#         self.nama = nama
#         self._gaji = gaji # protected, hanya "disarankan" diakses dari dalam

# class Manager(Karyawan):
#     def tampilkan_gaji(self):
#         # subclass tetap bisa mengakses atribut protected milik parent
#         print(f"Gaji {self.nama}: {self._gaji}")

# manager = Manager("Daffa", 12000000)
# manager.tampilkan_gaji()
# print(manager._gaji) # masih bisa diakses, tapi secara konvensi sebaiknya tidak

"""Private"""
# class RekeningBank:
#     def __init__(self, pemilik, saldo):
#         self.pemilik = pemilik
#         self.__saldo = saldo # private
        
#     def tarik_saldo(self, jumlah):
#         if jumlah > self.__saldo:
#             print("Saldo tidak cukup.")
#         elif jumlah <= 0:
#             print("Jumlah penarikan tidak valid.")
#         else:
#             self.__saldo -= jumlah          
#             print(f"Berhasil menarik {jumlah}. Sisa saldo: {self.__saldo}")
            
#     def cek_saldo(self):
#         print(f"Saldo saat ini: {self.__saldo}")

# rekening = RekeningBank("Budi", 100000)
# rekening.tarik_saldo(30000)
# rekening.cek_saldo()
# """print(rekening.__saldo)""" # AttributeError, karena sudah di-name-mangling
# # akses "paksa" ke private tetap mungkin lewat name mangling, tapi ini
# # melanggar konvensi encapsulation dan sebaiknya TIDAK dilakukan:
# print(rekening._RekeningBank__saldo) # 70000, tapi ini praktik yang buruk

"""Getter & Setter Manual"""
# class RekeningBank:
#     def __init__(self, pemilik, saldo):
#         self.pemilik = pemilik
#         self.__saldo = saldo
#     def get_saldo(self):
#         return self.__saldo
#     def set_saldo(self, saldo_baru):
#         if saldo_baru < 0:
#             print("Saldo tidak boleh negatif.")
#         else:
#             self.__saldo = saldo_baru

# rekening = RekeningBank("Budi", 100000)
# print(rekening.get_saldo())
# rekening.set_saldo(-500) # ditolak oleh validasi
# rekening.set_saldo(200000) # diterima
# print(rekening.get_saldo())

"""Getter & Setter Dengan Decorator"""
# class RekeningBank:
#     def __init__(self, pemilik, saldo):
#         self.pemilik = pemilik
#         self.__saldo = saldo
        
#     @property
#     def saldo(self):
#         """Getter -- dipanggil seperti atribut biasa, tanpa tanda
#         kurung."""
#         return self.__saldo
    
#     @saldo.setter
#     def saldo(self, saldo_baru):
#         """Setter -- dijalankan otomatis saat ada assignment ke
#         rekening.saldo"""
#         if saldo_baru < 0:
#             raise ValueError("Saldo tidak boleh negatif.")
        
#         self.__saldo = saldo_baru

# rekening = RekeningBank("Budi", 100000)
# print(rekening.saldo) # dipanggil seperti atribut, bukan method
# rekening.saldo = 250000 # otomatis lewat setter dengan validasi
# print(rekening.saldo)
# rekening.saldo = -1000 # akan raise ValueError


"""Latihan"""
class Buku:
    def __init__(self, NomorBuku, NamaBuku):
        self.__nama = NamaBuku
        self._nomor = NomorBuku
        
    """Getter & Setter Manual"""
    def get_name(self):
        return self.__nama
    
    def set_name(self, NamaBaru):
        self.nama = NamaBaru
        
    """Getter & Setter Decorator"""
    @property
    def nama(self):
        return self.__nama
    
    