import pytest
from challenge import Solution  # Importo la clase Solution del fichero challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "edges, node1, node2, expected_output",
        [
            # Caso base: grafo sin aristas, ambos nodos iguales
            ([-1], 0, 0, 0),

            # Grafo simple lineal con un nodo común reachable
            ([1, 2, -1], 0, 1, 1),

            # Grafo con nodo común reachable, pero con varios caminos
            ([2, 2, 3, -1], 0, 1, 2),

            # Grafo donde no existe nodo común reachable
            ([2, 2, 3, -1], 0, 3, -1),

            # Caso con ciclo, para validar no bucles infinitos
            ([1, 2, 0], 0, 2, 0),

            # Caso con múltiples nodos comunes, devuelve el de índice más pequeño
            ([2, 2, 3, -1, 3], 0, 4, 3),

            # Grafo con nodos que no se pueden alcanzar desde ninguno de los dos nodos iniciales
            ([2, -1, 3, 4, -1], 0, 1, 3),

            # Grafo con un nodo común al final del camino, pero distancias diferentes
            ([4, 4, 4, 4, -1], 0, 2, 4),

            # Caso con nodos desconectados, y solo uno alcanzable desde ambos
            ([-1, 2, -1], 1, 2, 2),
        ]
    )
    def test_closest_meeting_node(self, edges, node1, node2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método closestMeetingNode.

        Args:
            edges (List[int]): Lista con el índice de la arista saliente para cada nodo.
            node1 (int): Nodo de inicio 1.
            node2 (int): Nodo de inicio 2.
            expected_output (int): Índice esperado del nodo común con distancia mínima.
        """
        assert self.solution.closestMeetingNode(edges, node1, node2) == expected_output
