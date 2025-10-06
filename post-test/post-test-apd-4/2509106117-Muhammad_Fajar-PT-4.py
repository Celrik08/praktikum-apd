while True:
    nim = input("Masukkan NIM Anda: ")

    if nim.isdigit(): 
        break
    else:
        print("Input tidak valid! Harap masukkan angka saja.\n")

# 1
stamina = int(nim[-3:])
chakra = 0

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print("\n=== Misi 1: Rasengan ===")
print(f"Chakra terkumpul: {chakra}")
print(f"Sisa stamina: {stamina}")
if chakra >= 200:
    print("Status: Naruto berhasil menyempurnakan Rasengan!")
else:
    print("Status: Naruto kehabisan stamina sebelum berhasil.")

# 2
tinggi_menara = int(nim[-2:])
gulungan = 0

for i in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print("\n=== Misi 2: Infiltrasi Menara ===")
print(f"Tinggi Menara: {tinggi_menara} meter")
print(f"Gulungan informasi yang dikumpulkan: {gulungan}")

# 3
jumlah_koridor = int(nim[-2])
intelijen = 0
perangkap = 0

if jumlah_koridor == 1:
    for ruangan in range(1, 4):
        jumlah_ruang = ruangan
        if jumlah_ruang % 2 == 1:
            intelijen += 1
        else:
            perangkap += 1
        
    print("\n=== Misi 3: Penyelidikan Markas ===")
    print(f"Jumlah koridor: {jumlah_koridor}")
    print(f"Jumlah Ruangan: {jumlah_ruang}")
    print(f"Data Intelijen ditemukan: {intelijen}")
    print(f"Perangkap Peledak dijinakkan: {perangkap}")
elif jumlah_koridor > 1:
    for ruangan in range(1, jumlah_koridor * 3 + 1):
        jumlah_ruang = ruangan
        if jumlah_ruang % 2 == 1:
            intelijen += 1
        else:
            perangkap += 1
    print("\n=== Misi 3: Penyelidikan Markas ===")
    print(f"Jumlah koridor: {jumlah_koridor}")
    print(f"Jumlah Ruangan: {jumlah_ruang}")
    print(f"Data Intelijen ditemukan: {intelijen}")
    print(f"Perangkap Peledak dijinakkan: {perangkap}")
else:
    print ("Angka adalah 0, atau angka tersebut minus")