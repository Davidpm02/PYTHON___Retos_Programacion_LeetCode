import pytest
from challenge import Solution  

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums1, nums2, expected_output",
        [
            ([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]], [[1,6],[2,3],[3,2],[4,6]]),
            ([[2,4],[3,6],[5,5]], [[1,3],[4,3]], [[1,3],[2,4],[3,6],[4,3],[5,5]]),
            ([[1,1]], [[1,1]], [[1,2]]),
            ([[1,2],[3,4]], [], [[1,2],[3,4]]),
            ([], [[2,5],[4,7]], [[2,5],[4,7]]),
            ([[1,3],[3,5],[5,7]], [[2,4],[4,6],[6,8]], [[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]])
        ]
    )
    def test_merge_arrays(self, nums1, nums2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función mergeArrays.

        Args:
            nums1 (List[List[int]]): Primer array de entrada.
            nums2 (List[List[int]]): Segundo array de entrada.
            expected_output (List[List[int]]): Resultado esperado tras la fusión.
        """
        assert self.solution.mergeArrays(nums1, nums2) == expected_output
