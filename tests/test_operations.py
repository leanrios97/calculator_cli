# tests/test_operations.py
import unittest
from src.core.operations.addition import Addition
from src.core.operations.subtraction import Subtraction
from src.core.operations.multiplication import Multiplication
from src.core.operations.division import Division

class TestOperations(unittest.TestCase):
    def test_addition(self):
        add = Addition()
        self.assertEqual(add.execute(2, 3), 5)
        self.assertEqual(add.execute(-1, 1), 0)
        self.assertEqual(add.execute(0, 0), 0)
    
    def test_subtraction(self):
        sub = Subtraction()
        self.assertEqual(sub.execute(5, 3), 2)
        self.assertEqual(sub.execute(0, 1), -1)
        self.assertEqual(sub.execute(-1, -1), 0)

    def test_multiplication(self):
        mul = Multiplication()
        self.assertEqual(mul.execute(3, 4), 12)
        self.assertEqual(mul.execute(-2, 5), -10)
        self.assertEqual(mul.execute(0, 100), 0)
    
    def test_division(self):
        div = Division()
        self.assertEqual(div.execute(10, 2), 5)
        self.assertEqual(div.execute(-6, -2), 3)
        self.assertEqual(div.execute(0, 1), 0)