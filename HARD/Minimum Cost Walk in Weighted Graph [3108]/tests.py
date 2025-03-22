import pytest
from challenge import Solution  # Importamos la clase Solution desde challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, edges, query, expected_output",
        [
            (4, [[0, 1, 3], [1, 2, 2], [2, 3, 4]], [[0, 3], [1, 2]], [0, 2]),
            (3, [[0, 1, 1], [1, 2, 1]], [[0, 2], [1, 2]], [1, 1]),
            (5, [[0, 1, 7], [1, 2, 5], [2, 3, 3], [3, 4, 1]], [[0, 4], [2, 4]], [1, 1]),
            (3, [[0, 1, 2], [1, 2, 3]], [[0, 2], [0, 1]], [2, 2]),
            (4, [[0, 1, 8], [2, 3, 6]], [[0, 2], [1, 3]], [-1, -1]),
        ]
    )
    def test_minimum_cost(self, n, edges, query, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minimumCost.

        Args:
            n (int): Número de nodos en el grafo.
            edges (List[List[int]]): Lista de aristas representadas como [u, v, w].
            query (List[List[int]]): Lista de consultas representadas como [s, t].
            expected_output (List[int]): Resultado esperado de la función minimumCost.
        """
        assert self.solution.minimumCost(n, edges, query) == expected_output
