"""
    A GUI Form for deleting a book by title
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
from classes.book import Book
from db_manipulations import *
from book_model import *


class DeleteForm(QDialog):
    def __init__(self):
        super(DeleteForm, self).__init__()
        self.initUI(self)

    def initUI(self, DeleteForm):
        layout = QGridLayout(self)

        self.delete_label = QLabel("Title:")
        self.delete_line_edit = QLineEdit()
        self.delete_button = QPushButton("Delete")

        layout.addWidget(self.delete_label, 0, 0)
        layout.addWidget(self.delete_line_edit, 0, 1)
        layout.addWidget(self.delete_button, 0, 2, 1, 1)

        self.setLayout(layout)
        self.delete_button.clicked.connect(self.delete_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Delete Book")
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))

    def delete_button_click(self):
        text = self.delete_line_edit.text()
        books = select_by_title(string.capwords(text))

        if books != []:
            delete_by_title(string.capwords(text))
            QMessageBox(QMessageBox.Information, "Information",
                        "You successfully deleted thos book!").exec_()
            return
        else:
            QMessageBox(QMessageBox.Warning, "Error",
                        "There is no such book in the library!").exec_()
            return
