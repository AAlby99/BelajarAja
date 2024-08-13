def delete(db):
    print("----------------------------------------------------------------")
    user = input("Masukkan nama pemilik akun: ")
    alasan = (f"Akun dengan username: {user} telah di hapus dari sistem ini")
    konfirmasi = input(f"Apakah anda yakin ingin menghapus akun {user}? (y/n): ")
    if konfirmasi == "y":
        cursor = db.cursor()
        cursor.execute("DELETE FROM catatan WHERE nama=%s", (user,))
        cursor.execute("INSERT INTO history (username, history) VALUES (%s, %s)", (user, alasan))
        db.commit()
        print(f"Akun dengan username: {user} telah di hapus dari sistem ini")
        cursor.close()
    elif konfirmasi == "n":
        print("Penghapusan akun dibatalkan")
    else: 
        print("Gagal menghapus")