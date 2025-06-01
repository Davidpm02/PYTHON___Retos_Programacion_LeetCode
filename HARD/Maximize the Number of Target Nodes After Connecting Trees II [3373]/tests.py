import pytest
from challenge import Solution  # Importo la clase Solution del fichero challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "edges1, edges2, expected_output",
        [
            # Caso simple: ambos árboles con un nodo (sin aristas)
            ([], [], [1]),

            # Árbol1 con dos nodos conectados, árbol2 con dos nodos conectados
            (
                [[0, 1]],
                [[0, 1]],
                [3, 3]  # Ambos nodos de árbol1 suman count color + mejor color de árbol2
            ),

            # Árbol1 en línea 0-1-2, árbol2 con 3 nodos en línea
            (
                [[0, 1], [1, 2]],
                [[0, 1], [1, 2]],
                [5, 5, 5]  # Todos los nodos de árbol1 tienen la suma máxima de su color + mejor color árbol2
            ),

            # Árbol1 con forma de estrella, árbol2 con línea, para verificar el conteo de colores
            (
                [[0, 1], [0, 2], [0, 3]],
                [[0, 1], [1, 2], [2, 3]],
                [7, 6, 6, 6]  # Se calcula en función del color de cada nodo
            ),

            # Árbol1 y árbol2 ambos con solo un nodo (vacíos)
            (
                [],
                [],
                [1]
            ),

            # Árbol con 4 nodos y forma de cadena, árbol2 con 2 nodos conectados
            (
                [[0, 1], [1, 2], [2, 3]],
                [[0, 1]],
                [5, 5, 5, 5]
            )
        ]
    )
    def test_max_target_nodes(self, edges1, edges2, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método maxTargetNodes.

        Args:
            edges1 (List[List[int]]): Lista de aristas para el primer árbol.
            edges2 (List[List[int]]): Lista de aristas para el segundo árbol.
            expected_output (List[int]): Resultado esperado para cada nodo de árbol1.
        """
        assert self.solution.maxTargetNodes(edges1, edges2) == expected_output
