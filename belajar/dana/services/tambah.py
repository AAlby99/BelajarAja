nama_global = None
def insert(db):
    print("----------------------------------------------------------------")   
    global nama_global 
    nama = input("\nMasukan Nama pemilik dana: ")
    pengedit = "Belum di edit"
    uang = float(input("Masukan Nominal yang ingin di tambahkan: Rp."))
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO catatan (nama, pengedit, uang) VALUES (%s, %s, %s)", (nama, pengedit, uang))
    db.commit()
    cursor.rowcount#buat ngasih tau baris mana yang di ubah ma user 
    if cursor.rowcount > 0:
        print(f"Berhasil mengubah data ke {cursor.rowcount}")
        print(f"Berhasil menambahkan data dari {nama} dengan nominal Rp.{uang}0")
    else:
        print("gagal mengubah data")    
    cursor.close()
    nama_global = nama
        
def newacc(db):
    username = nama_global
    history = "belum ada"
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO history (username, history) VALUES (%s, %s)", (username, history))
    db.commit()
    cursor.rowcount#buat ngasih tau baris mana yang di ubah ma user 
    if cursor.rowcount > 0:
        print(f"Selamat! akun baru dengan username {username} berhasil di buat")
    else:
        print("gagal mengubah data")  
        
def inp(db):
    insert(db)
    newacc(db)