import os
from InquirerPy import inquirer
from Login_User import login_user
from Data_User import users
from Fungsi_Tampil_Data import tampilkan_produk
from Tambah_Produk import tambah_produk
from Ubah_Produk import ubah_produk
from Hapus_Produk import hapus_produk
from Tampil_Penjualan import tampil_penjualan
from Beli_Produk import beli_produk

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        pilihan = inquirer.select(
            message="=== MINIMARKET MUHAMMAD FAJAR ===",
            choices=["Login", "Register", "Keluar"],
            qmark="",
            instruction=None
        ).execute()

        if pilihan == "Login":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("SILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA")
            username = input("Username: ")
            password = input("Password: ")
            user = login_user(username, password)

            if user is None:
                print("Username atau password salah!")
                input("Tekan Enter untuk kembali...")
                continue

            print(f"Login berhasil! Selamat datang, {user['role'].capitalize()} {user['username']}")
            input("Tekan Enter untuk lanjut...")

            if user["role"] == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pilih = inquirer.select(
                        message="===ANDA MASUK MENU ADMIN ===",
                        choices=["Lihat Produk", "Tambah Produk", "Ubah Produk", "Hapus Produk", "Laporan Penjualan", "Logout"],
                        qmark="",
                        instruction=None
                    ).execute()

                    if pilih == "Lihat Produk":
                        tampilkan_produk(); input("Tekan Enter...")
                    elif pilih == "Tambah Produk":
                        tambah_produk()
                    elif pilih == "Ubah Produk":
                        ubah_produk()
                    elif pilih == "Hapus Produk":
                        hapus_produk()
                    elif pilih == "Laporan Penjualan":
                        tampil_penjualan()
                    elif pilih == "Logout":
                        break

            else:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pilih = inquirer.select(
                        message="=== ANDA MASUK MENU USER ===",
                        choices=["Lihat Produk", "Beli Produk", "Logout"],
                        qmark="",
                        instruction=None
                    ).execute()

                    if pilih == "Lihat Produk":
                        tampilkan_produk(); input("Tekan Enter...")
                    elif pilih == "Beli Produk":
                        beli_produk()
                    elif pilih == "Logout":
                        break

        elif pilihan == "Register":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== SILAHKAN REGISTER AKUN BARU ANDA===")
            username = input("Masukkan username: ").strip()
            password = input("Masukkan password: ").strip()

            if not username or not password:
                print("Username dan password tidak boleh kosong!")
                input("Tekan Enter untuk kembali ke menu utama...")
                continue

            if any(u["username"] == username for u in users.values()):
                print("Username sudah digunakan!, Silahkan buat Username baru")
            else:
                new_id = max(users.keys()) + 1 if users else 1
                users[new_id] = {"username": username, "password": password, "role": "user"}
                print("Akun berhasil dibuat!")

            input("Tekan Enter untuk kembali...")

        elif pilihan == "Keluar":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terima kasih sudah menggunakan aplikasi Minimarket Muhammad Fajar.")
            break

if __name__ == "__main__":
    main()