# src/interfaces/cli.py
from src.core.calculator import Calculator

class CalculatorCLI: 
    def __init__(self, calculator: Calculator): 
        self._calculator = calculator
    
    def run(self): 
        print("Bienvenido a la calculadora CLI")
        print("Escriba 'salir' para terminar")
        print("Operadores soportados: +, -, *, /")

        while True:
            try: 
                user_input = input("Ingrese operacion (ejemplo: 2 + 3): ")
                if user_input.lower() == 'salir': 
                    print("Adios!!")
                    break
                
                parts = user_input.split()
                if len(parts) != 3:
                    print("Entrada invalida. Formato: <numero1> <operador> <numero2>")
                    continue

                a, operator, b = float(parts[0]), parts[1], float(parts[2])
                result = self._calculator.calculate(a, operator, b)

                print(f"Resultado: {result}")
            
            except ValueError as e:
                print(f"Error: {e}")
            
            except Exception as e:
                print(f"Error inesperado: {e}")