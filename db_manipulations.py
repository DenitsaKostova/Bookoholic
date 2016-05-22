import sqlite3
from settings import * 


connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

def execute_query(query):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def add_dummy_entry():
    query = "INSERT INTO " + TABLE_NAME + " VALUES('123-456-789', 'Harry Potter', 'J.K.Rowling', 1997, 'Fantasy', 'I liked it vary much', 'read')"
    execute_query(query)


def add_entry(isbn, title, author, year, genre, review, status):
    query = "INSERT INTO " +  TABLE_NAME + " VALUES(" + "'{}','{}','{}',{},'{}','{}','{}')"\
            .format(isbn, title, author, year, genre, review, status)
    execute_query(query)

def select_by_isbn(isbn):
    query = "SELECT * FROM" + TABLE_NAME + "WHERE isbn=" + isbn
    execute_query(query)

def select_by_title(title):
    query = "SELECT * FROM" + TABLE_NAME + "WHERE title=" + title
    execute_query(query)

def select_by_author(author):
    query = "SELECT * FROM" + TABLE_NAME + "WHERE author=" + author
    execute_query(query)

def select_by_genre(genre):
    query = "SELECT * FROM" + TABLE_NAME + "WHERE genre=" + genre
    execute_query(query)

def select_by_genre(status):
    query = "SELECT * FROM" + TABLE_NAME + "WHERE status=" + status
    execute_query(query)

def delete_book():
    execute_query("Delete * from " + TABLE_NAME)



#add_entry('0439554937', 'Harry Potter', 'J.K.Rowling', 2003, 'Fantasy', 'very entertaining', 'read')
#add_entry('0670026603', 'Me Before You', 'Jojo Moyes', 2012, 'Romantic', 'entertaining', 'to be read')
