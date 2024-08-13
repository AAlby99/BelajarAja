# default argument 
def usia(umur = 18):
    us = umur
    return us

s = usia()
print(f"usia saya {s}")  # harna argument nya kosong jadi sistem mengkonfrensi umur menjadi default atau di sebelah sama dengan

u = usia(79)
print(f"usia saya {u}")

print(60*'-')

# jika 2 argument

def katakan(nama = 'anonimusus', kata = 'tak ada kata kata'):
    print(f"{nama} menyebut {kata}")

katakan("Alby", "hello")
katakan('risma')
katakan( kata='kiuy') 

print(60*'-')

def hitung(angka1 = 1, angka2 = 2, angka3 = 3, angka4 = 4, angka5 = 5, angka6 = 6):
    proses = angka1 + angka2 + angka3 + angka4 + angka5 + angka6
    return(proses)

print(hitung())
i = int(input("aa"))
print(hitung(angka6= i)) 
# kita juga bisa meng akses argumen ke 2 nya mengunakan nama argument lalu di '=' ini berlaku jika ada defaultnya doang jika tidak tidak bisa


