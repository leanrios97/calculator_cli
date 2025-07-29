# src\core\calculator.py
from .operations.operation import Operation
from .operation_factory import OperationFactory

class Calculator: 
    def __init__(self, operation_factory: OperationFactory): 
        self._operation_factory = operation_factory

    def calculate(self, a: float, operator: str, b: float) -> float: 
        operation = self._operation_factory.get_operation(operator)
        
        return operation.execute(a, b)