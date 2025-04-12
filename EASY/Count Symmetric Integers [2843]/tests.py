import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "low, high, expected_output",
        [
            (1, 100, 9),               # Números simétricos entre 1 y 100: 11, 22, 33, ..., 99
            (100, 200, 9),            # Otro rango de 3 cifras, pero solo simétricos de 4 cifras se cuentan
            (1, 9, 0),                # Todos con una sola cifra (no simétricos)
            (10, 99, 9),              # Todos de 2 cifras. Simétricos: 11, 22, 33, ..., 99
            (1, 1000, 99),            # Resultado esperado tras contar todos simétricos de 2 y 4 cifras
            (1200, 1233, 1),          # Solo 1221 es simétrico
            (0, 0, 0),                # Caso extremo: rango de un solo número impar (no simétrico)
            (10, 10, 0),              # Solo el número 10, no es simétrico
            (11, 11, 1),              # Solo el número 11, es simétrico
            (1000, 9999, 90),         # Simétricos de 4 cifras en ese rango
        ]
    )
    def test_count_symmetric_integers(self, low, high, expected_output):
        """
        Prueba parametrizada para validar diferentes rangos y sus cantidades de enteros simétricos.

        Args:
            low (int): Límite inferior del rango.
            high (int): Límite superior del rango.
            expected_output (int): Número de enteros simétricos esperados en ese rango.
        """
        assert self.solution.countSymmetricIntegers(low, high) == expected_output
