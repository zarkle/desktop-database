"""The backend code for a program that stores book information."""


import sqlite3


def connect_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS book
                   (id INTEGER PRIMARY KEY, title TEXT,
                    author TEXT, year INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()


connect()
