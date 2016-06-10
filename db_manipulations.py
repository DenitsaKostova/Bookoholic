import sqlite3
from settings import * 


def execute_query(query):
    connection = sqlite3.connect("../" + DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def add_dummy_entry():
    query = "INSERT INTO " + TABLE_NAME + " VALUES('123-456-789', 'Harry Potter', 'J.K.Rowling', 1997, 'Fantasy', 4, 'I liked it vary much', 'read')"
    execute_query(query)

def add_entry(isbn, title, author, year, genre, rating, review, status):
    query = "INSERT INTO " +  TABLE_NAME + " VALUES(" + "'{}','{}','{}',{},'{}',{},'{}','{}')"\
            .format(isbn, title, author, year, genre, rating, review, status)
    execute_query(query)

def add_book(book):
    add_entry(book.isbn, book.title, book.author, book.year, 
              book.genre, book.rating, book.review, book.status)

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

def delete_all():
    execute_query("Delete from " + TABLE_NAME)

def select_all():
    query = "SELECT * FROM " + TABLE_NAME
    execute_query(query)

#delete_all()
#add_entry('0439554937', 'Harry Potter', 'J.K.Rowling', 2003, 'Fantasy', 4, 'very entertaining', 'read')
#add_entry('0670026603', 'Me Before You', 'Jojo Moyes', 2012, 'Romantic', 4, 'entertaining', 'to be read')

#print(select_by_title("Harry Potter"))
#print(select_all())