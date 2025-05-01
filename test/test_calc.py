import unittest
from calc import add, subtract

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        from calc import multiply
        self.assertEqual(multiply(4, 5), 20)

