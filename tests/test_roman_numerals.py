import unittest
import sys
import os
from parameterized import parameterized

# srcディレクトリをパスに追加（本来的なやり方なのか？調査する）
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from roman_numerals import to_roman


class TestRomanNumerals(unittest.TestCase):
    @parameterized.expand([ # parameterizedテストの書き方はまだ今一つ分かっていない部分があるので勉強する
        ("test_to_roman_one", 1, "I"),
        ("test_to_roman_two", 2, "II"),        
        ("test_to_roman_five", 5, "V"),
        ("test_to_roman_ten", 10, "X"),  
              
    ])
    def test_to_roman(self, name, n, expected):
        self.assertEqual(to_roman(n), expected)
            

if __name__ == '__main__':
    unittest.main()