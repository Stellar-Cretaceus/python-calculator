import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(26, 49), 75)
        self.assertEqual(self.calc.add(534, 598), 1132)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 8), -2)
        self.assertEqual(self.calc.subtract(60, 20), 40)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-2, 2), -4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, -3), -2)
        self.assertEqual(self.calc.divide(1, 3), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(-13, -3), -1)
        self.assertEqual(self.calc.modulo(4, -13), -9)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()