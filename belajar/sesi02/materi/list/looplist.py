# Looping list and enumerate

# for loop (cara singkat nya)
kumpulan_angka = [2,4,8,0,5,3,2]
for angka in kumpulan_angka:
    print(f'angka {angka}')

print(40*'-')

# for loop dan range (cara panjang nya)

kumpulan_angka = [2,4,8,0,5,3,2]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f'angka {kumpulan_angka[i]}')

print(40*'-')
# while loop (cara sangat panjang tidak rekomendasi)
kumpulan_angka = [2,4,8,0,5,3,2] 
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f'angka {kumpulan_angka[i]}')
    i += 1

print(40*'-')
# list comprehension (paling cepet)

kumpulan_angka = [2,4,8,0,5,3,2]
[print(f'angka: {i}') for i in kumpulan_angka]

print("\n overall hasilnya tetap sama tetapi beda cara aja ")

# enumerate (menampilkan index dan datanya)

kumpulan_angka = [2,4,8,0,5,3,2]
for index,data in enumerate(kumpulan_angka):
    print(f"index: {index}, data: {data}")

# membuat kuadrat
kumpulan_angka = [2,4,8,0,5,3,2]

kuadrat = [i**2 for i in kumpulan_angka]

print(f"ini adalah hasil dari kuadrat: {kuadrat}")