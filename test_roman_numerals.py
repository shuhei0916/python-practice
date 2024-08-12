import unittest
from roman_numerals import to_roman

class TestRomanNumerals(unittest.TestCase):
    def test_to_roman(self):
        expected = "I"
        actual = to_roman(1)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()