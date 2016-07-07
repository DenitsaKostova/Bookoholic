import sqlite3
import string
from settings import *


def execute_query(query):
    connection = sqlite3.connect("../" + DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


def is_query_passing(query):
    connection = sqlite3.connect("../" + DATABASE_NAME)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        connection.close()
        return True
    except:
        return False


def add_dummy_entry():
    query = "INSERT INTO " + TABLE_NAME + " VALUES('123-456-789',\
                                          'Harry Potter', 'J.K.Rowling',\
                                          1997, 'Fantasy', 4,\
                                          'I liked it vary much', 'read')"
    execute_query(query)


def add_entry(isbn, title, author, year, genre, rating, review, status):
    query = "INSERT INTO " + TABLE_NAME + " VALUES(" + \
            "'{}','{}','{}',{},'{}',{},'{}','{}')"\
            .format(isbn, title, author, year, genre, rating, review, status)
    return execute_query(query)


def add_book(book):
    return add_entry(book.isbn, book.title, book.author, book.year,
              book.genre, book.rating, book.review, book.status)


def select_isbn_column():
    query = "SELECT isbn FROM " + TABLE_NAME
    return execute_query(query)


def select_by_isbn(isbn):
    query = "SELECT * FROM " + TABLE_NAME + " WHERE isbn='{}'".format(isbn)
    return execute_query(query)


def select_by_title(title):
    query = "SELECT * FROM " + TABLE_NAME + " WHERE title='{}'".format(title)
    return execute_query(query)


def select_by_author(author):
    query = "SELECT * FROM " + TABLE_NAME + " WHERE author='{}'".format(author)
    return execute_query(query)


def select_by_genre(genre):
    query = "SELECT * FROM " + TABLE_NAME + " WHERE genre='{}'".format(genre)
    return execute_query(query)


def select_by_status(status):
    query = "SELECT * FROM " + TABLE_NAME + " WHERE status='{}'".format(status)
    return execute_query(query)


def update_entry(title, rating, review, status):
    query = "Update " + TABLE_NAME + " SET rating={}, review='{}', status='{}'"\
            .format (rating, review, status) + " WHERE title='{}'".format(title)
    return is_query_passing(query)


def delete_by_isbn(isbn):
    query = "Delete FROM " + TABLE_NAME + " WHERE isbn='{}'".format(isbn)
    return execute_query(query)


def delete_by_title(title):
    query = "Delete FROM " + TABLE_NAME + " WHERE title='{}'".format(title)
    return execute_query(query)


def delete_all():
    return is_query_passing("Delete from " + TABLE_NAME)


def select_all():
    query = "Select * from " + TABLE_NAME + " ORDER BY title asc"
    connection = sqlite3.connect("../" + DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result