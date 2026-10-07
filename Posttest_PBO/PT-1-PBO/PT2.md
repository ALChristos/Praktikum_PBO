**Penjelasan Program**
Program ini merupakan simulasi Sistem Penyewaan Alat Pesta Pernikahan dengan menerapkan sistem Relasi UML dan Inheritance (Pewarisan) seperti penggunaan superclass untuk mengelola stok dan harga, yang kemudian diwariskan ke barang spesifik seperti tenda dan kursi. Selain itu, sistem ini juga terdapat interaksi antara admin, pelanggan, dan kartu member ke dalam alur transaksi yang secara otomatis memvalidasi ketersediaan barang serta memotong saldo pelanggan dengan aman.

**Penerapan Relasi UML**
1. Relasi UML
    - Asosiasi: Terjadi pada interaksi kelas Admin dan Penyewa. Kelas Admin memanggil Penyewa melalui method Melayani(), lalu menautkan dirinya ke dalam atribut Penyewa.AdminPelayan sebagai pengingat, tanpa ada relasi fisik yang kuat.   
    
    - Agregasi: Diterapkan saat kelas Penyewa menyewa barang. Objek Tenda atau KursiTamu merupakan objek independen, kemudian dimasukkan ke dalam list self.BarangSewa. Jika objek Penyewa dihapus, maka objek barang di memori tetap aman.   
    
    - Komposisi: Terjadi antara kelas Penyewa dan KartuMember. Objek KartuMember tidak diciptakan di luar, melainkan langsung buat di dalam konstruktor __init__ milik Penyewa (self.Kartu = KartuMember(self.Nama)). Eksistensi kartu ini bergantung mutlak pada penyewa.   
    

2. Inheritance (Pewarisan)
    - Superclass & Subclass: Kelas BarangSewa bertindak sebagai Superclass (induk), yang menurunkan sifat-sifat dasarnya ke 2 Subclass (anak) yaitu kelas Tenda dan KursiTamu.   
    
    - Penggunaan super(): Di dalam konstruktor Tenda dan KursiTamu, terdapat pemanggilan super().__init__(IDTenda, Jenis, Harga, Stok) yang berfungsi untuk pembuatan atribut dasar ke kelas induk.   
    
    - Atribut Tambahan: Setiap subclass memiliki ciri khasnya sendiri seperti kelas Tenda memiliki atribut tambahan self.Kapasitas dan KursiTamu memiliki self.BahanKursi.   
    
    - Method Overriding: Metode TampilkanInfo() milik kelas induk didefinisikan ulang di dalam kelas anak. Kelas anak menumpuk metode tersebut dengan menambahkan cetakan khusus seperti kapasitas, bahan kursi, dan perhitungan biaya setelah memanggil info dasar dari superclass.   
    
    - Tingkat Akses (Protected & Private):
        - Protected: Atribut _HargaSewa pada kelas induk berhasil diakses dan dimanipulasi secara langsung di dalam subclass untuk menghitung nilai EstimasiBiaya.   
        
        - Private: Atribut __Stok dikunci sebagai data eksklusif kelas induk. Subclass dan objek luar tidak bisa memotong stok secara langsung, melainkan harus melewati metode resmi KurangiStok().   
        