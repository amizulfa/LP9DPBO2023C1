from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, fasilitas, gambar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.fasilitas = fasilitas
        self.gambar = gambar

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_fasilitas(self):
        return self.fasilitas
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nFasilitas : " + self.fasilitas + "\n"
    
    def get_gambar(self):
        return self.gambar