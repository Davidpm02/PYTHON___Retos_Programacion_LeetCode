import pytest
from challenge import Solution  # Asegúrate de que el archivo del reto se llame 'challenge.py'

class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected_output",
        [
            ([[1, 0], [0, 1]], 3),  # Convertir un 0 en 1 conecta dos islas
            ([[1, 1], [1, 0]], 4),  # Convertir un 0 en 1 expande la isla existente
            ([[1, 1], [1, 1]], 4),  # No hay ceros, la isla más grande ya está completa
            ([[0, 0], [0, 0]], 1),  # Convertir cualquier 0 en 1 crea una isla de tamaño 1
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 5),  # Un solo cambio conecta varias islas
        ]
    )
    def test_largest_island(self, grid, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función largestIsland.

        Args:
            grid (List[List[int]]): Matriz representando la isla con 1s y 0s.
            expected_output (int): El tamaño máximo esperado de la isla tras cambiar un 0 a 1.
        """
        assert self.solution.largestIsland(grid) == expected_output