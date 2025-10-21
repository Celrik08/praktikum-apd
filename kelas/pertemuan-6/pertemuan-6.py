# buah = {"apel", "jeruk", "mangga", "apel"}
# buah = ([“apel”, “jeruk”, “mangga”, “apel”])

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"}
# }

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")

# print ("")
# print(f"nama saya adalah {Biodata("Nama")}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama"))

# print({Biodata.get("Aalamat")})

# Nilai = {
# "Matematika": 80,
# "B. Indonesia": 90,
# "B. Inggris": 81,
# "Kimia": 78,
# "Fisika": 80
# }

# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah

# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours":"Thriller"})

# #Setelah Ditambah
# print(Film)

# #Sebelum Diubah
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# # #Sebelum Dihapus
# # print(data)
# # del data["Nama"]
# # print(data)

# # cache = data.pop("Nama")
# # print(data)
# # print(cache)

# print("Jumlah Data = ", len(data))

# buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }


# pinjam1 = buku
# pinjam2 = buku.copy()

key = "apel", "jeruk", "mangga" 
 
value = 1 
 
buah = dict.fromkeys(key, value) 
 
print(buah) 

