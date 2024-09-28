import pytest
from challenge import Solution  # Se asume que el archivo del reto se llama challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (27, True),   # 27 es potencia de 3 (3^3)
            (9, True),    # 9 es potencia de 3 (3^2)
            (1, True),    # 1 es una potencia de 3 (3^0)
            (0, False),   # 0 no es una potencia de 3
            (-3, False),  # Los números negativos no son potencias de 3
            (10, False),  # 10 no es potencia de 3
            (243, True),  # 243 es potencia de 3 (3^5)
            (45, False),  # 45 no es potencia de 3
        ]
    )
    def test_is_power_of_three(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función isPowerOfThree.

        Args:
            n (int): Número entero que será evaluado.
            expected_output (bool): Resultado esperado.
        """
        assert self.solution.isPowerOfThree(n) == expected_output
