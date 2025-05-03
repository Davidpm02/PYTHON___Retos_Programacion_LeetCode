import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 2, 3], 10, 6),          # Todos los subarrays cumplen la condición
            ([1, 2, 3], 6, 5),           # Solo se elimina [1, 2, 3]
            ([1, 1, 1], 2, 4),           # Algunos subarrays fallan
            ([5], 5, 0),                # Solo un elemento, pero su score no cumple (5*1 >= 5)
            ([5], 6, 1),                # El mismo elemento ahora sí cumple
            ([10, 1, 1, 1], 10, 3),     # El 10 hace que se invalide rápidamente
            ([1]*1000, 100000, 500500), # Todos los subarrays posibles son válidos (score < k)
            ([], 1, 0),                 # Array vacío, sin subarrays posibles
            ([100, 200, 300], 100, 0),  # Todos los scores son mayores o iguales a k
            ([2, 1, 4], 7, 5),          # Validación general
        ]
    )
    def test_count_subarrays(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar distintos escenarios del método countSubarrays.

        Args:
            nums (List[int]): Lista de enteros de entrada.
            k (int): Umbral para validar el score del subarray.
            expected_output (int): Número esperado de subarrays válidos.
        """
        assert self.solution.countSubarrays(nums, k) == expected_output
