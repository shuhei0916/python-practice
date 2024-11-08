import unittest
import pandas as pd
import numpy as np

class TestPandasBasics(unittest.TestCase):
    def setUp(self):
        self.df_simple = pd.DataFrame(np.arange(12).reshape(3, 4))
        
    def test_version(self):
        self.assertEqual(pd.__version__, '2.2.3') 
    
        
        
if __name__ == '__main__':
    unittest.main()