import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 1, 1], 1, 6),       # Todos los subarrays tienen al menos un par igual
            ([1, 2, 3, 1], 1, 5),     # Algunos subarrays tienen al menos un par igual
            ([1, 2, 3, 4], 1, 0),     # Ningún par igual, no se pueden formar subarrays válidos
            ([1, 1, 1, 1], 3, 10),    # Todos los subarrays tienen suficientes pares iguales
            ([1, 2, 3, 1, 1, 1], 2, 15), # Varios subarrays con suficientes pares iguales
            ([1, 2, 1], 2, 3),       # Tres subarrays con exactamente dos pares iguales
            ([1, 2, 3], 2, 0),       # Ningún subarray tiene dos pares iguales
            ([1, 1, 1, 2], 2, 6),     # Tres subarrays válidos, con exactamente 2 pares iguales
            ([1, 2, 3, 4, 5], 1, 0),  # Ningún subarray con pares repetidos
            ([1, 1, 2, 2, 1], 2, 9)   # Subarrays con al menos dos pares iguales
        ]
    )
    def test_count_good(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar el número de subarrays válidos con al menos 'k' pares de índices iguales.

        Args:
            nums (List[int]): El arreglo de números.
            k (int): El mínimo número de pares de índices que deben cumplirse en el subarray.
            expected_output (int): El número esperado de subarrays válidos.
        """
        assert self.solution.countGood(nums, k) == expected_output
