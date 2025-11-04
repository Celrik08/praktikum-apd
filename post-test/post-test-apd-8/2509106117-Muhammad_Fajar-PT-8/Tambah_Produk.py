import os
from Data_Produk import produk

def tambah_produk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SILAHKAN TAMBAH PRODUK BARU===")
    nama = input("Nama produk: ")

    while True:
        harga = input("Harga produk: ")
        stok = input("Stok produk: ")
        if not harga.isdigit() or not stok.isdigit():
            print("Harga dan stok harus berupa angka! Bukan berupa huruf")
            input("Tekan Enter untuk ulangi...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== SILAHKAN TAMBAH PRODUK BARU ===")
            print(f"Nama produk: {nama}")
        else:
            break

    new_id = max(produk.keys()) + 1 if produk else 1
    produk[new_id] = {"nama": nama, "harga": int(harga), "stok": int(stok)}
    print("Produk berhasil ditambahkan!, silahkan cek datanya")
    input("Tekan Enter untuk kembali...")