angka = [2,3,1,3,1,9,2,3,1,3]

print(angka)

# count
jumlah_data_3 = angka.count(3)
print(f"jumlah angka 3 pada data di atas ada: {jumlah_data_3}")
jumlah_data_9 = angka.count(9)
print(f"jumlah angka 9 pada data di atas ada: {jumlah_data_9}")
print(40*"-")

# mengetahui posisi data (index)
buah = ["jeruk","kiwi", "semangka","nanas","kiwi", "apel"]

index_kiwi = buah.index("kiwi")
print(f"index kiwi ada di nomor: {index_kiwi}")
print(f"dan buah kiwi ada {buah.count("kiwi")}")
print(f"index jeruk ada di nomor: {buah.index("jeruk")}")
print(40*"-")

# sort (mengurutkan list)
# dari kecil ke besar
print(angka)
angka.sort() # ini mesin pengurutan nya
print(angka)
buah.sort() # harus di pisah tidak boleh di jadikan variable atau langsung di print nya
print(buah) 
print(40*"-")

# dari besar ke kecil
angka.reverse() # Catatan haruus sudah di sort dulu 
print(angka)
buah.reverse()
print(buah)
print(40*"-")
