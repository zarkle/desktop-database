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
