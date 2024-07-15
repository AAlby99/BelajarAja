def edit(db):
    des = int(input("1. tambah\n2. kurang\npilih: "))
    if des == 1:
        pengedit = input("Masukan Nama Pengedit: ")
        dwt = int(input("Masukan Nominal Yang Ingin Ditambahkan: Rp."))
        nama = input("Masukan Nama Pemilik Uang: ")
        
        cursor = db.cursor()
        cursor.execute("SELECT uang FROM catatan WHERE nama=%s", (nama,))
        hasil_arto = cursor.fetchone()        
        if hasil_arto is not None:
            arto = hasil_arto[0]
            uang = float(dwt) + float(arto)
        else:
            print(f'{nama} Tidak ada dalam DataBase')
        
        cursor.execute("UPDATE catatan SET pengedit=%s, uang=%s WHERE nama=%s", (pengedit, uang, nama))
        db.commit()
        cursor.close()
        if cursor.rowcount > 0:
            print(f"{pengedit} berhasil Update data dan nominal Menjadi Rp.{uang}")
        else:
            print("gagal mengubah data")


    elif des == 2:
        pengedit = input("Masukan Nama Pengedit: ")
        dwt = int(input("Masukan Nominal Yang Ingin Dikurangi: Rp."))
        nama = input("Masukan Nama Pemilik Uang: ")
        
        cursor = db.cursor()
        cursor.execute("SELECT uang FROM catatan WHERE nama=%s", (nama,))
        hasil_arto = cursor.fetchone()        
        if hasil_arto is not None:
            arto = hasil_arto[0]
            uang = float(dwt) - float(arto)
        else:
            print(f'{nama} Tidak ada dalam DataBase')
            
        cursor.execute("UPDATE catatan SET pengedit=%s, uang=%s WHERE nama=%s", (pengedit, uang, nama))
        db.commit()
        if cursor.rowcount > 0:
            print(f"{pengedit} berhasil Update data dan nominal Menjadi Rp.{uang}")
        else:
            print("gagal mengubah data")
        cursor.close()  