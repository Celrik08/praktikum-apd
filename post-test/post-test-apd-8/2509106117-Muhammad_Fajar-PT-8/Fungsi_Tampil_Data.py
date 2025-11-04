import os
from prettytable import PrettyTable
from Data_Produk import produk

def tampilkan_produk():
    os.system('cls' if os.name == 'nt' else 'clear')
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Harga", "Stok"]

    for idp, data in produk.items():
        table.add_row([idp, data["nama"], f"Rp{data['harga']}", data["stok"]])

    print("=== DAFTAR PRODUK MINIMARKET MUHAMMAD FAJAR ===")
    print(table)