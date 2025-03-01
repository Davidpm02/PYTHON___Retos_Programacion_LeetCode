import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "arr, expected_count",
        [
            ([1, 3, 5], 4),  # Todos los subarrays tienen suma impar
            ([2, 4, 6], 0),  # Ningún subarray tiene suma impar
            ([1, 2, 3, 4], 4),  # Mezcla de pares e impares
            ([1], 1),  # Un único elemento impar
            ([2], 0),  # Un único elemento par
            ([1, 1, 1, 1], 10),  # Caso con varios impares consecutivos
            ([10**6, 10**6, 10**6], 0)  # Números grandes pero todos pares
        ]
    )
    def test_numOfSubarrays(self, arr, expected_count):
        """
        Prueba parametrizada para validar la función numOfSubarrays con diferentes listas de entrada.
        """
        assert self.solution.numOfSubarrays(arr) == expected_count