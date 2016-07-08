import sys
import string
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QMessageBox,
                             QDialog, QGridLayout, QLayout, QTableView,
                             QAbstractScrollArea, QComboBox)
from goodread.goodreads_client import GoodReadsClient
from goodread.goodreads_book import GoodReadsBook
from goodread.goodreads_book_model import GoodReadsBookModel
from settings import KEY, SECRET


class GoodreadsOptionsForm(QDialog):
    def __init__(self, user_id):
        super(GoodreadsOptionsForm, self).__init__()
        self.initUI(self)
        self.user_id = user_id

    def initUI(self, GoodreadsOptionsForm):
        layout = QGridLayout(self)

        self.main_label = QLabel("Please choose an option:")
        self.search_combo_box = QComboBox()
        self.search_combo_box.addItem("Read")
        self.search_combo_box.addItem("Currently Reading")
        self.search_combo_box.addItem("To-Read")
        self.search_button = QPushButton("Search")

        layout.addWidget(self.main_label, 0, 0)
        layout.addWidget(self.search_combo_box, 0, 1)
        layout.addWidget(self.search_button, 0, 2, 1, 2)

        self.setLayout(layout)
        self.search_button.clicked.connect(self.search_button_click)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.setWindowTitle("Search Books")
        self.setWindowIcon(QIcon(QPixmap('../images/search.png')))


    def show_user_shelf(self, user_id, shelf):
        goodreads_shelf = shelf 
        client = GoodReadsClient(KEY, SECRET)
        books = client.get_shelf(user_id, goodreads_shelf)
        view_books = []

        for book in books:
            isbn = book["isbn"]
            title = book["title"]
            goodreads_url = book["link"]
            year = book["published"]
            author = book["authors"][0]["name"]
            rating = book["average_rating"]
            view_books.append((isbn, title, author, year, rating, goodreads_url))

        if view_books != []:
            book_model = GoodReadsBookModel()
            view_books = [GoodReadsBook(*book) for book in view_books]
            book_model.set_books(view_books)
            self.show_table(book_model)
        else:
            QMessageBox(QMessageBox.Information, "No results",
                        "Sorry. There are no results found!").exec_()

    def show_table(self, model):
        self.table = QTableView()
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.model = model
        self.table.setWindowTitle("Books")
        self.table.setWindowIcon(QIcon(QPixmap('../images/icon.png')))
        self.table.setModel(model)
        self.table.resizeColumnsToContents()
        self.table.show()    


    def search_button_click(self):
        option = self.search_combo_box.currentText()    
        shelf = ""
        if option == 'Read':
            shelf = "read"
        elif option == 'Currently Reading':
            shelf = "currently-reading"
        elif option == 'To-Read':
            shelf = "to-read"

        self.show_user_shelf(self.user_id, shelf)
