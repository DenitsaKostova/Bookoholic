import sqlite3


TABLE_NAME = "BooksInfo"
connection = sqlite3.connect('booktable.db')
cursor = connection.cursor()

def create_table():
	cursor.execute("CREATE TABLE IF NOT EXISTS BooksInfo(isbn TEXT,title TEXT, author TEXT, year LONG, genre TEXT, review TEXT, status TEXT)")

def data_entry():
	cursor.execute("INSERT INTO BooksInfo VALUES('123-456-789', 'Harry Potter', 'J.K.Rowling', 1997, 'Fantasy', 'I liked it vary much', 'read')")
	connection.commit()
	cursor.close()
	connection.close()

def add_entry(isbn, title, author, year, genre, review, status):
	query = "INSERT INTO " +  TABLE_NAME + " VALUES('{}','{}','{}',{},'{}','{}','{}').format(sbn, title, author, year, genre, review, status)"   

def search_title(isbn):
	query = "SELECT" + isbn + "from" + TABLE_NAME 

def search_title(title):
	query = "SELECT" + title + "from" + TABLE_NAME

def search_title(author):
	query = "SELECT" + author + "from" + TABLE_NAME 

def delete_book(filename=TABLE_NAME):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()
    cursor.execute('''Delete from BooksInfo''')
    connection.commit()
    connection.close()

#create_table()
data_entry()