from services.koneksi import konek as terkoneksi
from services.edit import edit
from services.tambah import inp 
from services.lihat import see
from services.keluar import keluar
from services.cari import search
from services.history import history
from services.hapus import delete

def liat():
    connect = terkoneksi()
    try:
        hasil_query = see(connect)
        for data in hasil_query:
            nama = data[1]
            pengedit = data[2]
            uang = data[3]
            print(f'''----------------------------------------------------------------
Pemilik {nama}, yang terakhir mengedit data ini adalah {pengedit}
dan memiliki uang sejumlah Rp.{uang}0''')
                
    finally:
        connect.close()
def penjelajahan():
    connection = terkoneksi()
    try:
        jejak = history(connection)
        for a in jejak:
            print(f'''----------------------------------------------------------------
Username: {a[1]},
History : {a[2]} 
Tanggal : {a[5]}
Nominal : {a[3]}
Sisa    : {a[4]} ''')
            
    finally:
        connection.close()
        
def start():
    connect = terkoneksi()
    if connect is None:
        print("Gagal menghubungkan ke database. Periksa kembali konfigurasi koneksi Anda.")
        return
    while True:
        print("\n\nHalo Selamat datang silakan pilih salah satu (takan 0 untuk berhenti)")
        pilihan = int(input("1. Menambah\n2. Edit\n3. Lihat\n4. Cari\n5. History\n6. Hapus Akun\nPilih: "))
        if pilihan == 1:
            inp(connect)    
        elif pilihan == 2:
            edit(connect)
        elif pilihan == 3:
            liat()
        elif pilihan == 4:
            search(connect)
        elif pilihan == 5:
            penjelajahan()
        elif pilihan == 6:
            delete(connect)
        elif pilihan == 0:
            keluar()
            break
        else:
            print("error")
            keluar()
            break
        
if __name__ == "__main__":
    start()