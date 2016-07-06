"""
    Shows all the books with status 'Want to Read'
    as a Wishlist. They are automatically added when
    the user adds a book
"""
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QDialog, QGridLayout, QLayout, QTableView,
                             QAbstractScrollArea, QComboBox)

from validation_utils import Validations
from book.book import Book
from db_manipulations import *
from book.book_model import BookModel


class WishlistForm(QDialog):
    def __init__(self):
        super(WishlistForm, self).__init__()
        self.initUI(self)

    def initUI(self, WishlistForm):
        layout = QGridLayout(self)

        self.show_wishlist_button = QPushButton("Show Wishlist")
        layout.addWidget(self.show_wishlist_button, 0, 1, 1, 2)

        self.setLayout(layout)
        self.show_wishlist_button.clicked.connect(self.
                                                  show_wishlist_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Wishlist")
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))

    def show_table(self, model):
        self.table = QTableView()
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.model = model
        self.table.setWindowTitle("Wishlist")
        self.table.setWindowIcon(QIcon(QPixmap('../images/icon.png')))
        self.table.setModel(model)
        self.table.show()

    def show_wishlist_button_click(self):
        text = 'Want Тo Read'
        books = select_by_status(text)
        wishlist_model = BookModel()
        books = [Book(*book) for book in books]
        wishlist_model.set_books(books)
        self.show_table(wishlist_model)
