print("Halo ini sesi pertama dari belajar python")

print("materi 1 variabel")
nama = "Ahmad Alby Rahmadani"
umur = 18

print(nama + str(umur))


print('''
     single tripel kuots
 tombol enter
        
      berfungsi sebnarnya
      ''')
print(f'''
      untuk menambahkan variable mengunakan f di awal bisa digunakan di print mana saja
      {nama}
      {umur}
      ''')

print("---------------if else---------------------")
user = input("masukan nama anda: ")
usiauser = input("masukan usia anda: ")

while user == '':
    user = input('isi nama mu dulu ya:  ''')
while usiauser == '':
    usiauser = input('umur mu di isi:  ''')
if int(usiauser) >= 0 and int(usiauser) <= 10:
      print(f'''            halo {user}        
      wahhh masih bayi ya kalian belom boleh main :)''')
elif int(usiauser) >= 11 and int(usiauser) <= 17:
      print(f'''            halo {user}          
            wahhh bocil lagii nihh yakin mau main? nanti jadi beban loh >_ ''')
elif int(usiauser) >= 18 and int(usiauser) <= 30:
      print(f'''             halo {user}    
      wahhh akhirnya kembali ayo masa remaja kamu jangan di sia" kan main kan game ini sepuasnya <3           
            ''')
elif int(usiauser) < 0 :
      print(f'''             hey {user}  
      kamu sehat??
            ''')
else:     
      print(f'''             halo {user} 
      yakin masih ingin main game ini kamu sudah tua loh -_-        
            ''')