# sesi pertama
nama = 'ahmad alby' #tipedata string kutip 1 '' kutip 2 ""sama
halo = 'halo semua nama ku '
usia = 18  #tipedata integer/int tidak perlu tanda ""
tinggi_badan =180.6 #2 kata mengunakan underscore  float mengunakan titik tidak bisa koma

print(halo + nama ,'usia saya ' + str(usia) + 'dan tinggi badan saya ' + str(tinggi_badan))
print("--------------------------------------------------------------------------------")
# sesi ke 2

# print(input("halo siapa nama kamu?? ")) #untuk meng input sesuatu mengunakan "input" bisa di letakkan di variabel
#contoh di varialbel
# tanya_nama = input('siapa namamu? ')
# print(tanya_nama)

#matematika py
#logic tanpa inputan user
a = 9
b = 90
c = a + b #hasil menyesuaikan
print(c)
#dengan inputan user

# s = input('masukkan angka : ')
# d = input('masukkan angka : ')
# h = int(s) + int(d) #harus mengunaka int
# q = int(s) - int(d)
# w = int(s) * int(d)
# z = int(s) / int(d)
# print("hasilnya adalah = " + str(h), " "+ str(q), " "+ str(w), " "+ str(z) )
print("--------------------------------------------------------------------------------")
#sesi ke 3

# string
namaku = "Ahmad alby rahmadani"
print(namaku.find('i'))
print(len(namaku))
print('a' in namaku)
print(namaku.upper()) #upper adalah fungsi jadi perlu ()
print(namaku.count('a')) #untuk menghitung jumlah huruf/kata

#perkondisian

# aseli = input('masukkan nama : ')
# umur = input("masukkan umur : ")
# if int(umur) > 50:
#     print("udah tuek")
# elif int(umur) >= 25:
#     print('usiamu sudah dewassa')
# elif int(umur) < 18:
#     print("halo " + aseli)
#     print("usiamu " + umur, "jadi tuh kamu masih bocil pesek iii sayang dehhh lopyuuu")
# elif int(umur) >= 18:
#     print("halo " + aseli)
#     print("usiamu " + umur, "jadi masih remaja ")

    # bisa juga mengunakan 'and' fungsinya adalah "diaantara" penganti >,>=,<=,< contoh
    # if int(umur) > 50 and int(umur) < 100:
    #     print("udah tuek")
print("--------------------------------------------------------------------------------")
#looping

#looping dengan for
negara = ['indonesia', 'inggris', 'singapura'] #perhitungan dimuali dari 0
print(negara)
print(negara[2])
for tetangga in negara: #perintah untuk membuat baris
    print(tetangga)
#looping dengan while
angka = 1
while angka <= 4:
    print(angka)
    angka += 1 #artinya sama dengan "angka = angka + 1"

print("-------------------------------TUGAS-------------------------------------")

saldo_awal = 1000000
deposit = input("masukkan depositnya: ")
hitung1 = saldo_awal + int(deposit)
hutang = 2500000
hitung2 = hitung1 - hutang


if hitung2 < 0:
    print("sisa hutang anda: " + str(hitung2) + " cepat bayar hutang anda")
else:
    print("saldo anda: " + str(hitung2) +(" ayo hutang lagi biar kami untung"))
