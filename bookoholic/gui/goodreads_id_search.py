import sys
import string
import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QTextEdit, QComboBox, QDialog, QGridLayout,
                             QLayout, QSlider)
from PyQt5.QtGui import QIcon, QPixmap
from goodreads_option import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class IdSearchForm(QDialog):
    def __init__(self):
        super(IdSearchForm, self).__init__()
        self.initUI(self)

    def initUI(self, BookForm):
        layout = QGridLayout(self)

        self.user_label = QLabel("User ID:")
        self.user_line_edit = QLineEdit()

        self.login_button = QPushButton("Search")

        layout.addWidget(self.user_label, 0, 0)
        layout.addWidget(self.user_line_edit, 0, 1)
        layout.addWidget(self.login_button, 1, 0, 1, 2, Qt.AlignCenter)

        self.setLayout(layout)
        self.login_button.clicked.connect(self.login_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Goodreads")
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))

    def login_button_click(self):
        user = self.user_line_edit.text()
        if user.isdigit():
            self.options_form_load = GoodreadsOptionsForm(user)
            self.options_form_load.show()
        else:
            QMessageBox(QMessageBox.Critical, "Error",
                        "ID must be numeric.").exec_()
            return
