#Program list Buku

library_kosong = []

while True:
    try:
        print("\nMenu Buku\n")
        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Lihat Buku v2")
        print("4. Keluar")
        
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
        
        if pilihan == 1:
            judul = input("Masukan Judul buku: ")
            penulis = input("Masukan Penulis buku: ")
            terbit = input("Masukan Tahun terbit: ")
            print("\ndata berhasil di input")
            
            buku = [judul, penulis, terbit]
            library_kosong.append(buku)
            
        elif pilihan == 2:
            [print(f"\njudul\t\t:{i[0]}\npenulis\t\t:{i[1]}\ntahun terbit\t:{i[2]}\n".title()) for i in library_kosong]
        elif pilihan == 3:
            print("no| judul|  penulis| terbit".title())
            for index,library in enumerate(library_kosong):
                print(f"{index} | {library[0]}|  {library[1]}| {library[2]}")
        elif pilihan == 4:
            print("Terima kasih sudah menggunakan program ini")
            break
        else:
            print("Pilihan tidak cocok")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")