import os
from Riwayat_Penjualan import riwayat_penjualan
from Rekursif_Penjualan import rekursif_penjualan

def tampil_penjualan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== LAPORAN PENJUALAN MINIMARKET MUHAMMAD FAJAR===")
    if not riwayat_penjualan:
        print("Belum ada transaksi.\n")
    else:
        keys = list(riwayat_penjualan.keys())
        rekursif_penjualan(keys)
        print(f"\nTotal keseluruhan: Rp{sum(riwayat_penjualan.values())}")
    input("Tekan Enter untuk kembali...")