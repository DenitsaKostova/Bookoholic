"""
    A GUI Form for deleting a book by isbn or title
"""
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QDialog, QGridLayout, QLayout, QTableView,
                             QAbstractScrollArea, QComboBox)

from validation_utils import Validations
from book.book import Book
from db_manipulations import *
from book.book_model import *


class DeleteForm(QDialog):
    def __init__(self):
        super(DeleteForm, self).__init__()
        self.initUI(self)

    def initUI(self, DeleteForm):
        layout = QGridLayout(self)

        self.delete_label = QLabel("Delete by:")
        self.delete_combo_box = QComboBox()
        self.delete_combo_box.addItem("ISBN")
        self.delete_combo_box.addItem("Title")
        self.delete_line_edit = QLineEdit()
        self.delete_button = QPushButton("Delete")

        layout.addWidget(self.delete_label, 0, 0)
        layout.addWidget(self.delete_combo_box, 0, 1)
        layout.addWidget(self.delete_line_edit, 0, 2)
        layout.addWidget(self.delete_button, 0, 3, 1, 2)

        self.setLayout(layout)
        self.delete_button.clicked.connect(self.delete_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Delete Book")
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))

    def delete_button_click(self):
        search = self.delete_combo_box.currentText()
        text = self.delete_line_edit.text()
        
        if search == 'ISBN':
            if not(Validations.is_valid_isbn(text)):
                QMessageBox(QMessageBox.Critical, "Error",
                            "Invalid ISBN. Please correct it!").exec_()
            books = select_by_isbn(string.capwords(text))
            if books != []:
                delete_by_isbn(string.capwords(text))
                QMessageBox(QMessageBox.Information, "Information",
                            "You successfully deleted this book!").exec_()
                return
        elif search == 'Title':
            books = select_by_title(string.capwords(text))
            if books != []:
                delete_by_title(string.capwords(text))
                QMessageBox(QMessageBox.Information, "Information",
                        "You successfully deleted this book!").exec_()
                return
        else:
            QMessageBox(QMessageBox.Information, "No results",
                        "There is NO such book in the library!").exec_()
            return
