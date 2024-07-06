import random
print('''
      ----------Array----------
      ''')
# array atau list biasanya dimulai dari 0 (index)
hobi = ["game", "film", "ngoding"]
#        [0]      [1]      [2]
r = random.randint(0,2)
print(hobi[r]) #mengunakan library
print(hobi[0])
print(hobi[4-2])  #bisa juga di tambah, kurang, kali,  bagi
print(len(hobi))  # untuk menghitung panjang array (menguakan bahasa manusia)
print('''
      ----------Temporeri Data----------
      ''')

hobis = ["game", "film", "ngoding"]
print(hobis)
tmp_hobis = hobis
tmp_hobis[2] = ('jus') #berfungsi untuk "memanipulasi" data
print(tmp_hobis)

posisi_kapten_curt = random.randint(1, 4)

bentuk_goa = "|_|"
jumlah_goa = [bentuk_goa] * 4
isi_goa = jumlah_goa.copy() # ini mengunakan copy agar isi utamanya tidak ikut berubah
isi_goa[posisi_kapten_curt - 1] = "|🐭|" # untuk mengisi array harus mengunakan []
isi_goa = " ".join(isi_goa) #ini untuk menghilangkan tanda array nya

print(f"denggan .join {isi_goa}")
print(f"tanpa .join {jumlah_goa}")
