a = [1,2]
b = [3,4]

list_biasa = [1,2,3,4]
print("list biasa",list_biasa)
print(40*'-')

# Membuat list baru yang menggabungkan list a dan b
list_gabung = [a,b]
print("list gabung",list_gabung)
print(40*'-')

# cara mengambil data
ambil1 = list_gabung[0]
print(f"mengambil data dalam 1 list: {ambil1}")
ambil2 = list_gabung[0][0] # [ambil list] [ambil dlam list]
print(f"mengambl data lebih spesifik {ambil2}")
print(40*'-')

# Membuat kist kombinasi
list_kombinasi = [a,b, 6,"au"]
print("list kombinasi",list_kombinasi)
print(40*'-')

# study kasus
data = ['Alby', 18, 'Laki laki', 'Donomerto']
data2 = ['Havila', 16, 'Perempuan', 'Kalibogor']
data3 = ['Da Vincci', 59, 'Laki laki', 'Prancis']

anggota = [data , data2 , data3]

for member in anggota:
    print(f'Nama angota: {member[0]}')
    print(f'Usia angota: {member[1]}')
    print(f'Jenis kelamin angota: {member[2]}')
    print(f'Tempat tinggal angota: {member[3]}\n')
    print(40*'-')