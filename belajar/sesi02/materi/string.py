print('-------string-------')
data = "ini adalah string"  # bisa mengunakan "" atau ''
print(data)
print(type(data))

print('hari ini adalah hari jum\'at')  # mengunakan tanda backslash \ untuk menampilkan jika mengunakan quotes 1 ('') merubah ' menjadi str
print("C:\\user\\alby")  # jika back slash ingin di cetak didalam print
print("hello\t world")  # \t menggunakan tab
print("hello \bworld")  # \b untuk backspace

print("hello \nworld")  # \n untuk enter (LF = line feed) dipake oleh unix, macos, linux
print("--------------------------------------------------------")
print("hello\rworld")  # \r untuk enter (CR = carriage return) dipake oleh commidrone, acorn,  lisp
print("--------------------------------------------------------")
print("hello\r\nworld")  # \r\n untuk enter (CRLF = line feed carriage return) dipake oleh windows

print(r"C:\new folder")  # r"" akan membuat semua yang ada di dalamnya menjadi string (raw string)
print('''Tiga biji tau lah ya ''')

print(f"tau juga lah ya klo f\n")

print("-------operasi string-------")
a = "halo "
b = "its me "
c = "again"
d = a + b + c
print(d)

panjang = len(d)  # untuk menghitung panjang str
print(panjang)
e = "a"
status = e in d  # mengecek apa kah ada "a" didalam variable d
print(status)
status = e not in d  # mengecek apa kah ada "a" didalam variable d
print(status)

print("--"*10)  # string di kali 10

print("index ke -0: " + d[0])  # (index di mulai dari 0) gunanya indexing di str untuk mengambil nilai yang telah di tentukan di dalam []
print("index ke -2: " + d[-2])  # sama aja tapi ngambil dari belakang
print("index ke -[0-2]: " + d[0:3])  # sama aja tapi ngambil dari data ke 0 sampai ke 2 (di situ sebelum 3)
print("index ke -[0-10]: " + d[0:11:2])  # sama aja tapi ngambil dari data ke 0 sampai ke 10 dengan loncatan 2X

# item paling kecil
print("paling kecil: (spasi)" + min(d))
# item paling besar
print("paling besar: " + max(d))

# ascii code
a = ord('a')
print("ascii code: " + str(a))
b = 117
print("ascii code: " + chr(b))


# operator dalam bentuk method====================

data = "ahmad alby rahmadani"
jumlah = data.count("a")
print("\njumlah a dalam data : " + str(jumlah))

# merubah case dari string
data = "Halo Indonesia"
print("Normal case: " + str(data))
data = data.lower()
print("Lower case: " + str(data))
data = data.upper()
print("Upper case: " + str(data))
judul = "the last of us\n"
title = judul.title()
print("ini adalah judul: " + str(title))

# pengecekan mengunakan isX method
soalan = "HALO"
apakah_lower = soalan.islower()  # hasilnya boolean
print(soalan + " Apakah lower case: " + str(apakah_lower))
apakah_upper = soalan.isupper()  # hasilnya boolean
print(soalan + " Apakah upper case: " +  str(apakah_upper))
judul = "The Last Of us"
title = judul.istitle()
print("mengecek apakah ini adalah judul: " + str(title))  # semua depanya harus besar jika kecil salah satu tetap jadi false

# CONTOH
# isalpha = untuk mengecek semuanya adalah huruf
# isalnum = untuk mengecek semuanya adalah angka dan huruf
# isdecimal = untuk mengecek semuanya adalah angka saja
# isspace = untuk mengecek semuanya adalah spasi, tab, newline
# istitle = untuk mengecek huruf depan adalah huruf besar

# ngecek komponen
cek_start = "Kuala University".startswith("Kuala")  # bisa di jadikan literal methodnya
print(cek_start)
cek_end = "Kuala University".endswith("University")
print(cek_end)
salah = "Kuala University".endswith("kuala")
print(salah)

# pengabungan komponen join & split
pisah = ['pisang','anggur','rambutan']  # ini adalah list
print(pisah)
gabung = '-.-'.join(pisah)
print(gabung)
split = gabung.split('-.-')  # menghilangkan komponen nyang ada i dalam tanda kurung dan membuat dia menjadi list lagi
print(split)

# justify rjust(), ljust(), center()
rjust ='hirosima'.rjust(10)  # dalam kurung menentukan panjang justify nya
print("'"+rjust+"'")
ljust = 'hirosima'.ljust(10) 
print("'" + ljust + "'")
center = 'tengah'.center(10)
print("'"+center+"'")
center = 'tengah'.center(30,"_")  # tambahkan argumen lagi untuk menganti agar bukan spasi
print("'"+center+"'")
center = 'tengah'.strip("_")  # menghilangkan justify
print("'"+center+"'")

# width and multiline
# data
nama = "alby"
ummur = 18
tinggi = 180

# string standart
biodata = f"nama: {nama}, usia: {ummur}, tinggi badan: {tinggi}".title()
print(5*"-"+"biodata saya"+5*"-")
print(biodata)

# string multiline
biomulti = f"nama: {nama}, \nusia: {ummur}, \ntinggi badan: {tinggi}".title()
print(biomulti)

# mengatur lebar
print(f'''
nama saya   : {nama:>10}
usia saya   : {ummur:<5} 
tinggi saya : {tinggi:^10}

''')