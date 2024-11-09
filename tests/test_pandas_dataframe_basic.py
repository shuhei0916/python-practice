import unittest
import pandas as pd
import numpy as np

class TestPandasBasics(unittest.TestCase):
    def setUp(self):
        self.df_simple = pd.DataFrame(np.arange(12).reshape(3, 4))
        
    def test_version(self):
        self.assertEqual(pd.__version__, '2.2.3') 
    
    def test_dataframe_value(self):
        actual = self.df_simple.values
        expected = np.array([[0, 1, 2, 3],
                             [4, 5, 6, 7],
                             [8, 9, 10, 11]])
        # self.assertEqual(actual, expected) # これだとエラー!
        np.testing.assert_array_equal(actual, expected)
    
    def test_values_type(self):
        self.assertIsInstance(self.df_simple.values, np.ndarray)
        
class TestExample(unittest.TestCase):
    def test_is_instance(self):
        num = 10
        self.assertIsInstance(num, int)
        
        
if __name__ == '__main__':
    unittest.main()