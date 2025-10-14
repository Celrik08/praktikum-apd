import os

users = [
    [1, "admin", "123", "admin"],
    [2, "user", "123", "user"]
]

produk = [
    [1, "Sabun Lifeboy", 5000, 20],
    [2, "Shampoo Sunslik", 10000, 15],
    [3, "Minyak Goreng", 14000, 10]
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MINIMARKET MUHAMMAD FAJAR===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Silahkan pilih menu: ")

    if menu == "1":
        user = None

        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA===")
        username = input("Username: ")
        password = input("Password: ")

        for u in users:
            if u[1] == username and u[2] == password:
                user = u
                break

        if user is None:
            print("\nUsername atau password salah!")
            input("Tekan Enter untuk kembali ke menu utama...")
            continue

        print(f"\nLogin berhasil! Selamat datang, {user[3]}")
        input("Tekan Enter untuk melanjutkan...")

        # ini ketika pengguna masuk sebagai admin
        if user[3] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. Lihat Produk")
                print("2. Tambah Produk")
                print("3. Update Produk")
                print("4. Hapus Produk")
                print("5. Logout")

                pilihan = input("Pilih menu: ")

                # menampilka produk ketika user pilih 1
                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR PRODUK MINIMARKET MUHAMMAD FAJAR ===")
                    print("ID\tNama\t\tHarga\tStok")
                    print("-"*40)
                    for p in produk:
                        print(f"{p[0]}\t{p[1]:15}\tRp{p[2]}\t{p[3]}")
                    print("-"*40)
                    input("Tekan Enter untuk kembali...")

                # ketika admin ingin menambahkan produk baru
                elif pilihan == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH PRODUK BARU ===")
                    nama = input("Nama produk: ")
                    
                    while True:
                        harga = input("Harga produk: ")
                        stok = input("Stok produk: ")

                        if not harga.isdigit() or not stok.isdigit():
                            print("Harga dan stok harus angka!")
                            input("Tekan Enter untuk mengulang input...")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=== TAMBAH PRODUK BARU ===")
                            print(f"Nama produk: {nama}")
                        else:
                            break

                    new_id = produk[-1][0] + 1 if produk else 1
                    produk.append([new_id, nama, int(harga), int(stok)])
                    print("Produk berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali...")

                # ketika admin ingin memperbarui
                elif pilihan == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UPDATE PRODUK ===")
                    print("ID\tNama\t\tHarga\tStok")
                    print("-"*40)
                    for p in produk:
                        print(f"{p[0]}\t{p[1]:15}\tRp{p[2]}\t{p[3]}")
                    print("-"*40)

                    id_produk = input("Masukkan ID produk yang akan diupdate: ")
                    if not id_produk.isdigit():
                        print("Input ID harus angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_produk = int(id_produk)
                    temukan = False

                    for p in produk:
                        if p[0] == id_produk:
                            temukan = True
                            print(f"Update produk: {p[1]}")
                            nama_baru = input("Nama baru produk (kosongkan jika tidak ingin diubah bagian nama baru produk): ")
                            harga_baru = input("Harga baru produk (kosongkan jika tidak ingin diubah bagian harga baru produk): ")
                            stok_baru = input("Stok baru produk (kosongkan jika tidak ingin diubah bagian stok baru produk): ")

                            if nama_baru == "" and harga_baru == "" and stok_baru == "":
                                print("\nProduk tidak ada yang diupdate!")
                                break

                            if nama_baru != "":
                                p[1] = nama_baru
                            if harga_baru.isdigit():
                                p[2] = int(harga_baru)
                            if stok_baru.isdigit():
                                p[3] = int(stok_baru)

                            print("Data produk berhasil diperbarui!")
                            break

                    if not temukan:
                        print("ID produk tidak ditemukan!")

                    input("Tekan Enter untuk kembali...")

                # ketika admin ingin menghapus produk
                elif pilihan == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS PRODUK ===")
                    print("ID\tNama\t\tHarga\tStok")
                    print("-"*40)
                    for p in produk:
                        print(f"{p[0]}\t{p[1]:15}\tRp{p[2]}\t{p[3]}")
                    print("-"*40)

                    id_produk = input("Masukkan ID produk yang ingin anda hapus: ")
                    if not id_produk.isdigit():
                        print("Input ID harus angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_produk = int(id_produk)
                    temukan = False
                    for p in produk:
                        if p[0] == id_produk:
                            temukan = True
                            produk.remove(p)
                            print("Produk berhasil dihapus!")
                            break
                    if not temukan:
                        print("ID produk tidak ditemukan!")

                    input("Tekan Enter untuk kembali...")

                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

        # ini ketika pengguna masuk sebagai user
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU USER ===")
                print("1. Lihat Produk")
                print("2. Logout")

                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR PRODUK MINIMARKET MUHAMMAD FAJAR===")
                    print("ID\tNama\t\tHarga\tStok")
                    print("-"*40)
                    for p in produk:
                        print(f"{p[0]}\t{p[1]:15}\tRp{p[2]}\t{p[3]}")
                    print("-"*40)
                    input("Tekan Enter untuk kembali...")
                elif pilihan == "2":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

    # ini ketika pengguna, ingin melakukan register
    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ANDA===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")

        ada = False
        for u in users:
            if u[1] == username:
                ada = True
                break

        if ada:
            print("Username sudah digunakan!")
            input("Tekan Enter untuk kembali...")
            continue

        new_id = users[-1][0] + 1 if users else 1
        users.append([new_id, username, password, "user"])

        print(f"Akun berhasil didaftarkan dengan ID User: {new_id}")
        input("Tekan Enter untuk kembali...")

    # ketika pengguna keluar
    elif menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan aplikasi Minimarket Muhammad Fajar")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")