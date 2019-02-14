import psycopg2


def create_table():
    conn = psycopg2.connect('dbname="something" user="postgres" password="postgres123" host="localhost" port="5432"')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS something (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect('dbname="something" user="postgres" password="postgres123" host="localhost" port="5432"')
    cur = conn.cursor()
    cur.execute('INSERT INTO something VALUES(%s, %s, %s)', (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect('dbname="something" user="postgres" password="postgres123" host="localhost" port="5432"')
    cur = conn.cursor()
    cur.execute('SELECT * FROM something')
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect('dbname="something" user="postgres" password="postgres123" host="localhost" port="5432"')
    cur = conn.cursor()
    cur.execute('DELETE FROM something WHERE item=%s', (item,))
    conn.commit()
    conn.close()
