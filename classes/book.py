import sqlite3
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Book:
# def __init__(self, isbn, title, author, year, genre, rating, review, status):
#     self.isbn = isbn
#     self.title = title
#     self.author = author
#     self.year = year
#     self.genre = genre
#     self.rating = rating
#     self.review = review
#     self.status = status

#THIS NAME SHOULD BE CHANGED ASAP
    def __init__(self, *attrs):
        self.isbn = attrs[0]
        self.title = attrs[1]
        self.author = attrs[2]
        self.year = attrs[3]
        self.genre = attrs[4]
        self.rating = attrs[5]
        self.review = attrs[6]
        self.status = attrs[7]

    @property
    def get_isbn(self):
        return self.isbn

    @property
    def get_title(self):
        return self.title

    @property
    def get_author(self):
        return self.author

    @property
    def get_year(self):
        return self.year

    @property
    def get_genre(self):
        return self.genre

    @property
    def get_rating(self):
        return self.rating

    @property
    def get_review(self):
        return self.review    

    @property
    def get_status(self):
        return self.status
        
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%s;%s;%s;%s;%s;%s,%s,%s" % (self.isbn, self.title,
                                          self.author, self.year,
                                          self.genre, self.rating, 
                                          self.review, self.status)

    def __str__(self):
        return (self.isbn + ' ' + self.title + ' ' +
                self.author + ' ' + str(self.year) + ' ' + 
                self.genre + ' ' + str(self.rating) + ' ' +
                self.review + ' ' + self.status)

    