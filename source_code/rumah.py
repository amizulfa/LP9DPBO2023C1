from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, gambar):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.luas_tanah = luas_tanah
        self.gambar = gambar

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_luas_tanah(self):
        return self.luas_tanah

    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Tanah : " + self.luas_tanah + "\n"

    def get_gambar(self):
        return self.gambar