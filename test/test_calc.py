import unittest
from calc import add, subtract, multiply, power, divide

class TestCalc(unittest.TestCase):
    
    # Addition Test
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # Subtraction Test
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 10), 0)
        self.assertEqual(subtract(0, 5), -5)

    # Multiplication Test
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-1, 5), -5)

    # Power Test
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)

    # Division Test
    def test_basic_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(20, 4), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
