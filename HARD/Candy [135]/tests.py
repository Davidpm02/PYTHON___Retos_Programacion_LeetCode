import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "ratings, expected_candies",
        [
            ([1, 0, 2], 5),                  # Caso clásico con subida y bajada: [2,1,2]
            ([1, 2, 2], 4),                  # Subida y valores iguales: [1,2,1]
            ([1, 2, 3, 4, 5], 15),           # Totalmente creciente: [1,2,3,4,5]
            ([5, 4, 3, 2, 1], 15),           # Totalmente decreciente: [5,4,3,2,1]
            ([1, 3, 4, 5, 2], 11),           # Pico descendente al final
            ([1, 3, 2, 2, 1], 7),            # Pico intermedio y repetidos
            ([1], 1),                        # Un solo niño
            ([1, 2, 3, 1, 0], 9),            # Subida y bajada pronunciada
            ([1, 1, 1, 1], 4),               # Todos iguales: 1 caramelo por niño
            ([1, 6, 10, 8, 7, 3, 2], 18),    # Secuencia compleja con subida y bajada
        ]
    )
    def test_candy(self, ratings, expected_candies):
        """
        Prueba parametrizada para validar múltiples escenarios del método candy.

        Args:
            ratings (List[int]): Lista con valoraciones de los niños.
            expected_candies (int): Número mínimo de caramelos esperados.
        """
        assert self.solution.candy(ratings) == expected_candies
