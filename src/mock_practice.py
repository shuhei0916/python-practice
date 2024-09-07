from unittest.mock import MagicMock
import unittest


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

class TestProduction(unittest.TestCase):
    def test_hoge(self):
        real = ProductionClass()
        real.something = MagicMock()
        real.method()
        hoge = real.something.assert_called_once_with(1, 2, 5)


if __name__ == "__main__":
    unittest.main()