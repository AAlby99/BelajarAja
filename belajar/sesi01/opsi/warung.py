import main
from services import db

def add():
    kode_barang = input("masukan id barang: ")
    nama_barang = input("masukan nama barang: ")
    harga_barang = int(input("masukan harga barang: "))
    stok_barang = int(input("masukan stok barang: "))
    
    
    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)

    
def cek():
    items = db.read_item()
    for item in items:
        kode_barang = item[1]
        nama = item[2]
        harga_barang = item[3]
        stok = item[4]
        print(f'''
              Kode-{kode_barang}
              Nama barang: {nama}
              Harga Barang: {harga_barang}
              Stok: {stok}
              ''')
    
def start():
    while True:
        menu = int(input('\nMENU \n1. Menambahkan Barang\n2. Cek Barang\n3. Keluar \n\n Silahkan pilih:  '))
        
        if menu == 1:
            add()
        elif menu == 2:
            cek()
        elif menu == 3:
            main.menu()
        else: 
            break

if __name__ == '__main__':
    start()