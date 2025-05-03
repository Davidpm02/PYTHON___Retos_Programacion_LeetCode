import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 6, 2], 1),                    # (1 + 2) == 6 / 2 → válido
            ([3, 10, 5, 8, 7], 1),            # Solo el triplete (3,10,5) cumple
            ([2, 4, 6, 8], 0),                # Ningún triplete válido
            ([5, 20, 15, 10, 25], 2),         # (5,20,15) y (15,10,25) son válidos
            ([1, 3, 2, 4, 3, 5], 0),          # No hay tripletes válidos
            ([4, 16, 12], 1),                 # (4 + 12) == 16 → válido
            ([1], 0),                         # Array demasiado corto, sin tripletes
            ([1, 2], 0),                      # Array demasiado corto, sin tripletes
            ([8, 32, 24, 16], 1),             # Solo (8,32,24) válido
            ([10, 100, 90, 80, 70], 1),       # (10 + 90) == 100/2 → válido
        ]
    )
    def test_count_subarrays(self, nums, expected_output):
        """
        Prueba parametrizada para validar distintos escenarios del método countSubarrays.

        Args:
            nums (List[int]): Array de entrada con números enteros.
            expected_output (int): Número esperado de tripletes válidos.
        """
        assert self.solution.countSubarrays(nums) == expected_output
