import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "boxes, expected_output",
        [
            ("110", [1, 1, 3]),  # Ejemplo con cajas y bolas en posiciones específicas
            ("001", [3, 1, 0]),  # Ejemplo con solo algunas cajas ocupadas
            ("0000", [0, 0, 0, 0]),  # Ejemplo sin bolas
            ("111", [0, 0, 0]),  # Ejemplo con todas las cajas ocupadas
            ("101", [2, 0, 2]),  # Ejemplo con bolas distribuidas a través de las cajas
            ("0101", [2, 0, 2, 2]),  # Más bolas distribuidas, diferentes movimientos requeridos
            ("1001001", [6, 4, 2, 2, 4, 6, 6, 7]),  # Caso más complejo con distribución variada de bolas
            ("1", [0])  # Caso con solo una caja ocupada
        ]
    )
    def test_min_operations(self, boxes, expected_output):
        """
        Prueba parametrizada para validar la función minOperations.

        Args:
            boxes (str): La cadena que representa el estado de las cajas y bolas.
            expected_output (List[int]): El resultado esperado con las operaciones mínimas necesarias para cada caja.
        """
        assert self.solution.minOperations(boxes) == expected_output
