from pathlib import Path
import unittest

# print(hoge_file)
# print(type(hoge_file))
# print(hoge_file.)
# print(__file__)
# print(Path())

class TestPathlibBasic(unittest.TestCase):
    def setUp(self):
        self.hoge_file = Path('data/hoge.txt')
    
    def test_is_file(self):
        self.assertTrue(self.hoge_file.is_file() )

if __name__ == "__main__":
    unittest.main()