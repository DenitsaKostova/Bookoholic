import sqlite3
from settings import *

def create_table():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS " + \
        "BooksInfo(isbn TEXT primary key, title TEXT, author TEXT, " + \
        "year LONG, genre TEXT, rating LONG, review TEXT, status TEXT)"
    cursor.execute(query)
    connection.commit()
    connection.close()

create_table()