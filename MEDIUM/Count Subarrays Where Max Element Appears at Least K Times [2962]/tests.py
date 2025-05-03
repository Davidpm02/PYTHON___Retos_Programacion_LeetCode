import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 3, 3, 3, 2], 2, 6),       # Subarrays con al menos dos '3', que es el valor máximo
            ([1, 2, 3, 4], 1, 4),          # Cada subarray que contenga el 4 al menos una vez es válido
            ([5, 5, 5, 5], 2, 6),          # Todos los subarrays con al menos dos '5'
            ([1, 2, 1, 2, 1], 1, 5),       # Valor máximo es 2, y aparece en posiciones 1 y 3
            ([1, 1, 1], 3, 1),             # Solo el subarray completo cumple con las 3 apariciones
            ([1, 2, 3, 4], 2, 0),          # Máximo aparece solo una vez, nunca llega a 2 apariciones
            ([4, 4, 4, 1, 4], 3, 7),       # Ventanas con al menos tres 4s
            ([1], 1, 1),                   # Caso mínimo: un único elemento que es el máximo
            ([1], 2, 0),                   # No se puede cumplir si k > apariciones
            ([2, 2, 2, 2], 1, 10),         # Todos los subarrays contienen el máximo al menos una vez
        ]
    )
    def test_count_subarrays(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar distintos escenarios del método countSubarrays.

        Args:
            nums (List[int]): Lista de enteros de entrada.
            k (int): Número mínimo de apariciones del valor máximo en el subarray.
            expected_output (int): Número esperado de subarrays válidos.
        """
        assert self.solution.countSubarrays(nums, k) == expected_output
