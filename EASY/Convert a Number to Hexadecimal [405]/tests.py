import pytest
from challenge import Solution  # Asumiendo que el código original está en el archivo challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            (26, "1a"),                 # Caso estándar, positivo.
            (-1, "ffffffff"),           # Caso negativo, representado en 32-bits.
            (0, "0"),                   # Caso base, cero.
            (255, "ff"),                # Valor límite positivo dentro de un byte (8 bits).
            (16, "10"),                 # Múltiplo de 16.
            (-2147483648, "80000000"),  # Mínimo de un entero con signo de 32 bits.
            (2147483647, "7fffffff"),   # Máximo de un entero con signo de 32 bits.
        ]
    )
    def test_to_hex(self, num, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función toHex.

        Args:
            num (int): El número a convertir a hexadecimal.
            expected_output (str): La representación hexadecimal esperada.
        """
        assert self.solution.toHex(num) == expected_output
