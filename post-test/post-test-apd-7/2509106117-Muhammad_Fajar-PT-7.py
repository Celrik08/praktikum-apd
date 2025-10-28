import os

# Disini variabel global 1
users = {
    1: {"username": "admin", "password": "123", "role": "admin"},
    2: {"username": "user", "password": "123", "role": "user"}
}

# Disini variabel global 2
produk = {
    1: {"nama": "Sabun Lifeboy", "harga": 5000, "stok": 20},
    2: {"nama": "Shampo Sunslik", "harga": 10000, "stok": 15},
    3: {"nama": "Minyak Goreng", "harga": 14000, "stok": 10}
}

# Disini variabel global 3
riwayat_penjualan = {}

# Disini defnya ada fungsi tanpa parameter
def tampilkan_produk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DAFTAR PRODUK MINIMARKET MUHAMMAD FAJAR ===")
    print("ID\tNama\t\t\tHarga\tStok")
    print("-" * 50)
    for idp, data in produk.items():
        print(f"{idp}\t{data['nama']:<20}\tRp{data['harga']}\t{data['stok']}")
    print("-" * 50)

# Disini defnya ada fungsi dengan parameter
def hitung_total(harga, jumlah):
    return harga * jumlah

# Disini defnya ada fungsi dengan parameter
def login_user(username, password):
    for id_user, data in users.items():
        if data["username"] == username and data["password"] == password:
            return {"id": id_user, **data}
    return None

# Disini def prosedur
def tambah_produk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SILAHKAN TAMBAH PRODUK BARU ===")
    nama = input("Nama produk: ")

    while True:
        harga = input("Harga produk: ")
        stok = input("Stok produk: ")

        if not harga.isdigit() or not stok.isdigit():
            print("Harga dan stok harus berupa angka! Bukan berupa huruf")
            input("Tekan Enter untuk ulangi input...")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== SILAHKAN TAMBAH PRODUK BARU ===")
            print(f"Nama produk: {nama}")
        else:
            break

    new_id = max(produk.keys()) + 1 if produk else 1
    produk[new_id] = {"nama": nama, "harga": int(harga), "stok": int(stok)}
    print("Produk berhasil ditambahkan!, silahkan cek datanya")
    input("Tekan Enter untuk kembali...")

# Disini def prosedur
def ubah_produk():
    tampilkan_produk()
    # Disini variabel lokal 1
    id_edit = input("Masukkan ID produk yang ingin diedit/diubah: ")

    # Disini error Handling
    if not id_edit.isdigit():
        print("ID harus berupa angka!, bukan berupa huruf")
        input("Tekan Enter untuk kembali...")
        return

    # Disini variabel lokal 2
    id_edit = int(id_edit)

    if id_edit not in produk:
        print("ID Produk tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    # Disini variabel lokal 3
    data = produk[id_edit]
    print(f"\nProduk yang akan diedit: {data['nama']}")
    # Disini variabel lokal 4
    nama_baru = input("Nama baru (kosongkan jika tidak ingin diubah oleh anda): ")
    # Disini variabel lokal 5
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

# Disini def prosedur
def hapus_produk():
    tampilkan_produk()
    id_hapus = input("Masukkan ID produk yang ingin anda hapus: ")

    if not id_hapus.isdigit():
        print("ID harus berupa angka!, bukan berupa huruf")
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

# Disini defnya ada fungsi rekursif
def rekursif_penjualan(keys, index=0):
    if index >= len(keys):
        return
    key = keys[index]
    print(f"Laporan ke-{key}: Rp{riwayat_penjualan[key]}")
    rekursif_penjualan(keys, index + 1)

# Disini def prosedur
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

    print(f"Berhasil membeli {jumlah} {data['nama']} seharga Rp{total}")
    input("Tekan Enter untuk kembali...")

# Disini defnya ada fungsi tanpa parameter
def tampil_penjualan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== LAPORAN PENJUALAN MINIMARKET MUHAMMAD FAJAR===")
    if not riwayat_penjualan:
        print("Belum ada transaksi penjualan.\n")
    else:
        keys = list(riwayat_penjualan.keys())
        rekursif_penjualan(keys)
        print(f"\nTotal keseluruhan: Rp{sum(riwayat_penjualan.values())}")
    input("Tekan Enter untuk kembali...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MINIMARKET MUHAMMAD FAJAR ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("SILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA")
        username = input("Username: ")
        password = input("Password: ")

        user_aktif = login_user(username, password)

        if user_aktif is None:
            print("Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue

        print(f"Login berhasil! Selamat datang, {user_aktif['role'].capitalize()} {user_aktif['username']}")
        input("Tekan Enter untuk melanjutkan...")

        if user_aktif["role"] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("===ANDA MASUK MENU ADMIN ===")
                print("1. Lihat Produk")
                print("2. Tambah Produk")
                print("3. Ubah Produk")
                print("4. Hapus Produk")
                print("5. Laporan Penjualan")
                print("6. Logout")

                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    tampilkan_produk()
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "2":
                    tambah_produk()

                elif pilihan == "3":
                    ubah_produk()

                elif pilihan == "4":
                    hapus_produk()

                elif pilihan == "5":
                    tampil_penjualan()
                
                elif pilihan == "6":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== ANDA MASUK MENU USER ===")
                print("1. Lihat Produk")
                print("2. Beli Produk")
                print("3. Logout")

                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    tampilkan_produk()
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "2":
                    beli_produk()

                elif pilihan == "3":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SILAHKAN REGISTER AKUN BARU ANDA===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        ada = any(data["username"] == username for data in users.values())

        if ada:
            print("Username sudah digunakan!, Silahkan buat Username baru")
        else:
            new_id = max(users.keys()) + 1 if users else 1
            users[new_id] = {"username": username, "password": password, "role": "user"}
            print("Akun berhasil dibuat!")

        input("Tekan Enter untuk kembali...")

    elif menu == "3":
        print("Terima kasih telah menggunakan aplikasi Minimarket Muhammad Fajar.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")