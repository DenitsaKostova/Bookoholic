"""
    A GUI form for adding a book
"""
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton,QMessageBox, QTextEdit,
                             QComboBox, QDialog, QGridLayout, QLayout, QSlider)
from PyQt5.QtGui import QIcon, QPixmap
from validation_utils import Validations
from classes.book import Book
from db_manipulations import add_book

class BookForm(QDialog):
    def __init__(self):
        super(BookForm, self).__init__()
        self.initUI(self)

    def initUI(self, BookForm):
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

        self.rating_label = QLabel("Rating:")
        self.rating_slider = QSlider(Qt.Horizontal)
        self.rating_slider.setMinimum(0)
        self.rating_slider.setMaximum(5)
        self.rating_slider.setValue(0)
        self.rating_slider.setTickPosition(QSlider.TicksBelow)
        self.rating_slider.setTickInterval(5)

        self.review_label = QLabel("Review:")
        self.review_text_edit = QTextEdit()

        self.status_label = QLabel("Status:")
        self.status_combo_box = QComboBox()
        self.status_combo_box.addItem("Read")
        self.status_combo_box.addItem("Currently Reading")
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
        layout.addWidget(self.rating_label, 5, 0)
        layout.addWidget(self.rating_slider, 5, 1)
        layout.addWidget(self.review_label, 6, 0)
        layout.addWidget(self.review_text_edit, 6, 1)
        layout.addWidget(self.status_label, 7, 0)
        layout.addWidget(self.status_combo_box, 7, 1)
        layout.addWidget(self.add_button, 8, 0, 1, 2,Qt.AlignCenter)

        self.setLayout(layout)
        self.add_button.clicked.connect(self.add_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Add Book")
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))
        

    def information_validation(self, year, isbn):
        return (not Validations.is_valid_year(year) or
                not Validations.is_valid_isbn(isbn))

    def error_message(self, year, isbn):
        validations = [Validations.is_valid_year, Validations.is_valid_isbn]
        var = [year, isbn]
        messages = ['year', 'ISBN']
        result = []
        for i in range(len(var)):
            if not validations[i](var[i]):
                result.append(messages[i] + ',')
        return ' '.join(result)

    def add_button_click(self):
        isbn = self.isbn_line_edit.text()
        title = self.title_line_edit.text()
        author = self.author_line_edit.text()
        year = self.year_line_edit.text()
        genre = self.genre_combo_box.currentText()
        rating = self.rating_slider.value()
        review = self.review_text_edit.toPlainText()
        status = self.status_combo_box.currentText()

        if self.information_validation(year, isbn):
            error_message = self.error_message(year, isbn)
            QMessageBox(QMessageBox.Critical, "Error",
                        "Invalid " + error_message[:len(error_message) - 1] +
                        ". Please correct it!").exec_()
            return

        new_book = Book(isbn, title, author, int(year), genre, int(rating), review, status)

        if new_book in self.books:
            QMessageBox(QMessageBox.Warning, "Warning",
                        "You have already added this book!").exec_()
            return

        self.books.append(new_book)
        if add_book(new_book):
            QMessageBox(QMessageBox.Information, "Add Book",
                        "You successfully added this book!").exec_()
        else:
            QMessageBox(QMessageBox.Information, "Add Book",
                        "You successfully added this book!").exec_()
