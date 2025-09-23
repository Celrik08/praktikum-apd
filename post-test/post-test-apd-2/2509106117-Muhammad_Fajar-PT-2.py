import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        nama_pelanggan = input("Masukkan Nama Pelanggan: ").strip()
        if nama_pelanggan.replace(" ", "").isalpha():
            print("\n")
            break

    harga_bata = 100
    harga_semen = 100000

    while True:
        jumlah_bata_input = input("Masukkan jumlah batu bata yang akan dibeli: ")
        if jumlah_bata_input.isdigit():
            jumlah_batu_bata = int(jumlah_bata_input)
            total_bata = harga_bata * jumlah_batu_bata
            print(f"Total harga batu bata: Rp {total_bata:,}\n")
            break

    while True:
        jumlah_semen_input = input("Masukkan jumlah karung semen yang akan dibeli: ")
        if jumlah_semen_input.isdigit():
            jumlah_semen = int(jumlah_semen_input)
            total_semen = harga_semen * jumlah_semen
            print(f"Total harga semen: Rp {total_semen:,}\n")
            break

    total_awal = total_bata + total_semen
    print(f"Total Biaya Awal Sementara: Rp {total_awal:,}\n")

    if jumlah_batu_bata == 500 and jumlah_semen == 5:
        diskon_persen = 0.15
        keterangan_diskon = "Paket Hemat (15%)"
        print("Selamat Anda Mendapatkan Diskon 15%\n")
    elif jumlah_batu_bata == 2000 and jumlah_semen == 16:
        diskon_persen = 0.30
        keterangan_diskon = "Paket Ultra Mantap (30%)"
    else:
        diskon_persen = 0
        keterangan_diskon = "Tidak Ada Diskon"

    jumlah_diskon = total_awal * diskon_persen
    total_akhir = float(total_awal - jumlah_diskon)

    print("="*42)
    print("        ESTIMASI BIAYA BAHAN BANGUNAN")
    print("="*42)
    print(f"Nama Pelanggan: {nama_pelanggan}")
    print("-"*57)
    print("| Barang     | Jumlah | Harga Satuan      |")
    print("-"*57)
    print(f"| Batu Bata  | {str(jumlah_batu_bata).ljust(6)} | Rp{harga_bata:<15}|")
    print(f"| Semen      | {str(jumlah_semen).ljust(6)} | Rp{harga_semen:<15}|")
    print("-"*57)
    print(f"Total Biaya Awal               : Rp {total_awal:,}")
    print(f"Diskon yang Didapat            : {keterangan_diskon}")
    print(f"Jumlah Diskon                  : Rp {int(jumlah_diskon):,}")
    print("-"*57)
    print(f"TOTAL BIAYA AKHIR : Rp {int(total_akhir):,}")
    print("="*42)

    lanjut = input("\nApakah Anda ingin melanjutkan program? (y/n): ").lower()
    if lanjut != "y":
        break