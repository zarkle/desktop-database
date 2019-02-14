import psycopg2


def create_table():
    conn = psycopg2.connect('dbname="something" user="postgres" password="postgres123" host="localhost" port="5432"')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS something (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()
