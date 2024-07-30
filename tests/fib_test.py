import unittest
import sys
import os
from parameterized import parameterized

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from fib import fib

class TestFibonacci(unittest.TestCase):      
    @parameterized.expand([
        ("test_fibonacci_zero", 0, 0),
        ("test_fibonacci_one", 1, 1),
        ("test_fibonacci_two", 2, 1),
        ("test_fibonacci_three", 3, 2),
    ])
    
    def test_fibonacci(self, name, n, expected):
        self.assertEqual(fib(n), expected)

 
if __name__ == '__main__':
    unittest.main()