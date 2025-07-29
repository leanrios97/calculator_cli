# main.py

from src.core.operation_factory import OperationFactory
from src.core.calculator import Calculator
from src.interfaces.cli import CalculatorCLI

if __name__ == "__main__":
    operation_factory = OperationFactory()
    calculator = Calculator(operation_factory)
    cli = CalculatorCLI(calculator)
    cli.run()