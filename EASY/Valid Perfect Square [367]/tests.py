import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            (16, True),        # 16 es un cuadrado perfecto (4*4)
            (25, True),        # 25 es un cuadrado perfecto (5*5)
            (14, False),       # 14 no es un cuadrado perfecto
            (1, True),         # 1 es un cuadrado perfecto (1*1)
            (0, True),         # 0 es un cuadrado perfecto (0*0)
            (100, True),       # 100 es un cuadrado perfecto (10*10)
            (101, False),      # 101 no es un cuadrado perfecto
            (2147395600, True),# 2147395600 es un cuadrado perfecto (46340*46340)
            (2147483647, False),# 2147483647 no es un cuadrado perfecto (máximo entero de 32 bits)
        ]
    )
    def test_is_perfect_square(self, num, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método isPerfectSquare.

        Args:
            num (int): El número que se comprobará si es un cuadrado perfecto.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.isPerfectSquare(num) == expected_output
