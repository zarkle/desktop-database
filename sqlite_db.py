import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS something (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO something VALUES (?, ?, ?)', (item, quantity, price))
    conn.commit()
    conn.close()

insert("Water Glass", 10, 5)