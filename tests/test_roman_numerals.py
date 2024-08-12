import unittest
import sys
import os
from parameterized import parameterized

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from roman_numerals import to_roman

class TestRomanNumerals(unittest.TestCase):
    @parameterized.expand([
        ("test_to_roman_one", 1, "I"),
        ("test_to_roman_five", 5, "V"),
        ("test_to_roman_ten", 10, "X"),        
    ])
    def test_to_roman(self, name, n, expected):
        self.assertEqual(to_roman(n), expected)
    
    def test_fail(self):
        self.fail("hge")
        
    # def test_to_roman(self):
    #     self.assertEqual("I", to_roman(1))
    # def test_five(self): 
    #     self.assertEqual("V", to_roman(5))
    # def test_ten(self):
    #     self.assertEqual("X", to_roman(10))
        

if __name__ == '__main__':
    unittest.main()