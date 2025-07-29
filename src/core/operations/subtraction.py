# src\core\operations\subtraction.py
from .operation import Operation

class Subtraction(Operation): 
    def execute(self, a: float, b: float) -> float:
        return a - b