import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, lower, upper, expected_output",
        [
            ([1, 2, 3, 4, 5], 4, 6, 4),         # Pares: (1,3),(1,4),(2,3),(2,4)
            ([1, 1, 1, 1], 2, 2, 6),            # Todas las combinaciones suman 2: C(4,2)=6
            ([1, 2, 3], 3, 5, 3),               # Pares: (1,2),(1,3),(2,3)
            ([0, 0, 0, 0], 0, 0, 6),            # Todas las combinaciones valen 0: C(4,2)=6
            ([-1, -2, -3, -4], -6, -3, 4),      # Pares: (-2,-4), (-1,-4), (-1,-3), (-2,-3)
            ([1, 5, 2, 4, 3], 5, 7, 6),         # Pares válidos: (1,4),(1,5),(2,3),(2,4),(2,5),(3,4)
            ([1], 1, 2, 0),                     # No hay pares posibles con un solo elemento
            ([1, 10, 100], 50, 150, 2),         # Pares: (10,100),(1,100)
            ([1, 2, 3, 4], 8, 10, 0),           # Ningún par suma dentro del rango
            ([5, 1, 2, 7, 3, 6], 7, 9, 8),      # Varios pares que caen dentro del rango
        ]
    )
    def test_count_fair_pairs(self, nums, lower, upper, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método countFairPairs.

        Args:
            nums (List[int]): Lista de enteros.
            lower (int): Límite inferior de la suma aceptable.
            upper (int): Límite superior de la suma aceptable.
            expected_output (int): Número esperado de pares válidos.
        """
        assert self.solution.countFairPairs(nums, lower, upper) == expected_output
