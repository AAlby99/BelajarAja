data = {
    "nama": "Ahmad Alby Rahmadani",
    "umur": 18,
    "hobi": "ngopi"
}

# panjang dictionary
LENDICT = len(data)  # rekomendasi mengunakan kapital semua jika mengunakan constant (data yang tidak berubah tetap)
print(f"panjang dari dictionary adalah: {LENDICT}")

print(40*'-')

# mengecek key ada atau tidak
KEY = "nama"
CHECKKEY = KEY in data
print(f"Apakah {KEY} ada di dalam data: {CHECKKEY} ")



print(40*'-')

# logika saya sendiri dari cek key
KEY = "umur"
CHECK = KEY in data
if CHECK == True: 
    print(f"{KEY} ditemukan di dalam data")
    print(f"Dan isi dari {KEY} = {data[KEY]}")
    
print(40*'-')
# mengakses value (read) dengan get
print(f"ini biasa {data['nama']}")
print(f"ini pake get {data.get('nama')}") # jika pke get mengunkana kurung () jika tidak pake []
print(f"ini pake get {data.get('kuy','key tidak ada')}") # jika pke get ini tidak akan error tapi outputnya bilang none atau apapun itu jika('key', 'pesan penganti none')

print(40*'-')

# meng update data
data['umur'] = 18

# menambah data (cara biasa)
data['fav'] = 'Die4U'
print(data)

print(40*'-')

# cara lebih efektif dan rekomendasi

data.update({'makanan':'mieayam'}) # jika ada di ganti jika tidak ada di tambah
print(data)

# ini untuk menghapus data nya
del data['fav']
print(data)