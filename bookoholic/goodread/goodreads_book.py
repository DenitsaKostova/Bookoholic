import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class GoodReadsBook:
    def __init__(self, *attrs):
        self.isbn = attrs[0]
        self.title = attrs[1]
        self.author = attrs[2]
        self.year = attrs[3]
        self.rating = attrs[4]
        self.url= attrs[5]

    @property
    def get_isbn(self):
        return self.isbn

    @property
    def get_title(self):
        return self.title

    @property
    def get_author(self):
        return self.author

    @property
    def get_year(self):
        return self.year

    @property
    def get_rating(self):
        return self.rating

    @property
    def get_url(self):
        return self.url
