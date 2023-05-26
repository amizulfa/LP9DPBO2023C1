from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, harga_per_bulan, gambar):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga_per_bulan = harga_per_bulan
        self.gambar = gambar

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_harga_per_bulan(self):
        return self.harga_per_bulan

    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nPenghuni : " + self.nama_penghuni + "\nHarga per Bulan : " + str(self.harga_per_bulan) + "\n"

    def get_gambar(self):
        return self.gambar