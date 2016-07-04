import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tests.validation_tests import *
from tests.model_tests import *

if __name__ == "__main__":
    unittest.main()