import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import sqlite3
from install import create_table
from settings import DATABASE_NAME
from book.book import Book
from install import *
from db_manipulations import *

import unittest

ISBN1 = '9780062024039'
ISBN2 = '9780439554930'
ISBN3 = '0450040186'
BOOK1 = [ISBN1, 'Divergent', 'Veronica Roth', 2012,
         'Fantasy', 3, 'NO', 'Read']
BOOK2 = [ISBN2, 'Harry Potter #1', ' J.K. Rowling', 1997,
         'Fantasy', 5, 'perfe', 'Currently Reading']
BOOK3 = [ISBN3, 'The Shining', 'Stephen King', 1980,
         'Horror', 2, 'ok', 'Want To Read']


class DBTest(unittest.TestCase):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

    def setUp(self):
        create_table()

    def add_dummy_entries(self):
        book1 = Book(*BOOK1)
        book2 = Book(*BOOK2)
        book3 = Book(*BOOK3)
        add_book(book1)
        add_book(book2)
        add_book(book3)

    def remove_dummy_entries(self):
        delete_by_isbn(ISBN1)
        delete_by_isbn(ISBN2)
        delete_by_isbn(ISBN3)

    def test_entries_are_stored(self):
        self.add_dummy_entries()
        books = select_all()
        self.assertTrue(tuple(BOOK1) in books)
        self.assertTrue(tuple(BOOK2) in books)
        self.assertTrue(tuple(BOOK3) in books)
        self.remove_dummy_entries()

    def test_select_by_isbn(self):
        self.add_dummy_entries()
        given_book_by_isbn = select_by_isbn(ISBN1)
        expected_book_by_isbn = tuple(BOOK1)
        self.assertEqual(given_book_by_isbn[0], expected_book_by_isbn)
        self.remove_dummy_entries()

    def test_select_by_title(self):
        self.add_dummy_entries()
        given_book_by_title = select_by_title('The Shining')
        expected_book_by_title = tuple(BOOK3)
        self.assertEqual(given_book_by_title[0], expected_book_by_title)
        self.remove_dummy_entries()

    def test_select_by_author(self):
        self.add_dummy_entries()
        given_book_by_author = select_by_author('Stephen King')
        expected_book_by_author = tuple(BOOK3)
        self.assertEqual(given_book_by_author[0], expected_book_by_author)
        self.remove_dummy_entries()

    def test_select_by_genre(self):
        self.add_dummy_entries()
        given_book_by_genre = select_by_genre('Fantasy')
        self.assertTrue(len(given_book_by_genre) >= 2)
        first_expected_book_by_genre = tuple(BOOK1)
        second_expected_book_by_genre = tuple(BOOK2)
        third_not_expected_book = tuple(BOOK3)
        self.assertTrue(first_expected_book_by_genre in given_book_by_genre)
        self.assertTrue(second_expected_book_by_genre in given_book_by_genre)
        self.assertFalse(third_not_expected_book in given_book_by_genre)
        self.remove_dummy_entries()

    def test_delete_entries(self):
        self.add_dummy_entries()
        self.remove_dummy_entries()
        books = select_all()
        self.assertTrue(BOOK1 not in books)
        self.assertTrue(BOOK2 not in books)
        self.assertTrue(BOOK3 not in books)
        self.assertFalse(BOOK1 in books)

    def test_update_entry(self):
        self.add_dummy_entries()
        update_entry('The Shining', 5, 'it was ok', 'Read')
        updated_book = (ISBN3, 'The Shining', 'Stephen King', 1980,
                        'Horror', 5, 'it was ok', 'Read')
        old_book = tuple(BOOK3)
        books = select_all()
        self.assertNotEqual(updated_book, old_book)
        self.assertFalse(old_book in books)
        self.assertTrue(updated_book in books)
        self.remove_dummy_entries()
