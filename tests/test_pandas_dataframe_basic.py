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
        # self.assertEqual(actual, expected)
        np.testing.assert_array_equal(actual, expected)
        
if __name__ == '__main__':
    unittest.main()