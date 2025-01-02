import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution desde tu reto

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "x, expected_output",
        [
            (4, 2),        # Caso simple, la raíz cuadrada de 4 es 2
            (9, 3),        # La raíz cuadrada de 9 es 3
            (16, 4),       # La raíz cuadrada de 16 es 4
            (0, 0),        # Caso especial para 0, la raíz cuadrada de 0 es 0
            (1, 1),        # La raíz cuadrada de 1 es 1
            (8, 2),        # Raíz cuadrada de 8, el valor más cercano en enteros es 2
            (25, 5),       # Raíz cuadrada de 25 es 5
            (100, 10),     # Raíz cuadrada de 100 es 10
            (15, 3),       # Raíz cuadrada de 15, el valor más cercano en enteros es 3
            (10, 3),       # Raíz cuadrada de 10, también 3 porque el valor exacto es 3.16
            (30, 5),       # Raíz cuadrada de 30, el valor más cercano es 5
        ]
    )
    def test_my_sqrt(self, x, expected_output):
        """
        Prueba parametrizada para validar la función mySqrt.

        Args:
            x (int): El valor sobre el cual se calculará la raíz cuadrada.
            expected_output (int): La raíz cuadrada esperada (valor entero).
        """
        result = self.solution.mySqrt(x)
        assert result == expected_output
