"""
    A GUI form for loging in to Goodreads profile(optional)
"""
import sys
import string
import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QTextEdit, QComboBox, QDialog, QGridLayout,
                             QLayout, QSlider)
from PyQt5.QtGui import QIcon, QPixmap

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class LoginForm(QDialog):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.initUI(self)

    def initUI(self, BookForm):
        layout = QGridLayout(self)

        self.user_label = QLabel("User:")
        self.user_line_edit = QLineEdit()

        self.pass_label = QLabel("Password:")
        self.pass_line_edit = QLineEdit()

        self.login_button = QPushButton("Login")

        layout.addWidget(self.user_label, 0, 0)
        layout.addWidget(self.user_line_edit, 0, 1)
        layout.addWidget(self.pass_label, 1, 0)
        layout.addWidget(self.pass_line_edit, 1, 1)
        layout.addWidget(self.login_button, 2, 0, 1, 2, Qt.AlignCenter)

        self.setLayout(layout)
        self.login_button.clicked.connect(self.login_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Goodreads")
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))

    def login_button_click(self):
        user = self.isbn_line_edit.text()
        password = self.pass_line_edit.text()

        