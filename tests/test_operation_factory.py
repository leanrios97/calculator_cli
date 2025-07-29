import unittest
from src.core.operation_factory import OperationFactory
from src.core.operations.addition import Addition

class TestOperationFactory(unittest.TestCase):
    def setUp(self):
        self.factory = OperationFactory()

    def test_get_operation(self):
        op = self.factory.get_operation('+')
        self.assertIsInstance(op, Addition)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.factory.get_operation('%')

if __name__ == '__main__':
    unittest.main()