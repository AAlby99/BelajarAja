import random

user = input("Masukan nama anda: ")
angka = random.randint(1, 100)
print(f"Halo {user} selamat datang di game tebak angka".title())
while True:
    isi = int(input("\nayo masukan angka: ".title()))
    if isi < angka:
        print("yah kurang tinggi angka nya ayo ulangi: ")
    elif isi > angka:
        print("yah kurang rendah angka nya ayo ulangi: ")
    elif isi == angka:
        print("Selamat, anda berhasil menebak angka!")
        break
        

