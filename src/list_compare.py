import unittest

class TestListCompare(unittest.TestCase):
    
    def test_list_less_than(self):
        self.assertTrue([1, 2, 3] < [1, 2, 5], "Test failed: [1, 2, 3] should be less than [1, 2, 5]")
        self.assertFalse([100] < [1, 2, 3], "Test failed: [100] should not be less than [1, 2, 3]")
        self.assertTrue([1, 2] < [1, 2, 3], "Test failed: [1, 2] should be less than [1, 2, 3]")
    
    def test_tuple_less_than(self):
        self.assertTrue((1, 2, 3) < (1, 2, 5), "Test failed: (1, 2, 3) should be less than (1, 2, 5)")
    
    def test_mixed_type_list(self):
        with self.assertRaises(TypeError):
            _ = [1, '2', 3] < [1, 2, 3]
            
    def test_different_length_lists(self):
        self.assertTrue([1, 2, 3] < [1, 2, 3, 4], "Test failed: [1, 2, 3] should be less than [1, 2, 3, 4]")
    
    def test_list_equality(self):
        self.assertEqual([1, 2, 3], [1, 2, 3], "Test failed: [1, 2, 3] should be equal to [1, 2, 3]")

if __name__ == "__main__":
    unittest.main()
