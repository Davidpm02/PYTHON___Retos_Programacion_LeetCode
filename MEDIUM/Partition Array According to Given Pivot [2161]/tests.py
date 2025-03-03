import pytest
from challenge import Solution  

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, pivot, expected_output",
        [
            ([9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]),
            ([-3, 4, 3, 2], 2, [-3, 2, 4, 3]),
            ([1, 2, 3, 4, 5], 3, [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], 3, [2, 1, 3, 5, 4]),
            ([7, 8, 9, 7, 8, 9], 8, [7, 7, 8, 8, 9, 9]),
            ([10, 20, 30, 40, 50], 25, [10, 20, 30, 40, 50]),
            ([0, 0, 0, 0, 0], 0, [0, 0, 0, 0, 0]),
        ]
    )
    def test_pivotArray(self, nums, pivot, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función pivotArray.

        Args:
            nums (List[int]): Lista de números enteros a ordenar.
            pivot (int): Número pivote para la reordenación.
            expected_output (List[int]): Resultado esperado después de la reordenación.
        """
        assert self.solution.pivotArray(nums, pivot) == expected_output