
def see(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM catatan")
    return cursor.fetchall()


