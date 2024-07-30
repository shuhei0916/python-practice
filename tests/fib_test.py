import unittest
import sys
import os

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from  fib import fib

class TestFibonacci(unittest.TestCase):       
    def test_fibonacci_zero(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()