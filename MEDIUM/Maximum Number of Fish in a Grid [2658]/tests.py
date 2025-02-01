import pytest
from challenge import Solution  # Asegúrate de que el archivo challenge.py contiene la clase Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected_output",
        [
            ([[1, 2, 3], [0, 0, 0], [7, 8, 9]], 24),    # Caso con varios grupos de peces
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),      # Caso sin peces
            ([[5, 5], [5, 5]], 20),                      # Caso donde todos los elementos son peces
            ([[1]], 1),                                  # Caso con solo un espacio con un pez
            ([[0, 1], [1, 1], [0, 1]], 3),               # Caso donde hay un solo grupo de peces conectados
            ([[3, 1, 2], [2, 0, 1], [1, 2, 3]], 9),      # Caso con peces dispersos en diferentes posiciones
            ([[2, 0, 0], [0, 0, 0], [0, 0, 2]], 2),      # Caso con dos peces aislados
            ([[4, 4, 4, 4], [4, 0, 0, 4], [4, 0, 4, 4]], 16),  # Caso con un grupo grande de peces
        ]
    )
    def test_find_max_fish(self, grid, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método findMaxFish.

        Args:
            grid (List[List[int]]): La cuadrícula que representa la malla de peces.
            expected_output (int): El número esperado de peces en la región conectada más grande.
        """
        assert self.solution.findMaxFish(grid) == expected_output
