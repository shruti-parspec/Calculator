import unittest
from calc import add, subtract, multiply, divide, power, modulus


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(10.5, 2.5), 13.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, 3), -8)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-5, 3), -15)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(10, 4), 2.5)
        self.assertEqual(divide(-10, 2), -5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(-2, 2), 4)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)
        self.assertEqual(modulus(-10, 3), 2)

    def test_modulus_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulus(10, 0)


if __name__ == "__main__":
    unittest.main()
