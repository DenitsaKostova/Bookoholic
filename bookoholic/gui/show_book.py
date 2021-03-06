"""
    A GUI form for searching for books by: ISBN,
    title, author or genre
"""
import sys
import string
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QDialog, QGridLayout, QLayout, QTableView,
                             QAbstractScrollArea, QComboBox)

from validation_utils import Validations
from book.book import *
from db_manipulations import *
from book.book_model import *


class SearchForm(QDialog):
    def __init__(self):
        super(SearchForm, self).__init__()
        self.initUI(self)

    def initUI(self, SearchForm):
        layout = QGridLayout(self)

        self.search_label = QLabel("Search book by:")
        self.search_combo_box = QComboBox()
        self.search_combo_box.addItem("ISBN")
        self.search_combo_box.addItem("Title")
        self.search_combo_box.addItem("Author")
        self.search_combo_box.addItem("Genre")
        self.search_line_edit = QLineEdit()
        self.search_button = QPushButton("Search")

        layout.addWidget(self.search_label, 0, 0)
        layout.addWidget(self.search_combo_box, 0, 1)
        layout.addWidget(self.search_line_edit, 0, 2)
        layout.addWidget(self.search_button, 0, 3, 1, 2)

        self.setLayout(layout)
        self.search_button.clicked.connect(self.search_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Search Book")
        self.setWindowIcon(QIcon(QPixmap('../images/search.png')))

    def show_table(self, model):
        self.table = QTableView()
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.model = model
        self.table.setWindowTitle("Books")
        self.table.setWindowIcon(QIcon(QPixmap('../images/icon.png')))
        self.table.setModel(model)
        self.table.show()

    def search_button_click(self):
        search = self.search_combo_box.currentText()
        text = self.search_line_edit.text()

        if search == 'ISBN':
            if not(Validations.is_valid_isbn(text)):
                QMessageBox(QMessageBox.Critical, "Error",
                            "Invalid ISBN. Please correct it!").exec_()
            books = select_by_isbn(string.capwords(text))
        elif search == 'Title':
            books = select_by_title(string.capwords(text))
        elif search == 'Author':
            books = select_by_author(string.capwords(text))
        elif search == 'Genre':
            books = select_by_genre(string.capwords(text))

        if books != []:
            book_model = BookModel()
            books = [Book(*book) for book in books]
            book_model.set_books(books)
            self.show_table(book_model)
        else:
            QMessageBox(QMessageBox.Information, "No results",
                        "Sorry. There are no results found!").exec_()
