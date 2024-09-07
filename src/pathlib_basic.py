from pathlib import Path
import unittest
import os

"""
pathlibの使い方の練習用コード
https://note.nkmk.me/python-pathlib-usage/#path_1
"""

def main():
    current_dir = Path(__file__).parent
    print(current_dir)
    print(type(current_dir))
    
    current_dir = os.getcwd()
    print(current_dir)
    print(type(current_dir))
    
    current_dir = Path.cwd()
    print(current_dir)
    print(type(current_dir))
    
    hoge_file_path = current_dir / 'data' / 'hoge.txt'    
    print(hoge_file_path)


class TestPathlibBasic(unittest.TestCase):
    def setUp(self):
        self.hoge_file_path = Path('data/hoge.txt')
        self.nonexistent_file_path = Path('data/noexistence.txt')
    
    def test_is_file(self):
        self.assertTrue(self.hoge_file_path.is_file())
        
    def test_check_suffix(self):
        self.assertEqual(self.hoge_file_path.suffix, '.txt')
        
    def test_nonexistent_file(self):
        self.assertFalse(self.nonexistent_file_path.exists())
    
    def test_cwd(self):
        actual = str(Path.cwd())
        # actual = str(Path(__file__).parent) # これでもよい
        expected = '/home/shuhei0916/projects/python-practice'
        self.assertEqual(actual, expected)
    
    def test_cat_path(self):
        current_dir = Path.cwd()
        joined_file_path = current_dir / 'data' / 'hoge.txt'
        # joined_file_path = current_dir.joinpath('data', 'hoge.txt') # これでもよい
        self.assertTrue(self.hoge_file_path.samefile(joined_file_path))
        

if __name__ == "__main__":
    TEST_MODE = True
    
    if TEST_MODE:
        unittest.main()
    else:  
        main()
    