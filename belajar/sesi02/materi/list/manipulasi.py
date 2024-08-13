## Manipulasi LIST
buah = ["jeruk", "semangka","kiwi","nanas"] # list mengunakan index ya (-1 untuk mengambil dari belakang)


# mengambil data list
print(f"buah pada index ke 1 adalah {buah[1]}")
print(f"buah pada index ke -1 adalah {buah[-1]}")
print(40*"-")

#mengabil info jumlah data list
panjang = len(buah)
print(f"buah dalam kardus itu ada {panjang}")
print(40*"-")

# manipulasi data list
# Meambahkan item pada list sesuai posisi
buah.insert(2,'pisang') # menambah kan pisang pada list di posisi  ke 2 (dalam index (posisi, data))
print(buah)
buah.append("durian") # menambah data langsung di akhir
print(buah)
print(40*"-")
# Mengabungkan list dengan list
sayur = ['selada', 'kubis', 'sawi', 'wortel']
print(buah)
print(sayur)
buah.extend(sayur)
print(f"Gabungan antara List buah dan sayur {buah}")
print(40*"-")

# merubah data (data kiwi menjadi angur)
buah[3] = "angur"
print(buah)

# menghapus data / mendelete data dalam list 
buah.remove("nanas") # menghapus data nanas pada list
print(buah)
penghapusan = buah.pop() # menghapus data paling akhir
print(buah)
print("data uang di hapus adalah " + penghapusan)
## Catatan nama data harus sama persis