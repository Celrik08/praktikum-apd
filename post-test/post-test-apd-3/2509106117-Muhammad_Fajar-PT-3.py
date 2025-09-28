print("=== Penghitung Gaji Karyawan PT. BOM ===")
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (peracik/pengantar): ").lower()
hari_kerja = int(input("Masukkan jumlah hari kerja: "))
jam_kerja = int(input("Masukkan jumlah jam kerja per hari: "))
lembur = int(input("Masukkan jumlah lembur: "))

if jabatan == "peracik":
    if hari_kerja >= 24 and jam_kerja >= 8 and lembur >= 4:
        bayaran_perjam = 25000
        bayaran_lembur = 15000
    elif hari_kerja >= 18 and jam_kerja >= 6 and lembur >= 2:
        bayaran_perjam = 20000
        bayaran_lembur = 10000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 10000

elif jabatan == "pengantar":
    if hari_kerja >= 20 and jam_kerja >= 7 and lembur >= 7:
        bayaran_perjam = 25000
        bayaran_lembur = 20000
    elif hari_kerja >= 16 and jam_kerja >= 5 and lembur >= 4:
        bayaran_perjam = 20000
        bayaran_lembur = 15000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 12000
else:
    print("Jabatan tidak dikenali, gaji tidak bisa dihitung.")
    exit()

total_gaji = ((bayaran_perjam * jam_kerja) * hari_kerja) + (lembur * bayaran_lembur)

print("\n=== Hasil Perhitungan Gaji ===")
print(f"Nama Karyawan     : {nama}")
print(f"Jabatan           : {jabatan.capitalize()}")
print(f"Hari Kerja        : {hari_kerja} hari")
print(f"Jam Kerja         : {jam_kerja} jam/hari")
print(f"Jumlah Lembur     : {lembur} kali")
print(f"Bayaran Per Jam   : Rp{bayaran_perjam:,}")
print(f"Bayaran Lemburan  : Rp{bayaran_lembur:,}")
print(f"Total Gaji        : Rp{total_gaji:,}")