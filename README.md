# Calculadora CLI

Una calculadora de línea de comandos escrita en Python que realiza operaciones matemáticas básicas (suma, resta, multiplicación, división) siguiendo principios SOLID y patrones de diseño como Strategy y Factory.

## Características
- Operaciones soportadas: suma (+), resta (-), multiplicación (*), división (/).
- Arquitectura modular y escalable.
- Cumple con los principios SOLID.
- Incluye pruebas unitarias para verificar el comportamiento.
- Interfaz de usuario simple en consola.

## Requisitos
- Python 3.6 o superior.
- Opcional: `pytest` para ejecutar pruebas unitarias con más funcionalidades.

## Instalación
1. Clona o descarga el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd calculadora_cli
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias (si usas pytest):
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Ejecuta la calculadora:
   ```bash
   python main.py
   ```
2. Sigue las instrucciones en pantalla:
   - Ingresa operaciones en el formato `<número> <operador> <número>` (ej. `5 + 3`).
   - Escribe `salir` para terminar.

Ejemplo de interacción:
```
Calculadora CLI (escribe 'salir' para terminar)
Operadores disponibles: +, -, *, /
Ingresa operación (ej: 5 + 3) o 'salir': 10 + 5
Resultado: 15.0
Ingresa operación (ej: 5 + 3) o 'salir': salir
¡Adiós!
```

## Estructura del proyecto
```
calculadora_cli/
├── src/
│   ├── core/
│   │   ├── operations/
│   │   │   ├── __init__.py
│   │   │   ├── operation.py
│   │   │   ├── addition.py
│   │   │   ├── subtraction.py
│   │   │   ├── multiplication.py
│   │   │   └── division.py
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   └── operation_factory.py
│   ├── interfaces/
│   │   ├── __init__.py
│   │   └── cli.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_operations.py
│   ├── test_calculator.py
│   └── test_operation_factory.py
├── main.py
├── README.md
└── requirements.txt
```

- `src/core/`: Lógica de negocio (operaciones, calculadora, fábrica).
- `src/interfaces/`: Interfaz de usuario (CLI).
- `tests/`: Pruebas unitarias.
- `main.py`: Punto de entrada de la aplicación.

## Ejecutar pruebas
1. Usando `unittest` (incluido en Python):
   ```bash
   python -m unittest discover -s tests -v
   ```
2. Usando `pytest` (requiere instalación):
   ```bash
   pytest tests/ -v
   ```

## Extender el proyecto
Para agregar una nueva operación (ej. potencia):
1. Crea una nueva clase en `src/core/operations/` (ej. `power.py`):
   ```python
   from .operation import Operation

   class Power(Operation):
       def execute(self, a: float, b: float) -> float:
           return a ** b
   ```
2. Actualiza `src/core/operations/__init__.py`:
   ```python
   from .power import Power
   ```
3. Registra la operación en `src/core/operation_factory.py`:
   ```python
   self._operations['^'] = Power()
   ```

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, abre un *issue* o un *pull request* en el repositorio.

## Licencia
MIT License