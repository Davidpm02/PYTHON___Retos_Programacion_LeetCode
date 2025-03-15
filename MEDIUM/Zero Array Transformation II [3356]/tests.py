import pytest
from challenge import Solution  # Importamos la clase Solution desde el archivo del reto

class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, queries, expected_output",
        [
            ([4, 2, 3], [[0, 1, 2], [1, 2, 2], [0, 2, 1]], 2),  # Se necesitan 2 consultas para hacer nums cero
            ([5, 5, 5], [[0, 2, 3], [0, 2, 2]], 2),  # Se necesitan ambas consultas
            ([1, 1, 1], [[0, 1, 1], [1, 2, 1]], 2),  # Se requiere aplicar ambas consultas
            ([0, 0, 0], [[0, 2, 1]], 0),  # Ya es una matriz cero
            ([10, 20, 30], [[0, 1, 10], [1, 2, 20]], -1),  # No es posible hacer todo cero
        ]
    )
    def test_min_zero_array(self, nums, queries, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minZeroArray.

        Args:
            nums (List[int]): La lista de números de entrada.
            queries (List[List[int]]): Lista de operaciones permitidas.
            expected_output (int): El número mínimo de consultas necesarias o -1 si no es posible.
        """
        assert self.solution.minZeroArray(nums, queries) == expected_output