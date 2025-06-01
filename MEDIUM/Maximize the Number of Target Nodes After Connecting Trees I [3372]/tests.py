import pytest
from challenge import Solution  # Importo la clase Solution desde challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "edges1, edges2, k, expected_output",
        [
            # Caso sencillo: dos árboles con un solo nodo cada uno, k=0
            ([], [], 0, [1]),

            # Árbol 1 con 3 nodos en línea, árbol 2 con 2 nodos, k=1
            (
                [[0, 1], [1, 2]],
                [[0, 1]],
                1,
                [3, 3, 3]  # Cada nodo en árbol1 puede alcanzar hasta 3 nodos tras conectar al mejor nodo de árbol2
            ),

            # Árbol 1 con 4 nodos formando un "T", árbol 2 igual, k=2
            (
                [[0, 1], [1, 2], [1, 3]],
                [[0, 1], [1, 2], [1, 3]],
                2,
                [6, 6, 6, 6]  # La conexión suma máximo del otro árbol
            ),

            # Árbol 1 vacio, árbol 2 con nodos, k=1
            (
                [],
                [[0, 1], [1, 2]],
                1,
                [3]
            ),

            # Caso con k negativo, no se puede llegar a otros nodos
            (
                [[0, 1]],
                [[0, 1]],
                -1,
                [1, 1]
            ),

            # Caso con un árbol grande y k pequeño
            (
                [[0, 1], [1, 2], [2, 3], [3, 4]],
                [[0, 1], [1, 2], [2, 3]],
                1,
                [3, 3, 3, 3, 3]
            )
        ]
    )
    def test_max_target_nodes(self, edges1, edges2, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método maxTargetNodes.

        Args:
            edges1 (List[List[int]]): Lista de aristas del primer árbol.
            edges2 (List[List[int]]): Lista de aristas del segundo árbol.
            k (int): Distancia máxima para contar nodos alcanzables.
            expected_output (List[int]): Resultado esperado para cada nodo de árbol1.
        """
        assert self.solution.maxTargetNodes(edges1, edges2, k) == expected_output
