print('''
      ----------Looping-----------''')
buah = "pisang🍌"
mulai = 0
akhir = 5

while mulai < akhir:
    print(buah)
    mulai += 1

print('''
      ---------Functions----------''')
def tambah(x, y):
    return x + y

from libr import tiga, isi
print(tambah(2 , 4))
print("funtion dari file lain")
tiga()
print("jika ada isian")
isi(9,2)