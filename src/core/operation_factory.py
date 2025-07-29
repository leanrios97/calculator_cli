# src/core/operation_factory.py
from typing import Dict
from .operations.operation import Operation
from .operations.addition import Addition   
from .operations.subtraction import Subtraction
from .operations.multiplication import Multiplication
from .operations.division import Division

class OperationFactory:
    def __init__(self):
        self._operations: Dict[str, Operation] = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division()
        }

    def get_operation(self, operator: str) -> Operation:
        if operator not in self._operations:
            raise ValueError(f"Operador no soportado: {operator}")
        return self._operations[operator]