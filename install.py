import sqlite3


TABLE_NAME = "BooksInfo"
connection = sqlite3.connect('booktable.db')
cursor = connection.cursor()

def create_table():
	cursor.execute("CREATE TABLE IF NOT EXISTS BooksInfo(isbn TEXT,title TEXT, author TEXT, year LONG, genre TEXT, review TEXT, status TEXT)")
	connection.commit()
	connection.close()	

def data_entry():
	cursor.execute("INSERT INTO BooksInfo VALUES('123-456-789', 'Harry Potter', 'J.K.Rowling', 1997, 'Fantasy', 'I liked it vary much', 'read')")
	connection.commit()
	connection.close()

def add_entry(isbn, title, author, year, genre, review, status):
	cursor.execute("INSERT INTO " +  TABLE_NAME + " VALUES(" + "'{}','{}','{}',{},'{}','{}','{}'".format(isbn, title, author, year, genre, review, status) + ")")
	connection.commit()
	connection.close()

def select_by_isbn(isbn):
	query = "SELECT * FROM" + TABLE_NAME + "WHERE isbn=" + isbn
	cursor.execute(query)
	connection.commit()
	connection.close()

def select_by_title(title):
	query = "SELECT * FROM" + TABLE_NAME + "WHERE title=" + title
	cursor.execute(query)
	connection.commit()
	connection.close()

def select_by_author(author):
	query = "SELECT * FROM" + TABLE_NAME + "WHERE author=" + author
	cursor.execute(query)
	connection.commit()
	connection.close()

def select_by_genre(genre):
	query = "SELECT * FROM" + TABLE_NAME + "WHERE genre=" + genre
	cursor.execute(query)
	connection.commit()
	connection.close()

def select_by_genre(status):
	query = "SELECT * FROM" + TABLE_NAME + "WHERE status=" + status
	cursor.execute(query)
	connection.commit()
	connection.close()


def delete_book(filename=TABLE_NAME):
	cursor.execute("Delete from BooksInfo")
	connection.commit()
	connection.close()

#create_table()
