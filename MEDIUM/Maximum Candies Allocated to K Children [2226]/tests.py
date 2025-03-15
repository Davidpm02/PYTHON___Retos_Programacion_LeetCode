import pytest
from challenge import Solution  

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "candies, k, expected_output",
        [
            ([5, 8, 6], 3, 5),  # Cada niño recibe 5 caramelos
            ([2, 5, 7, 10], 4, 3),  # Cada niño recibe 3 caramelos
            ([1, 2, 3], 7, 0),  # No hay suficientes caramelos
            ([10, 10, 10], 3, 10),  # Exactamente 3 niños pueden recibir 10 caramelos
            ([4, 2, 6, 8], 5, 2),  # Distribución óptima
            ([100], 10, 10),  # Un solo montón dividido entre 10 niños
            ([1, 1, 1, 1], 4, 1),  # Cada niño recibe 1 caramelo
            ([5, 3, 2, 1], 1, 5),  # Un solo niño recibe la mayor cantidad posible
            ([9, 9, 9, 9], 5, 7),  # Distribución óptima entre más niños
            ([0, 0, 0, 0], 2, 0),  # No hay caramelos disponibles
        ]
    )
    def test_maximum_candies(self, candies, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maximumCandies.

        Args:
            candies (List[int]): Lista de montones de caramelos.
            k (int): Número de niños.
            expected_output (int): El número máximo de caramelos que puede recibir cada niño.
        """
        assert self.solution.maximumCandies(candies, k) == expected_output