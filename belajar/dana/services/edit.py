def edit(db):
    des = int(input("\n1. tambah\n2. kurang\npilih: "))
    if des == 1:
        pengedit = input("Masukan Nama Pengedit: ")
        dwt = int(input("Masukan Nominal Yang Ingin Ditambahkan: Rp."))
        uangmasuk = input("Dapet transferan darimana nih boss??: ")
        nama = input("Masukan Nama Pemilik Uang: ")
        
        cursor = db.cursor()
        cursor.execute("SELECT uang FROM catatan WHERE nama=%s", (nama,))
        hasil_arto = cursor.fetchone()        
        if hasil_arto is not None:
            arto = hasil_arto[0]
            uang = int(dwt) + int(arto)
            uang = float(uang)

            
            cursor.execute("UPDATE catatan SET pengedit=%s, uang=%s WHERE nama=%s", (pengedit, uang, nama))
            db.commit()
            
            username = nama
            history = uangmasuk
            nominal = str(f"+{dwt}")
            total = uang
            cursor.execute("INSERT INTO history (username, history, nominal, total) VALUES (%s, %s, %s, %s)", (username, history, nominal, total))
            db.commit()
            if cursor.rowcount > 0:
                print(f'''
--------------------------------
{pengedit} berhasil menambah uang dengan nomilal +{dwt}, uang sebelumnya {arto} nominal menjadi Rp.{uang}0
--------------------------------------------------------'''
            )
            else:
                print("gagal mengubah data")
        else:
            print(f'''|---{nama} Tidak ada dalam DataBase---|''')
        cursor.close()


    elif des == 2:
        pengedit = input("Masukan Nama Pengedit: ")
        dwt = int(input("Masukan Nominal Yang Ingin Dikurangi: Rp."))
        uangkeluar = input("Kenapa di tarik bos..??: ")
        nama = input("Masukan Nama Pemilik Uang: ")
        
        cursor = db.cursor()
        cursor.execute("SELECT uang FROM catatan WHERE nama=%s", (nama,))
        hasil_arto = cursor.fetchone()        
        if hasil_arto is not None:
            arto = hasil_arto[0]
            uang = (int(dwt) - int(arto)) * -1
            uang = float(uang)
            
            cursor.execute("UPDATE catatan SET pengedit=%s, uang=%s WHERE nama=%s", (pengedit, uang, nama))
            db.commit()
            
            username = nama
            history = uangkeluar
            nominal = str(f"-{dwt}")
            total = uang
            cursor.execute("INSERT INTO history (username, history, nominal, total) VALUES (%s, %s, %s, %s)", (username, history, nominal, total))
            db.commit()
            if cursor.rowcount > 0:
                    print(f'''
--------------------------------
{pengedit} berhasil menarik uang dengan nomilal -{dwt}, uang sebelumnya {arto} nominal menjadi Rp.{uang}0
--------------------------------------------------------''')
            else:
                print("gagal mengubah data")
        else:
            print(f'''|---{nama} Tidak ada dalam DataBase---|''')
        cursor.close()  