import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, k, expected_output",
        [
            (1, 4, 2),         # Solo dígitos de un solo dígito que sean divisibles por 4 y palindrómicos
            (3, 5, 27),        # Caso clásico del ejemplo: n = 3, k = 5
            (5, 6, 2468),      # Caso con mayor número de dígitos, n impar
            (2, 1, 90),        # Todos los palíndromos de 2 dígitos son buenos si k = 1
            (2, 11, 9),        # Solo palíndromos dobles divisibles por 11
            (3, 1, 252),       # Todos los palíndromos de 3 dígitos son válidos si k = 1
            (4, 2, 90),        # Número par de dígitos, divisible entre 2
            (4, 3, 75),        # Número par de dígitos, divisible entre 3
            (1, 1, 9),         # Todos los dígitos del 1 al 9 son buenos si k = 1
            (1, 9, 1),         # Solo el 9 es divisible por 9
        ]
    )
    def test_count_good_integers(self, n, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método countGoodIntegers.

        Args:
            n (int): Número de dígitos que debe tener el entero.
            k (int): Divisor para determinar si el palíndromo es válido.
            expected_output (int): El número esperado de enteros "good".
        """
        assert self.solution.countGoodIntegers(n, k) == expected_output
