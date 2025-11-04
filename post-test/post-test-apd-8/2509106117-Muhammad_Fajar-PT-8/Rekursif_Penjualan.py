from Riwayat_Penjualan import riwayat_penjualan

def rekursif_penjualan(keys, index=0):
    if index >= len(keys):
        return
    key = keys[index]
    print(f"Transaksi ke-{key}: Rp{riwayat_penjualan[key]}")
    rekursif_penjualan(keys, index + 1)