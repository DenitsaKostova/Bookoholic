import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import string
import sqlite3
from db_manipulations import *
from book import Book

def add_book(book):
    add_entry(book.isbn, book.title, book.author, book.year,
              book.genre, book.rating, book.review, book.status)

def search_by_isbn(isbn):
    select_by_isbn(isbn)    

def search_by_title(title):
    select_by_title(string.capwords(title))

def search_by_author(author):
    select_by_author(string.capwords(author))

def search_by_genre(genre):
    genre_list = ["Biography", "Business", "Chick Lit","Classics", "Comics",
                  "Contemporary", "Crime", "Fantasy", "Fiction", "History",
                  "Historical Fiction", "Horror", "Humor and Comedy", "Memoir",
                  "Mystery", "Nonfiction", "Paranormal", "Philosophy", 
                  "Poetry", "Psychology", "Romance", "Science", "Self Help",
                  "Science Fiction", "Thriller", "Technical", "Young Adult", 
                  "Other"]
    if genre in genre_list:
      select_by_genre(string.capwords(genre))

