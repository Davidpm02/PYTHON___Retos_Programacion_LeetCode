import pytest
from challenge import Solution  # Asegúrate de que el archivo con el código de la clase Solution se llama "challenge.py"


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, edges, expected_output",
        [
            (6, [[0, 1], [0, 2], [1, 2], [3, 4]], 3),  # Caso con 3 componentes completas
            (6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]], 1),  # Caso con 1 componente completa
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0),  # Caso con ninguna componente completa
            (4, [[0, 1], [1, 2], [2, 3], [3, 0]], 1),  # Caso con 1 componente completa (ciclo)
            (3, [[0, 1], [1, 2]], 1),  # Caso con una componente completa (triángulo)
            (7, [[0, 1], [0, 2], [1, 2], [3, 4], [4, 5]], 0),  # Caso con 0 componentes completas
            (3, [[0, 1], [1, 2], [0, 2]], 1),  # Caso con 1 componente completa (triángulo completo)
        ]
    )
    def test_count_complete_components(self, n, edges, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countCompleteComponents.

        Args:
            n (int): El número de vértices en el grafo.
            edges (List[List[int]]): La lista de aristas que conecta los vértices.
            expected_output (int): El número esperado de componentes completas.
        """
        assert self.solution.countCompleteComponents(n, edges) == expected_output
