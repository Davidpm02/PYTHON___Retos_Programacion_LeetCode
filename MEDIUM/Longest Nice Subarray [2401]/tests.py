import pytest
from challenge import Solution  # Importamos la clase Solution desde challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 3, 8, 48, 10], 3),  # Subarray más largo que cumple la condición es [3, 8, 48]
            ([3, 1, 5, 11, 13], 1),  # No hay elementos consecutivos con AND == 0
            ([2, 2, 2, 2], 1),  # Todos los elementos son iguales, por lo que solo puede haber un número en cada subarray
            ([4, 8, 16, 32], 4),  # Todos los números son potencias de 2, por lo que forman el subarray más largo
            ([5, 10, 15, 20, 25], 2),  # Solo se pueden formar subarrays de longitud máxima 2
            ([1], 1),  # Un solo elemento siempre es válido
        ]
    )
    def test_longest_nice_subarray(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función longestNiceSubarray.

        Args:
            nums (List[int]): La lista de números enteros.
            expected_output (int): La longitud esperada del subarray más largo que cumple la condición.
        """
        assert self.solution.longestNiceSubarray(nums) == expected_output
