from Data_Produk import produk
from Riwayat_Penjualan import riwayat_penjualan
from Hitung_Total import hitung_total
from Fungsi_Tampil_Data import tampilkan_produk

def beli_produk():
    tampilkan_produk()
    id_produk = input("Masukkan ID produk yang ingin dibeli oleh anda: ")

    if not id_produk.isdigit():
        print("ID harus berupa angka!, bukan berupa huruf")
        input("Tekan Enter untuk kembali...")
        return

    id_produk = int(id_produk)
    if id_produk not in produk:
        print("Produk tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    jumlah = input("Masukkan jumlah yang ingin dibeli: ")
    if not jumlah.isdigit():
        print("Jumlah harus angka!, bukan berupa huruf")
        input("Tekan Enter untuk kembali...")
        return

    jumlah = int(jumlah)
    data = produk[id_produk]

    if jumlah > data["stok"]:
        print("Stok tidak mencukupi! / Kosong")
        input("Tekan Enter untuk kembali...")
        return

    total = hitung_total(data["harga"], jumlah)
    data["stok"] -= jumlah

    nomor_transaksi = len(riwayat_penjualan) + 1
    riwayat_penjualan[nomor_transaksi] = total

    print(f"Berhasil membeli {jumlah} {data['nama']} total Rp{total}")
    input("Tekan Enter untuk kembali...")