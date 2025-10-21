import os

users = {
    1: {"username": "admin", "password": "123", "role": "admin"},
    2: {"username": "user", "password": "123", "role": "user"}
}

produk = {
    1: {"nama": "Sabun Lifeboy", "harga": 5000, "stok": 20},
    2: {"nama": "Shampo Sunslik", "harga": 10000, "stok": 15},
    3: {"nama": "Minyak Goreng", "harga": 14000, "stok": 10}
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MINIMARKET MUHAMMAD FAJAR ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    # Menu ini adalah menu dimana pengguna harus login
    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("SILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA")
        username = input("Username: ")
        password = input("Password: ")

        user_aktif = None
        for id_user, data in users.items():
            if data["username"] == username and data["password"] == password:
                user_aktif = {"id": id_user, **data}
                break

        if user_aktif is None:
            print("Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue

        print(f"Login berhasil! Selamat datang, {user_aktif['role'].capitalize()} {user_aktif['username']}")
        input("Tekan Enter untuk melanjutkan...")

        # Menu ini khusus untuk pengguna admin, agar bisa mengedit produk
        if user_aktif["role"] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. Lihat Produk")
                print("2. Tambah Produk")
                print("3. Update Produk")
                print("4. Hapus Produk")
                print("5. Logout")

                pilihan = input("Pilih menu: ")

                # Admin bisa melihat produk
                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR PRODUK MINIMARKET MUHAMMAD FAJAR===")
                    print("ID\tNama\t\t\tHarga\tStok")
                    print("-" * 50)
                    for idp, data in produk.items():
                        print(f"{idp}\t{data['nama']:<20}\tRp{data['harga']}\t{data['stok']}")
                    print("-" * 50)
                    input("Tekan Enter untuk kembali...")

                # Admin bisa menambahkan produk
                elif pilihan == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH PRODUK BARU ===")
                    nama = input("Nama produk: ")

                    while True:
                        harga = input("Harga produk: ")
                        stok = input("Stok produk: ")

                        if not harga.isdigit() or not stok.isdigit():
                            print("Harga dan stok harus berupa angka!")
                            input("Tekan Enter untuk ulangi input...")
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=== TAMBAH PRODUK BARU ===")
                            print(f"Nama produk: {nama}")
                        else:
                            break

                    new_id = max(produk.keys()) + 1 if produk else 1
                    produk[new_id] = {"nama": nama, "harga": int(harga), "stok": int(stok)}
                    print("Produk berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali...")

                # Admin bisa update produk
                elif pilihan == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UPDATE PRODUK ===")
                    print("ID\tNama\t\t\tHarga\tStok")
                    print("-" * 50)
                    for idp, data in produk.items():
                        print(f"{idp}\t{data['nama']:<20}\tRp{data['harga']}\t{data['stok']}")
                    print("-" * 50)

                    id_produk = input("Masukkan ID produk yang ingin diupdate: ")
                    if not id_produk.isdigit():
                        print("Input ID harus angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_produk = int(id_produk)
                    if id_produk not in produk:
                        print("ID produk tidak ditemukan!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    data = produk[id_produk]
                    print(f"Update produk: {data['nama']}")
                    nama_baru = input("Nama baru (kosongkan jika tidak ingin diubah): ")
                    harga_baru = input("Harga baru (kosongkan jika tidak ingin diubah): ")
                    stok_baru = input("Stok baru (kosongkan jika tidak ingin diubah): ")

                    if nama_baru == "" and harga_baru == "" and stok_baru == "":
                        print("Produk tidak ada yang diupdate.")
                    else:
                        if nama_baru != "":
                            data["nama"] = nama_baru
                        if harga_baru.isdigit():
                            data["harga"] = int(harga_baru)
                        if stok_baru.isdigit():
                            data["stok"] = int(stok_baru)
                        print("Data produk berhasil diperbarui!")

                    input("Tekan Enter untuk kembali...")

                # Admin bisa hapus produk
                elif pilihan == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS PRODUK ===")
                    print("ID\tNama\t\t\tHarga\tStok")
                    print("-" * 50)
                    for idp, data in produk.items():
                        print(f"{idp}\t{data['nama']:<20}\tRp{data['harga']}\t{data['stok']}")
                    print("-" * 50)


                    id_produk = input("\nMasukkan ID produk yang akan dihapus: ")
                    if not id_produk.isdigit():
                        print("Input ID harus angka!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    id_produk = int(id_produk)
                    if id_produk in produk:
                        del produk[id_produk]
                        print("Produk berhasil dihapus!")
                    else:
                        print("ID produk tidak ditemukan!")
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

        # Menu ini adalah menu khusus user
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU USER ===")
                print("1. Lihat Produk")
                print("2. Logout")

                pilihan = input("Pilih menu: ")

                if pilihan == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR PRODUK ===")
                    print("ID\tNama\t\t\tHarga\tStok")
                    print("-" * 50)
                    for idp, data in produk.items():
                        print(f"{idp}\t{data['nama']:<20}\tRp{data['harga']}\t{data['stok']}")
                    print("-" * 50)
                    input("Tekan Enter untuk kembali...")

                elif pilihan == "2":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

    # Menu ini adalah khusus pengguna melakukan register, cuma ketika melakukan register, pengguna hanya bisa jadi user, tidak bisa jadi admin
    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        ada = False
        for data in users.values():
            if data["username"] == username:
                ada = True
                break

        if ada:
            print("Username sudah digunakan!")
        else:
            new_id = max(users.keys()) + 1 if users else 1
            users[new_id] = {"username": username, "password": password, "role": "user"}
            print("Akun berhasil dibuat!")

        input("Tekan Enter untuk kembali...")

    # Ini ketika pengguna ingin keluar
    elif menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan aplikasi Minimarket Muhammad Fajar.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")