**Penjelasan Program**

Sistem ini mengelola alur penyewaan barang berupa tenda dan kursi tamu oleh pelanggan. Alur kerja utama meliputi pendaftaran inventaris barang, pengelolaan stok dan harga, hingga eksekusi transaksi penyewaan yang secara otomatis akan memotong saldo pelanggan dan mengurangi stok barang jika syarat transaksi terpenuhi. Program beroperasi melalui tiga entitas utama yang saling berinteraksi secara dinamis.
Struktur Class

**Program ini terdiri dari tiga class utama yang berdiri sendiri:**
1. Class Tenda
Digunakan untuk merepresentasikan entitas tenda yang disewakan.
- Atribut Class: TotalTenda, BiayaPemasangan (Data konfigurasi umum yang berlaku untuk semua objek tenda).
- Atribut Instance: IDTenda, Jenis, HargaTenda (Public), dan __StokTenda (Private).
    Method:
    - @property Stok & @Stok.setter: Mengamankan akses dan memvalidasi perubahan stok tenda agar tidak bernilai negatif.
    - TampilkanTenda(): Instance method untuk mencetak rincian data tenda.
    - UbahBiayaPasang(): Class method untuk memodifikasi konfigurasi BiayaPemasangan.
    - ValidasiIDTenda(): Static method untuk memvalidasi format ID tenda (wajib berawalan "T-").

2. Class KursiTamu
Digunakan untuk merepresentasikan entitas kursi yang disewakan.
- Atribut Class: TotalKursi, BiayaTata.
- Atribut Instance: IDKursi, Merk, HargaKursi (Public), dan __StokKursi (Private).
    Method:
    - @property StokKursi & @StokKursi.setter: Getter dan Setter dengan validasi input angka.
    - TampilkanKursi(): Instance method untuk menampilkan spesifikasi kursi.
    - UbahBiayaTata(): Class method untuk memperbarui biaya penataan kursi.
    - ValidasiIDKursi(): Static method untuk memastikan ID kursi sesuai format ("K-").

3. Class Penyewa
Digunakan untuk merepresentasikan data pelanggan dan logika transaksi.
- Atribut Class: TotalPenyewa, DendaTelat, BatasSewa.
- Atribut Instance: Nama, Kontak (Public), dan __Saldo (Private).
    Method:
    - @property Saldo & @Saldo.setter: Mengunci akses saldo dan mencegah pengisian saldo bernilai minus.
    - SewaTenda(): Instance method yang mencontohkan interaksi antar objek. Method ini menerima objek Tenda, memvalidasi ketersediaan stok,  menghitung total biaya, dan memotong saldo penyewa.
    - Peraturan(): Class method untuk menampilkan informasi aturan sewa.
    - ValidasiKontak(): Static method untuk mengecek keabsahan nomor ponsel (wajib berawalan "08").

**Panduan Pengujian (Testing Guide)**
Untuk menjalankan program, eksekusi file Python secara langsung. Output di terminal akan menampilkan 5 fase pengujian utama:
    - Fase Inisialisasi Objek
        - Program membuat 2 objek Tenda, 2 objek KursiTamu, dan 2 objek Penyewa.
        - Fungsi __dict__ dipanggil untuk membuktikan bahwa atribut instance (termasuk yang private dengan name mangling) berhasil dibuat.
    - Fase Uji Instance Method
        - Memanggil TampilkanTenda() dan TampilkanKursi() untuk memverifikasi bahwa objek dapat mengolah dan mencetak datanya sendiri.
    - Fase Uji Class & Static Method
        - Biaya pasang tenda diubah menggunakan class method.
        - Format ID diuji menggunakan static method dan menghasilkan nilai True/False sesuai keabsahan ID.
    - Fase Uji Setter & Validasi (Encapsulation)
        - Sistem mencoba memasukkan stok minus (-10) dan saldo minus (-50000).
        - Ekspektasi Output: Program mencetak pesan [Error] / Tidak Valid!!! dan menolak perubahan data.
        - Sistem memasukkan stok valid (90), data berhasil diperbarui.
    - Fase Uji Interaksi Antar Objek (Transaksi)
        - Skenario 1 (Berhasil): Penyewa "Budi" (Saldo Rp1.000.000) menyewa 2 Tenda VIP. Transaksi berhasil, saldo Budi berkurang, dan stok tenda VIP berkurang.
        - Skenario 2 (Gagal): Penyewa "Siti" (Saldo Rp100.000) menyewa 1 Tenda Standar. Transaksi ditolak oleh sistem karena saldo tidak mencukupi untuk membayar sewa beserta biaya pemasangan.