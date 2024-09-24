import pytest
from challenge import Solution  # Asegúrate de que el nombre del archivo donde resides la clase Solution sea "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, True),                     # 2^0
            (2, True),                     # 2^1
            (4, True),                     # 2^2
            (8, True),                     # 2^3
            (16, True),                    # 2^4
            (32, True),                    # 2^5
            (3, False),                    # No es potencia de 2
            (5, False),                    # No es potencia de 2
            (10, False),                   # No es potencia de 2
            (0, False),                    # 0 no es potencia de 2
            (-2, False),                   # Número negativo no es potencia de 2
            (64, True),                    # 2^6
            (1024, True),                  # 2^10
        ]
    )
    def test_is_power_of_two(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función isPowerOfTwo.

        Args:
            n (int): El número que se probará para verificar si es potencia de 2.
            expected_output (bool): El resultado esperado tras aplicar isPowerOfTwo.
        """
        assert self.solution.isPowerOfTwo(n) == expected_output
