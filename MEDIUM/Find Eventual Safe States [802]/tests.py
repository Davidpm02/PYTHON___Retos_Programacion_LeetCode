import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "graph, expected_output",
        [
            # Caso base: grafo vacío
            ([], []),

            # Grafo con un solo nodo terminal
            ([[0]], [0]),

            # Grafo lineal sin ciclos
            ([[1], [2], []], [2, 1, 0]),

            # Grafo con ciclo
            ([[1], [2], [0]], []),

            # Grafo con nodos terminales aislados
            ([[1], [], [0], []], [1, 3]),

            # Grafo más complejo con nodos seguros
            ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),

            # Grafo en forma de estrella
            ([[1, 2, 3], [], [], [], []], [1, 2, 3, 0]),

            # Grafo donde todos los nodos son inseguros por un ciclo completo
            ([[1], [2], [3], [0]], []),

            # Grafo grande donde solo uno es seguro
            ([[] for _ in range(100)], list(range(100))),
        ]
    )
    def test_eventual_safe_nodes(self, graph, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función eventualSafeNodes.

        Args:
            graph (List[List[int]]): Lista de adyacencia que representa el grafo.
            expected_output (List[int]): Lista esperada de nodos seguros.
        """
        assert self.solution.eventualSafeNodes(graph) == expected_output
