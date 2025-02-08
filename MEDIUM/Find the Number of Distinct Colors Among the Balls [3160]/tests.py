import pytest
from challenge import Solution  # Importo la clase Solution desde el fichero del reto


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "limit, queries, expected_output",
        [
            (5, [[1, 2], [2, 3], [3, 2], [1, 4]], [1, 2, 2, 3]),  # Caso con varios cambios de color
            (3, [[1, 1], [2, 1], [3, 1]], [1, 1, 1]),  # Todas las bolas del mismo color
            (4, [[1, 2], [2, 3], [3, 4], [4, 5]], [1, 2, 3, 4]),  # Todos colores distintos
            (2, [[1, 2], [1, 3], [1, 4]], [1, 1, 1]),  # La misma bola cambia de color varias veces
            (6, [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 1]], [1, 2, 3, 3, 3, 3]),  # Rotación de colores
        ]
    )
    def test_query_results(self, limit, queries, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función queryResults.

        Args:
            limit (int): Número máximo de bolas.
            queries (List[List[int]]): Lista de consultas de cambio de color.
            expected_output (List[int]): Resultado esperado tras cada consulta.
        """
        assert self.solution.queryResults(limit, queries) == expected_output
