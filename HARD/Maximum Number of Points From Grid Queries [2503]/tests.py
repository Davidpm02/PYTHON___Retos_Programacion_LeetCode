import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, queries, expected_output",
        [
            (
                [[1, 2, 4], [3, 4, 3], [2, 1, 2]],
                [2, 3, 4],
                [1, 5, 6],
            ),  # Caso de prueba estándar con valores crecientes en la grilla
            (
                [[5, 1], [4, 6]],
                [1, 5],
                [0, 3],
            ),  # Caso con valores dispersos
            (
                [[10]],
                [5, 10, 15],
                [0, 0, 1],
            ),  # Caso borde con una grilla 1x1
            (
                [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                [1, 2],
                [0, 9],
            ),  # Caso con una grilla uniforme
            (
                [[7, 3, 8], [2, 6, 5], [9, 4, 1]],
                [3, 7, 9],
                [1, 7, 9],
            ),  # Caso con una distribución irregular
        ]
    )
    def test_maxPoints(self, grid, queries, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maxPoints.

        Args:
            grid (List[List[int]]): Matriz de enteros representando la grilla.
            queries (List[int]): Lista de valores de consulta.
            expected_output (List[int]): Resultado esperado.
        """
        assert self.solution.maxPoints(grid, queries) == expected_output