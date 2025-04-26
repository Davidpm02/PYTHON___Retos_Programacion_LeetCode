import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, maxValue, expected_output",
        [
            (1, 10, 10),                     # Caso base, un array de longitud 1 con valores entre 1 y 10
            (2, 5, 15),                      # Caso con longitud 2 y valores entre 1 y 5
            (3, 6, 48),                      # Caso con longitud 3 y valores entre 1 y 6
            (4, 7, 150),                     # Caso con longitud 4 y valores entre 1 y 7
            (5, 10, 1020),                   # Caso con longitud 5 y valores entre 1 y 10
            (6, 8, 432),                     # Caso con longitud 6 y valores entre 1 y 8
            (7, 10, 1716),                   # Caso con longitud 7 y valores entre 1 y 10
            (2, 2, 2),                       # Caso pequeño con longitud 2 y valores entre 1 y 2
            (3, 3, 6),                       # Caso pequeño con longitud 3 y valores entre 1 y 3
            (1, 1, 1),                       # Caso donde n = 1 y maxValue = 1
        ]
    )
    def test_ideal_arrays(self, n, maxValue, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función idealArrays.

        Args:
            n (int): Longitud del array.
            maxValue (int): Valor máximo para los elementos del array.
            expected_output (int): El número esperado de arrays ideales, módulo 10^9 + 7.
        """
        assert self.solution.idealArrays(n, maxValue) == expected_output
