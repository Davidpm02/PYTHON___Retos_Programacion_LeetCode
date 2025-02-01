import pytest
from challenge import Solution  # Asegúrate de que el archivo challenge.py contiene la clase Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "edges, expected_output",
        [
            ([[1, 2], [1, 3], [2, 3]], [2, 3]),  # Caso donde la conexión redundante es [2, 3]
            ([[1, 2], [2, 3], [3, 4], [1, 4]], [1, 4]),  # Caso con una única conexión redundante
            ([[1, 2], [2, 3], [3, 4], [1, 3]], [1, 3]),  # Otra arista redundante
            ([[1, 2], [1, 3], [3, 4], [1, 4], [2, 4]], [2, 4]),  # Caso con múltiples conexiones redundantes
            ([[1, 2], [2, 3], [3, 4], [4, 1]], [4, 1]),  # La redundante es la conexión [4, 1]
            ([[1, 2], [1, 3], [2, 4], [3, 4]], [3, 4]),  # El ciclo se forma con [3, 4]
            ([[1, 2], [1, 3], [2, 3], [1, 4]], [1, 4]),  # La arista redundante es [1, 4]
            ([[1, 2], [3, 4], [5, 6], [1, 3], [2, 5]], [1, 3])  # Redundante es la conexión [1, 3]
        ]
    )
    def test_find_redundant_connection(self, edges, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método findRedundantConnection.

        Args:
            edges (List[List[int]]): Lista de aristas en el grafo.
            expected_output (List[int]): La arista redundante esperada.
        """
        assert self.solution.findRedundantConnection(edges) == expected_output
