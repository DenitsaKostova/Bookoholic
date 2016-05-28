import sqlite3
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Book:
    def __init__(self, isbn, title, author, year, genre, review, status):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.review = review
        self.status = status

    def __str__(self):
        return (self.isbn + ' ' + self.title + ' ' +
                self.author + ' ' + str(self.year) + ' ' + 
                self.genre + ' ' + self.review + ' ' + 
                self.status)

    @property
    def get_isbn(self):
        return self.get_isbn

    @property
    def get_title(self):
        return self.get_title

    @property
    def get_author(self):
        return self.get_author

    @property
    def get_year(self):
        return self.get_year

    @property
    def get_genre(self):
        return self.get_genre

    @property
    def get_status(self):
        return self.get_status