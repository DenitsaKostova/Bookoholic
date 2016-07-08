"""
    A GUI form for editing a book's rating, review and status
"""
import sys
import string
import os.path
import string

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QTextEdit, QComboBox, QDialog, QGridLayout,
                             QLayout, QSlider)
from PyQt5.QtGui import QIcon, QPixmap

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from validation_utils import Validations
from book.book import Book
from db_manipulations import *


class EditForm(QDialog):
    def __init__(self):
        super(EditForm, self).__init__()
        self.initUI(self)

    def initUI(self, EditForm):
        layout = QGridLayout(self)

        self.title_label = QLabel("Title:")
        self.title_line_edit = QLineEdit()
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
        self.status_combo_box.addItems(["Read",
                                        "Currently Reading",
                                        "Want Тo Read"])
        self.edit_button = QPushButton("Edit book")

        layout.addWidget(self.title_label, 0, 0)
        layout.addWidget(self.title_line_edit, 0, 1)
        layout.addWidget(self.rating_label, 1, 0)
        layout.addWidget(self.rating_slider, 1, 1)
        layout.addWidget(self.review_label, 2, 0)
        layout.addWidget(self.review_text_edit, 2, 1)
        layout.addWidget(self.status_label, 3, 0)
        layout.addWidget(self.status_combo_box, 3, 1)
        layout.addWidget(self.edit_button, 4, 0, 1, 2, Qt.AlignCenter)

        self.setLayout(layout)
        self.edit_button.clicked.connect(self.edit_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Edit Book")
        self.setWindowIcon(QIcon(QPixmap('../images/edit.png')))

    def edit_button_click(self):
        title = self.title_line_edit.text()
        rating = self.rating_slider.value()
        review = self.review_text_edit.toPlainText()
        status = self.status_combo_box.currentText()

        if select_by_title(string.capwords(title)) == []:
            QMessageBox(QMessageBox.Critical, "Error",
                        "There is no such book in the library!").exec_()
        else:
            if update_entry(string.capwords(title), rating, review, status):
                QMessageBox(QMessageBox.Information, "Updated book info",
                            "You updated the info about this book!").exec_()
            else:
                QMessageBox(QMessageBox.Information, "Information",
                            "The book was NOT edited! Try again.").exec_()


  
        