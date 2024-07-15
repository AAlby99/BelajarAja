def insert(db):    
    nama = input("masukan Nama pemilik dana: ")
    pengedit = "Belum di edit"
    uang = float(input("masukan Nominal yang ingin di tambahkan: Rp."))
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO catatan (nama, pengedit, uang) VALUES (%s, %s, %s)", (nama, pengedit, uang))
    db.commit()
    cursor.rowcount#buat ngasih tau baris mana yang di ubah ma user 
    if cursor.rowcount > 0:
        print(f"berhasil mengubah data ke {cursor.rowcount}")
        print(f"berhasil menambahkan data dari {nama} dan nominal Rp.{uang}")
    else:
        print("gagal mengubah data")    
    cursor.close()
