# tanggal dan waktu
import datetime as tanggal
# Membuat objek tanggal

hari_ini = tanggal.date.today()

print(f"hari ini adalah hari {hari_ini:%A}")

ulang_tahun = tanggal.date(2006, 2, 10)

print(f"hari ulang tahun alby pada hari: {ulang_tahun:%a}") #a kecil untuk di singkat a besar untuk panjang hari

hari = int(input("masukan tangal lahir anda(ymd): "))
bulan = int(input("bulan lahir: "))
taun = int(input("taun lahir: "))
deteksi = hari, bulan, taun

hari = tanggal.date(taun, bulan, hari)
print(f"ytanggal lahir anda: {hari} di hari {hari:%A} ")

bdayi = hari_ini - hari
bday = bdayi.days // 365 #.days untuk agar menjdi hari bukan date lagi
bulan = (bdayi.days % 365) // 30
print(f"umur saya: {bday} tahun {bulan} bulan")