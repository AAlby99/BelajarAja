from copy import deepcopy as dc

data = [10, 9 ,8]
data2 = [2, 1 ,0]

gabungori = [data, data2]
print(f"Semula: {gabungori}")

# mengunakan copy biasa
data = [10, 9 ,8]
data2 = [2, 1 ,0]
print(40*'-')

gabung = [data, data2]
gabung_copy = gabung.copy()
gabung_copy[0][0] = 15
print(f"Asli: {gabung}")
print(f"Copy: {gabung_copy}")
# hasilnya akan tetap berubah 2 2 nya
print(40*'-')

# menggunakan deepcopy
data = [10, 9 ,8]
data2 = [2, 1 ,0]
gabungg = [data, data2]
gabung_deepcopy = dc(gabungg)
gabung_deepcopy[0][0] = 13
print(f"Asli: {gabungori}")
print(f"Copy: {gabung_copy}")
print(f"DeepCopy: {gabung_deepcopy}")
print(40*'-')
print(f"ini Hexadesimal nya: {hex(id(gabungori))}")
print(f"ini Hexadesimal nya: {hex(id(gabung))}")
print(f"ini Hexadesimal nya: {hex(id(gabungg))}")

# deep copy bisa meng copy k=sampai ke dalam list sedangkan coppy biasa tidak 