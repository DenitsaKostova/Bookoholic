import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import sqlite3
from install import create_table
from settings import *
from book.book import Book
from install import *
from db_manipulations import *
from gui.add_book import *
from gui.delete_book import *
from gui.show_book import *
from gui.show_wishlist import *

TEST_DATABASE = 'tests.db'

import unittest


class DBTest(unittest.TestCase):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

    def setUp(self):
        create_tables(TEST_DATABASE)

    def test_add_book(self):
        book1 = Book('9780062024039', 'Divergent', 'Veronica Roth', 2012, 'Fantasy', 3, 'NO', 'Read')
        book2 = Book('9780439554930', 'Harry Potter #1', ' J.K. Rowling', 1997, 'Fantasy', 5, 'perfe', 'Currently Reading')
        add_book(book1)
        add_book(book2)
        