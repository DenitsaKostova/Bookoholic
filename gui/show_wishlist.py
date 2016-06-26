import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QDialog, QGridLayout, QLayout, QTableView,
                             QAbstractScrollArea, QComboBox)

from validation_utils import Validations
from classes.book import Book
from db_manipulations import *
from wishlist_model import *

class WishlistForm(QDialog):
    def __init__(self):
        super(WishlistForm, self).__init__()
        self.initUI(self)

    def initUI(self, WishlistForm):
        layout = QGridLayout(self)
        """layout.setContentsMargins(0, 0, 0, 0)
        myImage = QImage()
        myImage.load("../images/texture.jpg")

        myLabel = QLabel()
        myLabel.setScaledContents(True)
        self.setGeometry(100, 100, 650, 350)
        myLabel.setPixmap(QPixmap.fromImage(myImage))
        layout.addWidget(myLabel)"""

        self.show_wishlist_button = QPushButton("Show Wishlist")
        layout.addWidget(self.show_wishlist_button, 0, 1, 1, 2)

        self.setLayout(layout)
        self.show_wishlist_button.clicked.connect(self.show_wishlist_button_click)
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
        text = 'Want to Read'
        books = select_by_status(text)
        #print(books)
        wishlist_model = WishlistModel()
        books = [Book(*book) for book in books]
        wishlist_model.set_books(books)
        self.show_table(wishlist_model)