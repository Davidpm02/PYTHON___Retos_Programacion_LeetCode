import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),  # Caso típico de permutación
            ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),  # Permutación invertida parcialmente
            ([1, 0], [0, 1]),                         # Caso mínimo con dos elementos
            ([2, 0, 1], [1, 2, 0]),                   # Permutación rotada
            ([3, 2, 1, 0], [0, 1, 2, 3]),             # Inversión completa
            ([0], [0]),                               # Caso base con un único elemento
        ]
    )
    def test_build_array(self, nums, expected_output):
        """
        Prueba parametrizada para verificar la transformación de la permutación según nums[nums[i]].

        Args:
            nums (List[int]): Lista de enteros representando una permutación.
            expected_output (List[int]): Lista esperada tras la transformación.
        """
        assert self.solution.buildArray(nums) == expected_output
