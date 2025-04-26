import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, minK, maxK, expected_output",
        [
            ([1, 3, 5, 2, 7, 5], 1, 5, 2),  # Subarreglos fijos: [1,3,5] y [1,3,5,2]
            ([1, 1, 1, 1], 1, 1, 10),       # Todos los subarreglos son válidos
            ([1, 3, 5, 2, 7, 5], 1, 7, 3),  # Subarreglos fijos: [1,3,5,2,7] y [1,3,5,2,7,5]
            ([1, 2, 3, 4, 5], 1, 5, 1),     # Subarreglo fijo: [1,2,3,4,5]
            ([1, 3, 2, 4, 5], 1, 5, 0),     # No hay subarreglos válidos
            ([1, 3, 5, 7, 5], 5, 7, 1),     # Subarreglo fijo: [5,7]
            ([1, 2, 3, 4, 5], 2, 4, 3),     # Subarreglos fijos: [2,3,4], [2,3,4,5], [2,3,4]
            ([1, 3, 1, 3], 1, 3, 2),        # Subarreglos fijos: [1,3], [1,3]
            ([10, 20, 30, 40, 50], 20, 40, 2), # Subarreglos fijos: [20,30,40], [20,30,40,50]
            ([5, 6, 7, 8, 9], 6, 9, 3),     # Subarreglos fijos: [6,7,8,9], [6,7,8,9]
        ]
    )
    def test_count_subarrays(self, nums, minK, maxK, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countSubarrays.

        Args:
            nums (List[int]): El arreglo de enteros.
            minK (int): El valor mínimo que debe estar presente en el subarreglo.
            maxK (int): El valor máximo que debe estar presente en el subarreglo.
            expected_output (int): El resultado esperado para el número de subarreglos válidos.
        """
        assert self.solution.countSubarrays(nums, minK, maxK) == expected_output
