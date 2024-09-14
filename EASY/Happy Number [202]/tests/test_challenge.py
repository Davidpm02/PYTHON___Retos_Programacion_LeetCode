import pytest
from challenge import Solution  # Asegúrate de que el archivo con la clase Solution se llame "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_number, expected_output",
        [
            (19, True),        # 19 es un número feliz
            (2, False),        # 2 no es un número feliz
            (7, True),         # 7 es un número feliz
            (4, False),        # 4 no es un número feliz
            (1, True),         # 1 es un número feliz
            (100, True),       # 100 es un número feliz
            (123456789, False) # 123456789 no es un número feliz
        ]
    )
    def test_is_happy(self, input_number, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función isHappy.

        Args:
            input_number (int): El número entero que se probará si es un número feliz.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.isHappy(input_number) == expected_output
