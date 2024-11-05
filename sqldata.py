from sqlite3 import Connection

conn = Connection("Data.db")
c= conn.cursor()

def default():
    c.execute("CREATE TABLE IF NOT EXISTS taxies (user_id, name, phone)")
    conn.commit()

def add_taxi(user_id, name, phone):
    c.execute("INSERT INTO taxies VALUES (?, ?, ?)", (user_id, name, phone))
    conn.commit()

def get_taxi(id):
    return c.execute("SELECT * FROM taxies WHERE user_id=?", (id, )).fetchone()

def close_db():
    conn.close()

default() 
