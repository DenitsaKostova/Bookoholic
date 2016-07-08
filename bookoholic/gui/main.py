import os
import sys

from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtWidgets import (QMainWindow, QApplication, QVBoxLayout,
                             QLabel, QWidget, QAction, QDesktopWidget,
                             QMessageBox, QTableView, QAbstractScrollArea)

from add_book import BookForm
from edit_book import EditForm
from delete_book import DeleteForm
from show_book import SearchForm
from show_library import LibraryForm
from show_wishlist import WishlistForm
from goodreads_id_search import IdSearchForm


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        myImage = QImage()
        myImage.load("../images/wallpaper.jpg")

        myLabel = QLabel()
        myLabel.setScaledContents(True)
        self.setGeometry(100, 100, 650, 350)
        myLabel.setPixmap(QPixmap.fromImage(myImage))
        layout.addWidget(myLabel)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)
        self.setWindowIcon(QIcon(QPixmap('../images/icon.png')))

        menubar = self.menuBar()

        """
            Login Menu - Goodreads Profile
        """
        book_menu = menubar.addMenu('&Goodreads')
        login_action = QAction(QIcon('../images/login.png'),
                               '&Goodreads profile', self)
        login_action.setStatusTip('Login to Goodreads profile (optional)')
        login_action.triggered.connect(self.goodreads_form_load)
        book_menu.addAction(login_action)

        """
            Books Menu - add / delete book
        """
        book_menu = menubar.addMenu('&Books')
        add_book_action = QAction(QIcon('../images/add.png'),
                                  '&Add Book', self)
        add_book_action.setStatusTip('Add a new book to the library')
        add_book_action.triggered.connect(self.add_book_form_load)
        book_menu.addAction(add_book_action)

        edit_book_action = QAction(QIcon('../images/edit.png'),
                                   '&Edit Book', self)
        edit_book_action.setStatusTip('Edit an existing book.')
        edit_book_action.triggered.connect(self.edit_book_form_load)
        book_menu.addAction(edit_book_action)

        delete_book_action = QAction(QIcon('../images/delete.png'),
                                     '&Delete Book', self)
        delete_book_action.setStatusTip('Delete a book from the library')
        delete_book_action.triggered.connect(self.delete_book_form_load)
        book_menu.addAction(delete_book_action)

        """
            Library Menu - Search for specific book/s,
            show the whole Library
        """
        book_menu = menubar.addMenu('&Library')

        search_book_action = QAction(QIcon('../images/search.png'),
                                     '&Search Book', self)
        search_book_action.setStatusTip('Search for a book in the library')
        search_book_action.triggered.connect(self.search_book_form_load)
        book_menu.addAction(search_book_action)

        show_library_action = QAction(QIcon('../images/library.png'),
                                      '&Show Library', self)
        show_library_action.setStatusTip('Show all books in the Library')
        show_library_action.triggered.connect(self.show_library_form_load)
        book_menu.addAction(show_library_action)

        """
            Wishlist Menu - show wishlist
        """
        whishlist_menu = menubar.addMenu('&Wishlist')

        show_wishlist_action = QAction(QIcon('../images/whish.png'),
                                       '&Show Wishlist', self)
        show_wishlist_action.setStatusTip('Show wishlist')
        show_wishlist_action.triggered.connect(self.show_wishlist_form_load)
        whishlist_menu.addAction(show_wishlist_action)

        self.statusBar()
        self.setWindowTitle("Bookoholic")
        self.move(QDesktopWidget().availableGeometry().center() -
                  self.frameGeometry().center())

    def goodreads_form_load(self):
        self.goodreads_form_load = IdSearchForm()
        self.goodreads_form_load.show()

    def add_book_form_load(self):
        self.add_book_form_load = BookForm()
        self.add_book_form_load.show()

    def edit_book_form_load(self):
        self.edit_book_form_load = EditForm()
        self.edit_book_form_load.show()

    def delete_book_form_load(self):
        self.delete_book_form_load = DeleteForm()
        self.delete_book_form_load.show()

    def search_book_form_load(self):
        self.search_book_form_load = SearchForm()
        self.search_book_form_load.show()

    def show_library_form_load(self):
        self.show_library_form_load = LibraryForm()
        self.show_library_form_load.show()

    def show_wishlist_form_load(self):
        self.show_wishlist_form_load = WishlistForm()
        self.show_wishlist_form_load.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
