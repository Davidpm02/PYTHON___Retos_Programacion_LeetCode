import pytest
from challenge import Solution  
from typing import List


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected_output",
        [
            ([[1, 2], [2, 4]], [2, 3]),  # El 2 está repetido, falta el 3.
            ([[1, 1], [3, 4]], [1, 2]),  # El 1 está repetido, falta el 2.
            ([[4, 3, 2], [6, 1, 5], [9, 7, 7]], [7, 8]),  # El 7 está repetido, falta el 8.
            ([[9, 7, 8], [6, 6, 4], [3, 2, 1]], [6, 5]),  # El 6 está repetido, falta el 5.
            ([[1, 3, 2], [6, 5, 5], [9, 8, 7]], [5, 4]),  # El 5 está repetido, falta el 4.
        ]
    )
    def test_find_missing_and_repeated_values(self, grid: List[List[int]], expected_output: List[int]):
        """
        Prueba parametrizada para validar diferentes casos de la función findMissingAndRepeatedValues.

        Args:
            grid (List[List[int]]): Matriz cuadrada con valores en el rango [1, n**2].
            expected_output (List[int]): Lista con el número repetido y el número faltante.
        """
        assert self.solution.findMissingAndRepeatedValues(grid) == expected_output