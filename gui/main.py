import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, 
                             QLabel, QWidget, QAction, QDesktopWidget,
                             QInputDialog, QMessageBox, QTableView, 
                             QAbstractScrollArea, QSlider)

from add_book import *
from delete_book import *
from show_book import *
from show_wishlist import *
from show_library import *


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

        add_book_action = QAction(QIcon('../images/add.png'), '&Add Book', self)
        add_book_action.setStatusTip('Add a new book to the library')
        add_book_action.triggered.connect(self.add_book_form_load)

        delete_book_action = QAction(QIcon('../images/delete.png'), '&Delete Book', self)        
        delete_book_action.setStatusTip('Delete a book from the library')
        delete_book_action.triggered.connect(self.delete_book_form_load)

        search_book_action = QAction(QIcon('../images/search.png'), '&Search Book', self)
        search_book_action.setStatusTip('Search for a book in the library')
        search_book_action.triggered.connect(self.search_book_form_load)

        show_library_action = QAction(QIcon('../images/library.png'), '&Show Library', self)
        show_library_action.setStatusTip('Show all books in the Library')
        show_library_action.triggered.connect(self.show_library_form_load)

        show_wishlist_action = QAction(QIcon('../images/whish.png'), '&Show Wishlist', self)
        show_wishlist_action.setStatusTip('Show wishlist')
        show_wishlist_action.triggered.connect(self.wishlist_form_load)

        self.statusBar()

        menubar = self.menuBar()

        book_menu = menubar.addMenu('&Books')
        book_menu.addAction(add_book_action)     
        book_menu.addAction(delete_book_action)

        book_menu = menubar.addMenu('&Library')
        book_menu.addAction(search_book_action)
        book_menu.addAction(show_library_action)

        whishlist_menu = menubar.addMenu('&Wishlist')
        whishlist_menu.addAction(show_wishlist_action)
        
        #self.setFixedSize(self.sizeHint())
        self.setWindowTitle("Bookoholic")
        self.move(QDesktopWidget().availableGeometry().center() -
                  self.frameGeometry().center())

    def add_book_form_load(self):
        self.add_book_form_load = BookForm()
        self.add_book_form_load.show()

    def delete_book_form_load(self):
        self.delete_book_form_load = DeleteForm()
        self.delete_book_form_load.show()

    def search_book_form_load(self):
        self.search_book_form_load = SearchForm()
        self.search_book_form_load.show()

    def show_library_form_load(self):
        self.show_library_form_load = LibraryForm()
        self.show_library_form_load.show()

    def wishlist_form_load(self):
        self.wishlist_form_load = WishlistForm()
        self.wishlist_form_load.show()



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
