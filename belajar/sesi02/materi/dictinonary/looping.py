guest = {
    'a':'ara',
    'b':'bella',
    'c':'callie',
    'd':'diana'
}

# looping secara umum dan hanya mengambil key nya saja
for t in guest:
    print(t)
    
# cara yang lebih rekomendasi (untuk mengambil key nya)
kunci = guest.keys()
print(f'hasil key: {kunci}') # hasilnya adalah key nya
for key in guest.keys():
    print(key) # hasilnya adalah key juga tapi tidak ada tulisan dict_keysnya
print(40*'-')

# operator untuk mengambil itemnya (iterebels) / value nya (buat ngambil value nya)
for isi in guest.keys():
    print(guest.get(isi))
    
value = guest.values()
print(value) # hasilnya ada dictionarynya
# cara rekomendasi
for value in guest.values():
    print(value) # menghilangkan dictionarynya
print(40*'-')

# operator items (ubtuk ambil 2 2 nya)

aitem = guest.items()
print(aitem) # hasil nya ada key nya dan ada value nya dan juga ada dictionarynya

for ai in guest.items():
    print(ai) # hasil nya ada
print(40*'-')

# ngambil kek items tapi lebih elegan kayak pake enumerate

for key,value in guest.items():
    print(f'key: {key} value: {value}')


#   KESIMPULAN berbagai cara untuk mengambil data dari dictionary