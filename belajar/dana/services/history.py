def history(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM history")
    return cursor.fetchall()