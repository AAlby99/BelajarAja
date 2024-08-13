# def = definition
#  "wkwk" = nama function nya
# (masukan sesuatu di dalam kurung ini) = namanya argumen/parameter jika ada di dalam kurung

# def wkwk(argumen):
#     badan fungsi


# contoh
def halo(nama): #function helo menerima input dengan variable 'nama'
    print(f"halo nama ku {nama}")
    
halo('alby')


# JADI 'nama' yang ada di dalam badan fungction itu di tangkep ke def halo(nama)nah di tangkep di 'nama' itu lalu si nama di isi oleh pemangil 
# yaitu halo('alby) JADI ALBY di kirim ke def lalu def di kirim ke badan fungction

#contoh lain

def tambah_dua_angka(pertama, kedua):
    hasil = pertama + kedua
    print(f'jadi {pertama} + {kedua} = {hasil}')

tambah_dua_angka(3,  2) 

# Contoh pake input

def pp(keren):
    print(f'woi nama gua {keren}'.title())

jeneg = input('nama: ')

pp(jeneg)

# contoh pake list

def buah(enaku):
    enaku[1]
    kumpulan_buah = enaku.copy()
    for kk in kumpulan_buah:
        print(f'ada buah: {kk}')
        
keranjang = ['semangka', 'jeruk', 'pisang']

print("aku punya buah: ")
buah(keranjang) # apapun nama  di dalam kurungnya jika sudah dikirim ke def maka namanya akan terubah seperti di def 
# cara kasarnya gini "apapun yang kita asukin akan menjadi argumen def itu sendiri"
print(f'buah favoritku {keranjang[1]}')