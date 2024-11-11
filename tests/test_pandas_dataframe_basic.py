import unittest
import pandas as pd
import numpy as np

class TestPandasBasics(unittest.TestCase):
    def setUp(self):
        number_array = np.arange(12).reshape(3, 4)
        self.df_simple = pd.DataFrame(number_array)
        self.df = pd.DataFrame(number_array, 
                               columns=['col_0', 'col_1', 'col_2', 'col_3'],
                               index=['row_0', 'row_1', 'row_2'])
        
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
        
    def test_df_colums(self):
        self.assertIsInstance(self.df.columns, pd.core.indexes.base.Index)
        
        actual = self.df.columns.tolist()
        expected = ['col_0', 'col_1', 'col_2', 'col_3']
        np.testing.assert_array_equal(actual, expected)
        
        
if __name__ == '__main__':
    unittest.main()