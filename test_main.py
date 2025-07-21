import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        assert add(2,3) == 5
        assert add(-1,1) == 0
        assert add(7,9) == 16

# If expected output and actual output is same then we will get teh
#result as pass.
# Assert is assertion function which checking
# actual == expected
# if it matches test case passed
# run this I will use libarary called pytest

