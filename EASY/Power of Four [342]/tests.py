import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, True),          # 4^0 = 1 es potencia de 4
            (4, True),          # 4^1 = 4 es potencia de 4
            (16, True),         # 4^2 = 16 es potencia de 4
            (64, True),         # 4^3 = 64 es potencia de 4
            (5, False),         # 5 no es potencia de 4
            (15, False),        # 15 no es potencia de 4
            (0, False),         # 0 no es potencia de 4
            (-4, False),       # Números negativos no son potencias
            (2, False),         # 2 no es potencia de 4
            (8, False),         # 8 no es potencia de 4
        ]
    )
    def test_is_power_of_four(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función isPowerOfFour.

        Args:
            n (int): El entero que se probará si es potencia de 4.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.isPowerOfFour(n) == expected_output
