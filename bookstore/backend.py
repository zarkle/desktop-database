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


def search(title=None, author=None, year=None, isbn=None):
    """Search books."""
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM book WHERE title=? OR author=? \
        OR year=? OR isbn=?', (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete(id):
    """Delete a book record."""
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM book WHERE id=?', (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    """Update a book record."""
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE book SET title=?, author=?, year=?, \
        isbn=? WHERE id=?', (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect_db()
