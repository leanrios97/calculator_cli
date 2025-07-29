from .operation import Operation

class Division(Operation): 
    def execute(self, a: float, b: float) -> float: 
        if b == 0: 
            raise ValueError("No se puede dividir por cero.")
        
        return a / b