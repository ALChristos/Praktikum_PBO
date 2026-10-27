from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol


class BarangSewa(ABC):
    def __init__(self, IDBarang: str, NamaBarang: str, HargaSewa: int, Stok: int) -> None:
        if not IDBarang.strip() or not NamaBarang.strip():
            raise ValueError("ID dan nama barang wajib diisi.")
        if type(HargaSewa) is not int or HargaSewa < 0:
            raise ValueError("Harga sewa harus bilangan bulat nonnegatif.")
        if type(Stok) is not int or Stok < 0:
            raise ValueError("Stok harus bilangan bulat nonnegatif.")

        self.IDBarang = IDBarang
        self.NamaBarang = NamaBarang
        self._HargaSewa = HargaSewa
        self.__Stok = Stok

    @property
    def Stok(self) -> int:
        return self.__Stok

    @property
    def HargaSewa(self) -> int:
        return self._HargaSewa

    @abstractmethod
    def HitungBiayaTambahan(self) -> int:
        pass

    @abstractmethod
    def InfoKhusus(self) -> None:
        pass
    
    def KurangiStok(self, jumlah: int) -> bool:
        if type(jumlah) is not int or not 0 < jumlah <= self.__Stok:
            return False
        self.__Stok -= jumlah
        return True

    def HitungEstimasiBiaya(self) -> int:
        return self.HargaSewa + self.HitungBiayaTambahan()

    def TampilkanInfo(self) -> None:
        print(self)
        self.InfoKhusus()
        print(f"Estimasi biaya untuk 1 unit: Rp{self.HitungEstimasiBiaya():,}")

    def __str__(self) -> str:
        return(
            f"ID: {self.IDBarang} | Nama: {self.NamaBarang} | "
            f"Harga sewa: Rp{self.HargaSewa:,} | Stok: {self.Stok}"
        )


class Tenda(BarangSewa):
    TotalTenda = 0
    BiayaPemasangan = 250_000

    def __init__(self, IDTenda: str, Jenis: str, Harga: int, Stok: int, Kapasitas: int) -> None:
        if not self.ValidasiIDTenda(IDTenda):
            raise ValueError("ID tenda harus diawali 'T-'.")
        if type(Kapasitas) is not int or Kapasitas <= 0:
            raise ValueError("Kapasitas harus bilangan bulat positif.")
        super().__init__(IDTenda, Jenis, Harga, Stok)
        self.Kapasitas = Kapasitas
        Tenda.TotalTenda += 1

    def HitungBiayaTambahan(self) -> int:
        return type(self).BiayaPemasangan

    def InfoKhusus(self) -> None:
        print(f"Kapasitas: {self.Kapasitas} orang")
        print(f"Biaya pemasangan: Rp{self.HitungBiayaTambahan():,}")

    @classmethod
    def UbahBiayaPasang(cls, BiayaBaru: int) -> None:
        if type(BiayaBaru) is not int or BiayaBaru < 0:
            raise ValueError("Biaya pemasangan tidak valid.")
        cls.BiayaPemasangan = BiayaBaru

    @staticmethod
    def ValidasiIDTenda(IDTenda: str) -> bool:
        return isinstance(IDTenda, str) and IDTenda.startswith("T-")


class KursiTamu(BarangSewa):
    TotalKursi = 0
    BiayaTata = 150_000

    def __init__(self, IDKursi: str, Merk: str, Harga: int, Stok: int, BahanKursi: str) -> None:
        if not self.ValidasiIDKursi(IDKursi):
            raise ValueError("ID kursi harus diawali 'K-'.")
        if not BahanKursi.strip():
            raise ValueError("Bahan kursi wajib diisi.")
        super().__init__(IDKursi, Merk, Harga, Stok)
        self.BahanKursi = BahanKursi
        KursiTamu.TotalKursi += 1

    def HitungBiayaTambahan(self) -> int:
        return type(self).BiayaTata

    def InfoKhusus(self) -> None:
        print(f"Bahan kursi: {self.BahanKursi}")
        print(f"Biaya penataan: Rp{self.HitungBiayaTambahan():,}")

    @classmethod
    def UbahBiayaTata(cls, BiayaBaru: int) -> None:
        if type(BiayaBaru) is not int or BiayaBaru < 0:
            raise ValueError("Biaya penataan tidak valid.")
        cls.BiayaTata = BiayaBaru

    @staticmethod
    def ValidasiIDKursi(IDKursi: str) -> bool:
        return isinstance(IDKursi, str) and IDKursi.startswith("K-")


class Admin:
    def __init__(self, NamaAdmin: str) -> None:
        self.NamaAdmin = NamaAdmin

    def Melayani(self, Penyewa: Penyewa) -> None:
        print(f"Admin {self.NamaAdmin} melayani penyewa: {Penyewa.Nama}")
        Penyewa.AdminPelayan = self


class KartuMember:
    POIN_AWAL = 100

    def __init__(self, NamaMember: str) -> None:
        self.NamaMember = NamaMember
        self.Poin = self.POIN_AWAL

    def InfoKartu(self) -> None:
        print(f"Kartu member {self.NamaMember} memiliki {self.Poin} poin.")

    def TampilkanInfo(self) -> None:
        self.InfoKartu()


