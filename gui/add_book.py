import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit,
                             QComboBox, QDialog, QGridLayout, QLayout)
from PyQt5.QtGui import QIcon, QPixmap
from validation_utils import Validations
from classes.book import Book
import gui.main

class BookForm(QDialog):
    def __init__(self):
        super(BookForm, self).__init__()
        self.add_book_UI(self)

    def add_book_UI(self, BookForm):
        layout = QGridLayout(self)
        self.books = []

        self.isbn_label = QLabel("ISBN:")
        self.isbn_line_edit = QLineEdit()

        self.title_label = QLabel("Title:")
        self.title_line_edit = QLineEdit()

        self.author_label = QLabel("Author:")
        self.author_line_edit = QLineEdit()

        self.year_label = QLabel("Year:")
        self.year_line_edit = QLineEdit()

        self.genre_label = QLabel("Genre:")
        self.genre_combo_box = QComboBox()
        self.genre_combo_box.addItem("Biography")
        self.genre_combo_box.addItem("Business")
        self.genre_combo_box.addItem("Chick Lit")
        self.genre_combo_box.addItem("Classics")
        self.genre_combo_box.addItem("Comics")
        self.genre_combo_box.addItem("Contemporary")
        self.genre_combo_box.addItem("Crime")
        self.genre_combo_box.addItem("Fantasy")
        self.genre_combo_box.addItem("Fiction")
        self.genre_combo_box.addItem("Historical Fiction")
        self.genre_combo_box.addItem("History")
        self.genre_combo_box.addItem("Horror")
        self.genre_combo_box.addItem("Humor and Comedy")
        self.genre_combo_box.addItem("Memoir")
        self.genre_combo_box.addItem("Mystery")
        self.genre_combo_box.addItem("Nonfiction")
        self.genre_combo_box.addItem("Paranormal")
        self.genre_combo_box.addItem("Philosophy")
        self.genre_combo_box.addItem("Poetry")
        self.genre_combo_box.addItem("Psychology")
        self.genre_combo_box.addItem("Romance")
        self.genre_combo_box.addItem("Science")
        self.genre_combo_box.addItem("Science Fiction")
        self.genre_combo_box.addItem("Self Help")
        self.genre_combo_box.addItem("Thriller")
        self.genre_combo_box.addItem("Travel")
        self.genre_combo_box.addItem("Technical")
        self.genre_combo_box.addItem("Young Adult")
        self.genre_combo_box.addItem("Other")

        self.review_label = QLabel("Review:")
        self.review_line_edit = QTextEdit()

        self.status_label = QLabel("Status:")
        self.status_combo_box = QComboBox()
        self.status_combo_box.addItem("Read")
        self.status_combo_box.addItem("Currently Readung")
        self.status_combo_box.addItem("Want to Read")

        self.add_button = QPushButton("Add Book")

        layout.addWidget(self.isbn_label, 0, 0)
        layout.addWidget(self.isbn_line_edit, 0, 1)
        layout.addWidget(self.title_label, 1, 0)
        layout.addWidget(self.title_line_edit, 1, 1)
        layout.addWidget(self.author_label, 2, 0)
        layout.addWidget(self.author_line_edit, 2, 1)
        layout.addWidget(self.year_label, 3, 0)
        layout.addWidget(self.year_line_edit, 3, 1)
        layout.addWidget(self.genre_label, 4, 0)
        layout.addWidget(self.genre_combo_box, 4, 1)
        layout.addWidget(self.review_label, 5, 0)
        layout.addWidget(self.review_line_edit, 5, 1)
        layout.addWidget(self.status_label, 6, 0)
        layout.addWidget(self.status_combo_box, 6, 1)
        layout.addWidget(self.add_button, 7, 0, 1, 2,Qt.AlignCenter)

        self.setLayout(layout)
        self.add_button.clicked.connect(self.add_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Add Book")
        self.setWindowIcon(QIcon(QPixmap('icon.png')))

