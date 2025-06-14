import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 2, 3, 4], 3),                  # Máxima diferencia es entre 1 y 4 (circular)
            ([4, 1, 7], 6),                     # Máxima diferencia entre 1 y 7
            ([10, 20, 30], 20),                # Máxima diferencia entre 10 y 30 (circular)
            ([5, 5, 5, 5], 0),                 # Todos iguales, diferencia máxima es 0
            ([100], 0),                        # Un solo elemento, la diferencia es 0 por convención
            ([1, 100], 99),                    # Solo dos elementos, la diferencia máxima es 99
            ([1, 3, 9, 2], 8),                 # Máxima diferencia entre 9 y 2
            ([0, -10, 10], 20),                # Máxima diferencia entre -10 y 10
            ([1, -2, 4, -5], 9),               # Máxima entre 4 y -5
            ([3, 6, 2, 9], 7),                 # Máxima entre 2 y 9
        ]
    )
    def test_max_adjacent_distance(self, nums, expected_output):
        """
        Prueba parametrizada para validar distintos escenarios del método maxAdjacentDistance.

        Args:
            nums (List[int]): Lista de enteros representando el array circular.
            expected_output (int): Diferencia máxima esperada entre elementos adyacentes.
        """
        assert self.solution.maxAdjacentDistance(nums) == expected_output
