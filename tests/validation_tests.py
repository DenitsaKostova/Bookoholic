import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from bookoholic.validation_utils import Validations


class ValidationTest(unittest.TestCase):
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

    def test_valid_year(self):
        self.assertTrue(Validations.is_valid_year('1942'))
        self.assertTrue(Validations.is_valid_year('1888'))
        self.assertTrue(Validations.is_valid_year('1111'))
        self.assertFalse(Validations.is_valid_year('xed'))
        self.assertFalse(Validations.is_valid_year('42.42'))
        self.assertFalse(Validations.is_valid_year('421'))

    def test_valid_isbn(self):
        self.assertFalse(Validations.is_valid_isbn('1234567890'))
        self.assertFalse(Validations.is_valid_isbn('dewf'))
        self.assertFalse(Validations.is_valid_isbn('12213'))
        self.assertFalse(Validations.is_valid_isbn('123456789'))
        self.assertTrue(Validations.is_valid_isbn('9781400064755'))
        self.assertTrue(Validations.is_valid_isbn('1400064759'))
        self.assertTrue(Validations.is_valid_isbn('9780316015844'))
       