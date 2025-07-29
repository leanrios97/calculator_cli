import unittest
from src.core.calculator import Calculator
from src.core.operation_factory import OperationFactory

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.factory = OperationFactory()
        self.calculator = Calculator(self.factory)

    def test_calculate_addition(self):
        result = self.calculator.calculate(5, '+', 3)
        self.assertEqual(result, 8)

    def test_calculate_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate(5, '/', 0)

if __name__ == '__main__':
    unittest.main()