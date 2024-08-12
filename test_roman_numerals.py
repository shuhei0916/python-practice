import unittest
from roman_numerals import to_roman

class TestRomanNumerals(unittest.TestCase):
    def test_to_roman(self):
        self.assertEqual("I", to_roman(1))
        
    def test_five(self): 
        self.assertEqual("V", to_roman(5))
        

if __name__ == '__main__':
    unittest.main()