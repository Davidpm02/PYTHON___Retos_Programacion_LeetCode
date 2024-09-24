import pytest
from challenge import Solution  

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            (38, 2),          # 3 + 8 = 11 -> 1 + 1 = 2
            (0, 0),           # 0 es un solo dígito
            (9, 9),           # 9 es un solo dígito
            (123, 6),         # 1 + 2 + 3 = 6
            (999, 9),         # 9 + 9 + 9 = 27 -> 2 + 7 = 9
            (10, 1),          # 1 + 0 = 1
            (56, 11),         # 5 + 6 = 11 -> 1 + 1 = 2
            (9875, 2),        # 9 + 8 + 7 + 5 = 29 -> 2 + 9 = 11 -> 1 + 1 = 2
            (999999, 9),      # 9 + 9 + 9 + 9 + 9 + 9 = 54 -> 5 + 4 = 9
        ]
    )
    def test_add_digits(self, num, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función addDigits.

        Args:
            num (int): El número que se probará.
            expected_output (int): El resultado esperado tras aplicar addDigits.
        """
        assert self.solution.addDigits(num) == expected_output
