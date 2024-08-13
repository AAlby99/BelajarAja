nama_global = None

def insert(db):
    print("----------------------------------------------------------------")   
    global nama_global 
    try:
        nama = input("\nMasukan Nama pemilik dana: ")
        pengedit = "Belum di edit"
        uang = int(input("Masukan Nominal yang ingin di tambahkan: Rp."))
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO catatan (nama, pengedit, uang) VALUES (%s, %s, %s)", (nama, pengedit, uang))
        db.commit()
        cursor.rowcount#buat ngasih tau baris mana yang di ubah ma user 
        if cursor.rowcount > 0:
            print(f"Berhasil mengubah data ke {cursor.rowcount}")
            print(f"Berhasil menambahkan data dari {nama} dengan nominal Rp.{uang:,.2f}")
        else:
            print("gagal mengubah data")    
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        cursor.close()
        nama_global = nama
        
def newacc(db):
    username = nama_global
    history = "belum ada"
    
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO history (username, history) VALUES (%s, %s)", (username, history))
        db.commit()
        cursor.rowcount#buat ngasih tau baris mana yang di ubah ma user 
        if cursor.rowcount > 0:
            print(f"Selamat! akun baru dengan username {username} berhasil di buat")
        else:
            print("gagal mengubah data")  
    except Exception as e:
        print(f"Error: {str(e)}")
        
def inp(db):
    insert(db)
    newacc(db)