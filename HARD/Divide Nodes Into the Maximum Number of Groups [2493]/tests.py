import pytest
from challenge import Solution  # Asegúrate de que el archivo del reto se llame 'challenge.py'

class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, edges, expected_output",
        [
            (3, [[1, 2], [2, 3]], 2),  # Grafo lineal simple
            (4, [[1, 2], [2, 3], [3, 4]], 2),  # Grafo lineal más largo
            (3, [[1, 2], [2, 3], [3, 1]], -1),  # Grafo cíclico impar (no bipartito)
            (5, [[1, 2], [1, 3], [3, 4], [4, 5]], 3),  # Grafo con ramas
            (6, [[1, 2], [2, 3], [4, 5], [5, 6]], 4),  # Dos componentes separados
            (1, [], 1),  # Un solo nodo, un solo grupo
            (2, [[1, 2]], 2),  # Dos nodos conectados (bipartito)
            (4, [[1, 2], [2, 3], [3, 4], [4, 1]], -1),  # Ciclo par, no bipartito
            (4, [[1, 2], [3, 4]], 2),  # Dos componentes bipartitos separados
        ]
    )
    def test_magnificent_sets(self, n, edges, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función magnificentSets.

        Args:
            n (int): Número de nodos en el grafo.
            edges (List[List[int]]): Lista de aristas del grafo.
            expected_output (int): El número máximo de grupos esperados.
        """
        assert self.solution.magnificentSets(n, edges) == expected_output
