import re
import sys
from functools import *

VALID_YEAR = r'^\d{4}$'

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
    def is_valid_isbn(cls, isbn):
        formated_isbn = isbn.replace('-', '')
        if len(formated_isbn) == 10:
            try:
                checksum = str(11 - (sum(int(formated_isbn[i]) * (10 - i) for i in range(8)) % 11))
            except ValueError:
                return False

            if checksum == '11':
                checksum = '0'  
            elif checksum == '10':
                checksum = 'X'  
            if checksum == isbn[9]:
                return True
            else:
                return False

        elif len(formated_isbn) == 13:
            try:
                checksum = str(10 - (sum(int(formated_isbn[i]) + int(formated_isbn[i+1])*3 for i in range(0,11,2))%10))
               
            except ValueError:
                return False
            if checksum == '10': 
                checksum = '0'  
            if checksum == isbn[12]:
                return True
            else:
                return False
        else:
            return False

print(Validations.is_valid_isbn('9780545582957'))
range(0,10)
