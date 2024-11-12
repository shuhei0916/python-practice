import unittest
import pandas as pd
import numpy as np

class TestPandasBasics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 共通データの定義をクラスレベルで行う
        cls.number_array = np.arange(12).reshape(3, 4)
        cls.columns = ['col_0', 'col_1', 'col_2', 'col_3']
        cls.index = ['row_0', 'row_1', 'row_2']

    def setUp(self):
        # クラスレベルのデータを使用してDataFrameを作成
        self.df_simple = pd.DataFrame(self.number_array)
        self.df = pd.DataFrame(self.number_array, columns=self.columns, index=self.index)
        self.df_multi = pd.DataFrame({'col_0': [0, 1, 2], 
                                      'col_1': [0.0, 0.1, 0.2], 
                                      'col_2': ['A', 'B', 'C']})

    def test_dataframe_values_content(self):
        # DataFrameの値が期待通りであることをテスト
        actual = self.df_simple.values
        expected = np.array([[0, 1, 2, 3],
                             [4, 5, 6, 7],
                             [8, 9, 10, 11]])
        np.testing.assert_array_equal(actual, expected, err_msg="df_simpleの値が期待と一致しません")

    def test_df_simple_values_type(self):
        # DataFrameのvalues属性がndarrayであることをテスト
        self.assertIsInstance(self.df_simple.values, np.ndarray, "df_simple.valuesはnp.ndarrayではありません")
        
    def test_df_columns_content(self):
        # dfのカラム名が期待通りであることをテスト
        actual = self.df.columns.tolist()
        expected = self.columns
        np.testing.assert_array_equal(actual, expected, err_msg="カラム名が期待と一致しません")
        
    def test_df_columns_type(self):
        # dfのカラム名の型がIndexであることをテスト
        self.assertIsInstance(self.df.columns, pd.Index, "df.columnsはpd.Index型ではありません")

    def test_df_col_1_type(self):
        self.assertIsInstance(self.df['col_1'], pd.core.series.Series)
        
    def test_df_elem(self):
        self.assertEqual(self.df.at['row_0', 'col_1'], 1)
        
    def test_df_multi_types(self):
        self.assertEqual(self.df_multi['col_1'].dtype, np.float64)

if __name__ == '__main__':
    unittest.main()
