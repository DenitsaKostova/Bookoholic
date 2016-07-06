"""
    Show full library
"""
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QDialog, QGridLayout, QLayout, QTableView,
                             QAbstractScrollArea, QComboBox)

from book.book import Book
from db_manipulations import *
from book.book_model import *


class LibraryForm(QDialog):
    def __init__(self):
        super(LibraryForm, self).__init__()
        self.initUI(self)

    def initUI(self, LibraryForm):
        layout = QGridLayout(self)

        self.show_lib_button = QPushButton("Show Library")
        layout.addWidget(self.show_lib_button, 0, 1, 1, 2)

        self.setLayout(layout)
        self.show_lib_button.clicked.connect(self.show_lib_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Library")
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))

    def show_table(self, model):
        self.table = QTableView()
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.model = model
        self.table.setWindowTitle("Library")
        self.table.setWindowIcon(QIcon(QPixmap('../images/icon.png')))
        self.table.setModel(model)
        self.table.show()

    def show_lib_button_click(self):
        books = select_all()
        
        if books == []:
            QMessageBox(QMessageBox.Warning, "Error",
                        "There are no books in the library!").exec_()
            return
        else:
            book_model = BookModel()
            books = [Book(*book) for book in books]
            book_model.set_books(books)
            self.show_table(book_model)

        
        
