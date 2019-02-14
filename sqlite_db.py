import sqlite3


conn = sqlite3.connect("lite.db")
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS something (item TEXT, quantity INTEGER, price REAL)')
conn.commit()
conn.close()