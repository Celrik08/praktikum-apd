from Data_Produk import produk
from Fungsi_Tampil_Data import tampilkan_produk

def hapus_produk():
    tampilkan_produk()
    id_hapus = input("Masukkan ID produk yang ingin anda dihapus: ")

    if not id_hapus.isdigit():
        print("ID harus angka!, bukan berupa huruf")
        input("Tekan Enter untuk kembali...")
        return

    id_hapus = int(id_hapus)
    if id_hapus not in produk:
        print("Produk tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    konfirmasi = input(f"Yakin ingin menghapus produk tersebut'{produk[id_hapus]['nama']}'? (y/n): ").lower()
    if konfirmasi == "y":
        del produk[id_hapus]
        print("Produk berhasil dihapus!, silahkan di cek datanya")
    else:
        print("Anda membatalkan penghapusan.")
    input("Tekan Enter untuk kembali...")