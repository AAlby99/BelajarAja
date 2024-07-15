import mysql.connector
def konek():
    try: 
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_dana'
        )
        if db.is_connected():
            return db
    except mysql.connector.Error as err:
        print(f"Gagal Terkoneksi: {err}")
        return None


