import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from bookoholic.book.book import Book
from bookoholic.book.book_model import BookModel, COLUMNS
from PyQt5.QtCore import Qt
import unittest

class ModelTest(unittest.TestCase):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

    def test_book_model(self):
        books = [Book('9780062024039', 'Divergent', 'Veronica Roth', 
                       2012, 'Fantasy', 3, 'NO', 'Read'),
                 Book('9780439554930', 'Harry Potter #1', ' J.K. Rowling', 
                       1997, 'Fantasy', 5, 'perfe', 'Currently Reading'),
                 Book('0450040186', 'The Shining', 'Stephen King', 
                       1980, 'Horror' , 2, 'ok', 'Want To Read')]

        self.book_model = BookModel()
        self.book_model.set_books(books)
        self.assertEqual(self.book_model.rowCount(), len(books))
        self.assertEqual(self.book_model.headerData(0, Qt.Horizontal,
                         Qt.DisplayRole), 'ISBN')
        self.assertEqual(self.book_model.headerData(1, Qt.Horizontal,
                         Qt.DisplayRole), 'Title')
        self.assertEqual(self.book_model.headerData(2, Qt.Horizontal,
                         Qt.DisplayRole), 'Author')
        self.assertEqual(self.book_model.headerData(3, Qt.Horizontal,
                         Qt.DisplayRole), 'Year') 
        self.assertEqual(self.book_model.headerData(4, Qt.Horizontal,
                         Qt.DisplayRole), 'Genre') 
        self.assertEqual(self.book_model.headerData(5, Qt.Horizontal,
                         Qt.DisplayRole), 'Rating') 
        self.assertEqual(self.book_model.headerData(6, Qt.Horizontal,
                         Qt.DisplayRole), 'Review') 
        self.assertEqual(self.book_model.headerData(7, Qt.Horizontal,
                         Qt.DisplayRole), 'Status') 

        getters = ('get_isbn', 'get_title', 'get_author', 'get_year',
                   'get_genre', 'get_rating', 'get_review', 'get_status')
        for row in range(self.book_model.rowCount()):
            for column in range(COLUMNS):
                self.assertEqual(getattr(books[row], getters[column]),
                                 self.book_model.data(self.book_model.index(
                                                      row, column),
                                                      Qt.DisplayRole))
