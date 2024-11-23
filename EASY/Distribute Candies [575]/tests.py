import pytest
from challenge import Solution  # Importo la clase Solution del archivo principal del reto


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "candyType, expected_output",
        [
            ([1, 1, 2, 2, 3, 3], 3),  # Hay 3 tipos y Alice puede comer 3 caramelos
            ([1, 1, 1, 1], 1),        # Un único tipo de caramelo, Alice solo puede comer 1
            ([1, 2, 3, 4], 2),        # 4 tipos, pero Alice solo puede comer 2 caramelos
            ([1, 2, 2, 3, 3, 4, 4], 3),  # 4 tipos, Alice puede comer 3 caramelos
            ([1], 1),                 # Solo un caramelo disponible
            ([], 0),                  # No hay caramelos
            ([1, 1, 2, 3], 2),        # 3 tipos, Alice solo puede comer 2 caramelos
            ([1, 1, 2, 2, 3, 3, 4, 4], 4),  # 4 tipos y Alice puede comer 4 caramelos
            ([1, 2, 3, 4, 5, 6], 3),  # 6 tipos pero Alice solo puede comer 3 caramelos
            ([1, 1, 1, 2, 2, 2], 2),  # Solo 2 tipos, Alice puede comer 2 caramelos
        ]
    )
    def test_distribute_candies(self, candyType, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función distributeCandies.

        Args:
            candyType (List[int]): Lista de tipos de caramelos disponibles.
            expected_output (int): Número máximo de caramelos que Alice puede comer.
        """
        assert self.solution.distributeCandies(candyType) == expected_output