class Penyewa:
    TotalPenyewa = 0
    DendaTelat = 100_000
    BatasSewa = 7

    def __init__(self, Nama: str, Kontak: str, Saldo: int) -> None:
        if not Nama.strip():
            raise ValueError("Nama penyewa wajib diisi.")
        if not self.ValidasiKontak(Kontak):
            raise ValueError("Kontak harus berupa nomor yang diawali '08'.")

        self.Nama = Nama
        self.Kontak = Kontak
        self.__Saldo = 0
        self.Saldo = Saldo
        self.AdminPelayan: Admin | None = None
        self.DaftarSewa: list[tuple[BarangSewa, int]] = []
        self.Kartu = KartuMember(self.Nama)
        Penyewa.TotalPenyewa += 1

    @property
    def Saldo(self) -> int:
        return self.__Saldo

    @Saldo.setter
    def Saldo(self, SaldoBaru: int) -> None:
        if type(SaldoBaru) is not int or SaldoBaru < 0:
            raise ValueError("Saldo harus bilangan bulat nonnegatif.")
        self.__Saldo = SaldoBaru

    def CekAdmin(self) -> None:
        if self.AdminPelayan is not None:
            print(f"{self.Nama} dilayani oleh admin {self.AdminPelayan.NamaAdmin}")

    def SewaBarang(self, Barang: BarangSewa, Jumlah: int) -> bool:
        if type(Jumlah) is not int or Jumlah <= 0:
            print("Jumlah sewa tidak valid!")
            return False

        print(f"{self.Nama} menyewa {Jumlah} {Barang.NamaBarang}")
        total_biaya = Barang.HargaSewa * Jumlah + Barang.HitungBiayaTambahan()
        if self.__Saldo < total_biaya:
            print(f"Saldo tidak cukup! Butuh Rp{total_biaya:,}")
            return False
        if not Barang.KurangiStok(Jumlah):
            print("Stok tidak cukup!")
            return False

        self.__Saldo -= total_biaya
        self.DaftarSewa.append((Barang, Jumlah))
        print(f"Berhasil menyewa! Sisa saldo {self.Nama}: Rp{self.__Saldo:,}")
        return True

    def CekBarangSewa(self) -> None:
        print(f"Barang yang disewa oleh {self.Nama}:")
        if not self.DaftarSewa:
            print("Belum ada barang yang disewa.")
        for nomor, (barang, jumlah) in enumerate(self.DaftarSewa, start=1):
            print(f"{nomor}. {jumlah} {barang.NamaBarang}")

    def CekKartuMember(self) -> None:
        self.Kartu.InfoKartu()

    @classmethod
    def Peraturan(cls) -> None:
        print(f"Batas sewa {cls.BatasSewa} hari; denda Rp{cls.DendaTelat:,}/hari.")

    @staticmethod
    def ValidasiKontak(NoKontak: str) -> bool:
        return isinstance(NoKontak, str) and NoKontak.startswith("08")


class DapatDitampilkan(Protocol):
    def TampilkanInfo(self) -> None:
        pass

def TampilkanObjek(objek: DapatDitampilkan) -> None:
    objek.TampilkanInfo()


admin1 = Admin("Om Bram")
tenda1 = Tenda("T-01", "Tenda VIP Tertutup", 150_000, 5, 300)
tenda2 = Tenda("T-02", "Tenda Standar Terbuka", 80_000, 2, 100)
kursi1 = KursiTamu("K-01", "Kursi + Cover", 5_000, 100, "Rangka Stainless")
kursi2 = KursiTamu("K-02", "Kursi Biasa", 2_000, 200, "Rangka Plastik")
penyewa1 = Penyewa("Budi", "081234", 1_000_000)
penyewa2 = Penyewa("Siti", "089876", 100_000)

print("=== 1. ASOSIASI ===")
admin1.Melayani(penyewa1)
penyewa1.CekAdmin()

print("\n=== 2. AGREGASI DAN KOMPOSISI ===")
penyewa1.SewaBarang(tenda1, 2)
penyewa1.SewaBarang(kursi1, 10)
penyewa1.CekBarangSewa()
penyewa1.CekKartuMember()

print("\n=== 3. INHERITANCE DAN OVERRIDING ===")
for barang in (tenda1, kursi1):
    barang.TampilkanInfo()
    print()

print("=== 4. ABSTRAKSI ===")
try:
    BarangSewa("X-01", "Barang Abstrak", 1_000, 1)
except TypeError as error:
    print(f"[TypeError] {error}")

class TendaSetengahJadi(BarangSewa):
    def HitungBiayaTambahan(self) -> int:
        return 0

try:
    TendaSetengahJadi("X-02", "Setengah Jadi", 1_000, 1)
except TypeError as error:
    print(f"[TypeError] {error}")

print("\n=== 5. POLIMORFISME VIA PEWARISAN ===")
for barang in (tenda2, kursi2):
    print(f"{barang.NamaBarang}: biaya tambahan Rp{barang.HitungBiayaTambahan():,}")
    barang.InfoKhusus()

print("\n=== 6. DUCK TYPING ===")
for objek in (tenda1, penyewa1.Kartu):
    TampilkanObjek(objek)

print("\n=== 7. OPERATOR OVERLOADING (__str__) ===")
print(tenda1)
print(kursi1)

print("\n=== 8. SOLID: OPEN/CLOSED PRINCIPLE ===")
for barang in (tenda2, kursi2):
    print(f"{barang.NamaBarang}: Rp{barang.HitungEstimasiBiaya():,} untuk 1 unit")

print("\n=== 9. VALIDASI ===")
penyewa2.SewaBarang(tenda1, 1)
try:
    penyewa2.Saldo = -5_000
except ValueError as error:
    print(f"[ValueError] {error}")


