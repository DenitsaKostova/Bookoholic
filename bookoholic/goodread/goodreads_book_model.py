import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PyQt5.QtCore import QAbstractItemModel, Qt, QVariant, QModelIndex
from PyQt5.QtWidgets import QTableView, QAbstractScrollArea, QApplication

from goodread.goodreads_book import *

COLUMNS = 6


class GoodReadsBookModel(QAbstractItemModel):
    def __init__(self):
        super(GoodReadsBookModel, self).__init__()
        self.books = []

    def set_books(self, books):
        self.beginResetModel()
        self.books = books
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        return len(self.books)

    def columnCount(self, parent=QModelIndex()):
        return COLUMNS

    def data(self, index, role):
        if (not self.hasIndex(index.row(), index.column()) or
           role != Qt.DisplayRole):
            return QVariant()

        book = self.books[index.row()]

        getters = ('get_isbn', 'get_title', 'get_author', 'get_year',
                   'get_rating', 'get_url')

        if index.column() < self.columnCount():
            return getattr(book, getters[index.column()])

        return QVariant()

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Vertical:
            if not self.is_valid_row_index(section):
                return QVariant()
            else:
                return section + 1
        if orientation == Qt.Horizontal:
            if not self.is_valid_column_index(section):
                return QVariant()
            else:
                return ('ISBN', 'Title', 'Author', 'Year',
                        'Rating', 'Goodreads url')[section]
        return QVariant()

    def index(self, row, column, parent=QModelIndex()):
        if self.is_valid_row_index(row) and\
           self.is_valid_column_index(column):
            return self.createIndex(row, column)
        else:
            return QModelIndex()

    def is_valid_row_index(self, row_index):
        return 0 <= row_index and row_index < self.rowCount()

    def is_valid_column_index(self, column_index):
        return 0 <= column_index and column_index < self.columnCount()

    def parent(self, child):
        return QModelIndex()
