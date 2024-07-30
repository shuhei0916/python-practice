import unittest
import sys
import os

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from  fib import fib

class TestFibonacci(unittest.TestCase):       
    def test_fibonacci_zero(self):
        self.assertEqual(fib(0), 0)
        
    def test_fibonacci_one(self):
        self.assertEqual(fib(1), 1)
 
if __name__ == '__main__':
    unittest.main()