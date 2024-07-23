def search(db):
    cursor = db.cursor()
    key = input("\nMasukkan nama pemilik akun: ")
    cursor.execute("SELECT nominal, history, tanggal, total FROM history WHERE username=%s", (key,))
    isidb = cursor.fetchall()

    if isidb:
        for data in isidb:
            nominal, history, tanggal, total = data
            print(f'''----------------------------------------------------------------
Pemilik {key}, dengan catatan: {history}
dan menarik/menambah uang sebanyak Rp.{nominal} di tambah uang yang ada menjadi Rp.{total}0 
pada {tanggal}
        ''')
    else:
        print("Data tidak ditemukan.")

    cursor.close()
