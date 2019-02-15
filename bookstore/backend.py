"""The backend code for a program that stores book information."""


import sqlite3


def connect_db():
    """Connect to database."""
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS book \
                   (id INTEGER PRIMARY KEY, title TEXT, \
                    author TEXT, year INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    """Insert a new book record."""
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO book VALUES (NULL,?,?,?,?)', (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    """View all books."""
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM book')
    rows = cursor.fetchall()
    conn.close()
    return rows


connect_db()
