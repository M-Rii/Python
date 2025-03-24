from abc import ABC, abstractmethod

def log_activity(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if "Masuk" in func.__name__:
            print("Barang berhasil masuk")
        elif "Keluar" in func.__name__:
            print("Barang berhasil keluar")
        print(result)
        return result
    return wrapper

class Transaksi(ABC):
    def __init__(self):
        self.id = None
        self.nama = None
        self.jumlah = None
        self.deskripsi = None

    def inputID(self):
        self.id = input("Masukkan ID Barang: ")
        return f"ID Barang: {self.id}"

    def inputNama(self):
        self.nama = input("Masukkan Nama Barang: ")
        return f"Nama Barang: {self.nama}"

    def inputJumlah(self):
        self.jumlah = int(input("Masukkan Jumlah Barang: "))
        return f"Jumlah Barang: {self.jumlah}"

    def inputDeskripsi(self):
        self.deskripsi = input("Masukkan Deskripsi Barang: ")
        return f"Deskripsi: {self.deskripsi}"

    @abstractmethod
    def proses_transaksi(self):
        pass

class Masuk(Transaksi):
    @log_activity
    def proses_transaksi(self): 
        return f"Barang Masuk - ID: {self.id}, Nama: {self.nama}, Jumlah: {self.jumlah}, Deskripsi: {self.deskripsi}"

class Keluar(Transaksi):
    @log_activity
    def proses_transaksi(self):
        return f"Barang Keluar - ID: {self.id}, Nama: {self.nama}, Jumlah: {self.jumlah}, Deskripsi: {self.deskripsi}"

class Gudang:
    def __init__(self):
        self.list_barang = []

    @log_activity
    def barangMasuk(self, id_barang, nama_barang, jumlah_barang, deskripsi_barang):
        self.list_barang.append({"ID": id_barang, "Nama": nama_barang, "Jumlah": jumlah_barang, "Deskripsi": deskripsi_barang})
        return f"Barang masuk: {nama_barang} ({jumlah_barang} unit), Deskripsi: {deskripsi_barang}"

    @log_activity
    def barangKeluar(self, id_barang, jumlah_barang):
        for barang in self.list_barang:
            if barang["ID"] == id_barang:
                if barang["Jumlah"] >= jumlah_barang:
                    barang["Jumlah"] -= jumlah_barang
                    if barang["Jumlah"] == 0:
                        self.list_barang.remove(barang)
                    return f"Barang keluar: {barang['Nama']} ({jumlah_barang} unit), {barang['Deskripsi']}"
                else:
                    return f"Jumlah barang tidak mencukupi untuk dikeluarkan"
        return f"Barang dengan ID {id_barang} tidak ditemukan"

    def detail(self):
        if not self.list_barang:
            print("Tidak ada barang")
        else:
            print("\nDetail Barang:")
            for barang in self.list_barang:
                print(f"ID: {barang['ID']}, Nama: {barang['Nama']}, Jumlah: {barang['Jumlah']}, Deskripsi: {barang['Deskripsi']}")
        print("\n")

if __name__ == "__main__":
    gudang = Gudang()

    while True:
        print("\n=== Sistem Gudang ===")
        print("1. Barang Masuk")
        print("2. Barang Keluar")
        print("3. Detail Barang")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            transaksi_masuk = Masuk()
            id_barang = transaksi_masuk.inputID()
            nama_barang = transaksi_masuk.inputNama()
            jumlah_barang = transaksi_masuk.inputJumlah()
            deskripsi_barang = transaksi_masuk.inputDeskripsi()
            transaksi_masuk.proses_transaksi()
            gudang.barangMasuk(transaksi_masuk.id, transaksi_masuk.nama, transaksi_masuk.jumlah, deskripsi_barang)

        elif pilihan == "2":
            transaksi_keluar = Keluar()
            id_barang = transaksi_keluar.inputID()
            nama_barang = transaksi_keluar.inputNama()
            jumlah_barang = transaksi_keluar.inputJumlah()
            transaksi_keluar.proses_transaksi()
            gudang.barangKeluar(transaksi_keluar.id, transaksi_keluar.jumlah)

        elif pilihan == "3":
            gudang.detail()

        elif pilihan == "4":
            print("Keluar dari sistem. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
