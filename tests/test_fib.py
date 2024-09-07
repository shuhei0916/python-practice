"""
python -m unittest tests.test_fib のように実行してください。
直接 python tests/test_fib.py のようには実行できません。
pythonでは実行されたファイルのディレクトリ（ここでは./tests）がトップレベルの階層として扱われ、
それより上の階層にさかのぼってパッケージをimportすることが出来ないためです。
参考: https://qiita.com/hoto17296/items/fa0166728177e676cd36
"""

import unittest
import sys
import os
from parameterized import parameterized
from src.fib import fib

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