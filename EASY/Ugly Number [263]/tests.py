import pytest
from challenge import Solution  # Se asume que el archivo del reto se llama challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (6, True),     # 6 es un número feo: 6 = 2 * 3
            (8, True),     # 8 es un número feo: 8 = 2 * 2 * 2
            (14, False),   # 14 no es un número feo: tiene 7 como factor
            (1, True),     # 1 es considerado feo por definición
            (0, False),    # 0 no es un número feo
            (30, True),    # 30 es un número feo: 30 = 2 * 3 * 5
            (25, True),    # 25 es un número feo: 25 = 5 * 5
            (37, False),   # 37 no es un número feo: es primo
        ]
    )
    def test_is_ugly(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función isUgly.

        Args:
            n (int): Número entero que será evaluado.
            expected_output (bool): Resultado esperado.
        """
        assert self.solution.isUgly(n) == expected_output
