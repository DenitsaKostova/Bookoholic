import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from bookoholic.book.book import Book


class BookTest(unittest.TestCase):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

    def test_types(self):
        book = Book('9780062024039', 'Divergent', 'Veronica Roth', 2012, 'Fantasy', 3, 'NO', 'Read')
        self.assertTrue(book.get_isbn, str)
        self.assertTrue(book.get_title, str)
        self.assertTrue(book.get_author, str)
        self.assertTrue(book.get_year, int)
        self.assertTrue(book.get_genre, str)
        self.assertTrue(book.get_rating, int)
        self.assertTrue(book.get_review, str)
        self.assertTrue(book.get_status, str)

    def test_decorator(self):
        book = Book('9780062024039', 'Divergent', 'Veronica Roth', 2012, 'Fantasy', 3, 'NO', 'Read')
        self.assertRaises(AttributeError, get_isbn='1280062024039')
        self.assertRaises(AttributeError, get_title='Hello')
        self.assertRaises(AttributeError, get_author='Veronica Potter')
        self.assertRaises(AttributeError, get_year=2013)
        self.assertRaises(AttributeError, get_genre='Other')
        self.assertRaises(AttributeError, get_rating=2)
        self.assertRaises(AttributeError, get_review="Lqlqlq")
        self.assertRaises(AttributeError, get_status="Reading")
    

    def test_init(self):
        book = Book('9780062024039', 'Divergent', 'Veronica Roth', 2012, 'Fantasy', 3, 'NO', 'Read')
        self.assertEqual(book.get_isbn, '9780062024039')
        self.assertNotEqual(book.get_isbn, '1780062024039')
        self.assertEqual(book.get_title, 'Divergent')
        self.assertNotEqual(book.get_title, 'Bookoholic')
        self.assertEqual(book.get_author, 'Veronica Roth')
        self.assertNotEqual(book.get_author, 'Veronica Lqlqlq')
        self.assertEqual(book.get_year, 2012)
        self.assertNotEqual(book.get_year, 2017)
        self.assertEqual(book.get_genre, 'Fantasy')
        self.assertNotEqual(book.get_genre, 'Horror')
        self.assertEqual(book.get_rating, 3)
        self.assertNotEqual(book.get_rating, 23)
        self.assertEqual(book.get_review, 'NO')
        self.assertNotEqual(book.get_review, 'Yes')
        self.assertEqual(book.get_status, 'Read')
        self.assertNotEqual(book.get_status, 'Reading')
