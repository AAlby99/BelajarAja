from services.koneksi import konek
from services.edit import edit
from services.tambah import insert
from services.lihat import see
from services.keluar import keluar

def liat():
    connect = konek()
    try:
        hasil_query = see(connect)
        for data in hasil_query:
            nama = data[1]
            pengedit = data[2]
            uang = data[3]
            print(f'''
                Pemilik {nama} yang terakhir mengedit data ini adalah {pengedit}
                            dan memiliki uang sejumlah Rp.{uang}0
                ''')
                
    finally:
        connect.close()
        
def start():
    connect = konek()
    if connect is None:
        print("Gagal menghubungkan ke database. Periksa kembali konfigurasi koneksi Anda.")
        return
    while True:
        print("\n\nHalo Selamat datang silakan pilih salah satu (takan 0 untuk berhenti)")
        pilihan = int(input("1. Menambah\n2. Edit\n3. Lihat\nPilih: "))
        if pilihan == 1:
            insert(connect)    
        elif pilihan == 2:
            edit(connect)
        elif pilihan == 3:
            liat()
        elif pilihan == 0:
            keluar()
            break
        else:
            print("error")
            keluar()
            break
        
if __name__ == "__main__":
    start()