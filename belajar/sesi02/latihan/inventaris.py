def tambah_barang(inventaris, nama, jumlah, harga):
    inventaris[nama] = {'jumlah': jumlah, 'harga': harga}

def hapus_barang(inventaris, nama):
    if nama in inventaris:
        del inventaris[nama]
    else:
        print("Barang tidak ditemukan.")

def tampilkan_daftar_barang(inventaris):
    if not inventaris:
        print("Inventaris kosong.")
    else:
        for nama, data in inventaris.items():
            print(f"Nama: {nama}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']}")

def hitung_total_nilai_inventaris(inventaris):
    total_nilai = sum(data['jumlah'] * data['harga'] for data in inventaris.values())
    return total_nilai

def main():
    inventaris = {}
    while True:
        print("\nSelamat datang di sistem manajemen inventaris toko!")
        print("Pilih opsi:\n1. Tambah barang\n2. Hapus barang\n3. Tampilkan daftar barang\n4. Hitung total nilai inventaris\n5. Keluar")
        pilihan = input("Pilihan: ")

        if pilihan == '1':
            nama = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            harga = int(input("Masukkan harga per unit: "))
            tambah_barang(inventaris, nama, jumlah, harga)
            print("Barang berhasil ditambahkan!")
        elif pilihan == '2':
            nama = input("Masukkan nama barang yang akan dihapus: ")
            hapus_barang(inventaris, nama)
        elif pilihan == '3':
            tampilkan_daftar_barang(inventaris)
        elif pilihan == '4':
            total_nilai = hitung_total_nilai_inventaris(inventaris)
            print(f"Total nilai inventaris: {total_nilai}")
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
            
if __name__ == "__main__":
    main()
