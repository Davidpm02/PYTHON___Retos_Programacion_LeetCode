import pytest
from challenge import Solution  # Importo la clase Solution desde challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "colors, edges, expected_output",
        [
            # Grafo simple, sin ciclos, camino único, valor máximo del color 'a' es 1
            ("a", [], 1),

            # Grafo lineal: a -> b -> c, colores "abc"
            # Camino máximo: 'a', 'b', 'c' con valor máximo 1 para cada color
            ("abc", [[0,1],[1,2]], 1),

            # Grafo con nodos con mismo color en camino: "abaca"
            # Camino 0->1->2->3->4
            # Color 'a' aparece 3 veces, resultado esperado 3
            ("abaca", [[0,1],[1,2],[2,3],[3,4]], 3),

            # Grafo con bifurcación sin ciclo, colores variados
            ("abaca", [[0,1],[0,2],[1,3],[2,3],[3,4]], 3),

            # Grafo con ciclo (0->1->2->0), debe devolver -1
            ("abc", [[0,1],[1,2],[2,0]], -1),

            # Grafo con ciclo más grande
            ("abcde", [[0,1],[1,2],[2,3],[3,1],[3,4]], -1),

            # Grafo sin aristas, múltiples nodos
            ("abcde", [], 1),

            # Grafo con colores repetidos en caminos distintos
            ("aaabb", [[0,1],[1,2],[3,4]], 3),

            # Grafo con muchos nodos y sin ciclos, colores alternados
            ("ababab", [[0,1],[1,2],[2,3],[3,4],[4,5]], 3),
        ]
    )
    def test_largestPathValue(self, colors, edges, expected_output):
        """
        Valido varios casos para la función largestPathValue, incluyendo:

        - Grafos acíclicos con caminos simples y múltiples bifurcaciones.
        - Grafos con ciclos, que deben devolver -1.
        - Casos con nodos sin aristas.
        - Casos con múltiples apariciones del mismo color en caminos.
        """
        assert self.solution.largestPathValue(colors, edges) == expected_output
