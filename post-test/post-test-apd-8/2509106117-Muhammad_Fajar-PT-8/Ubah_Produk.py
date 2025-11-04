from Data_Produk import produk
from Fungsi_Tampil_Data import tampilkan_produk

def ubah_produk():
    tampilkan_produk()
    id_edit = input("Masukkan ID produk yang ingin diedit/diubah: ")

    if not id_edit.isdigit():
        print("ID harus berupa angka!, bukan berupa huruf")
        input("Tekan Enter untuk kembali...")
        return

    id_edit = int(id_edit)
    if id_edit not in produk:
        print("ID produk tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    data = produk[id_edit]
    print(f"\nProduk yang akan diedit: {data['nama']}")
    nama_baru = input(f"Nama baru (kosongkan jika tidak ingin diubah oleh anda): ")
    harga_baru = input("Harga baru (kosongkan jika tidak ingin diubah oleh anda): ")
    stok_baru = input("Stok baru (kosongkan jika tidak ingin diubah oleh anda): ")

    if not harga_baru.isdigit() or not stok_baru.isdigit():
        print("Harga dan stok harus berupa angka!, bukan berupa huruf")
        input("Tekan Enter untuk kembali...")
        return

    if nama_baru:
        data["nama"] = nama_baru
    if harga_baru:
        data["harga"] = int(harga_baru)
    if stok_baru:
        data["stok"] = int(stok_baru)

    print("Produk berhasil diperbarui!, silahkan di cek datanya")
    input("Tekan Enter untuk kembali...")