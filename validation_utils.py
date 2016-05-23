import re

VALID_YEAR = r'^\d{4}$'
VALID_ISBN = r'^(97(8|9))?\d{9}(\d|X)$'

class Validations:
    @classmethod
    def equal(cls, pattern, value):
        match = re.search(pattern, value)
        if not match:
            return False
        start, end = match.span()
        if value[start:end] == value:
            return True
        return False

    @classmethod
    def is_valid_year(cls, value):
        return Validations.equal(VALID_YEAR, value)

    @classmethod
    def is_valid_isbn(cls, value):
        return Validations.equal(VALID_ISBN, value)
