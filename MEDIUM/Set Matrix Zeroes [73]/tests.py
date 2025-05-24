import pytest
from challenge import Solution  # challenge.py debe contener la clase Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "matrix, expected_output",
        [
            (
                [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
            ),
            (
                [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
            ),
            (
                [[1, 2], [3, 0]],
                [[1, 0], [0, 0]]
            ),
            (
                [[0, 0], [0, 0]],
                [[0, 0], [0, 0]]
            ),
            (
                [[1, 2], [3, 4]],
                [[1, 2], [3, 4]]
            ),
            (
                [[1]],
                [[1]]
            ),
            (
                [[0]],
                [[0]]
            ),
            (
                [[1, 0, 3]],
                [[0, 0, 0]]
            ),
            (
                [[1], [0], [3]],
                [[0], [0], [0]]
            ),
        ]
    )
    def test_set_zeroes(self, matrix, expected_output):
        """
        Prueba parametrizada para validar que la matriz se modifica correctamente.

        Args:
            matrix (List[List[int]]): Matriz original que será modificada in-place.
            expected_output (List[List[int]]): Matriz esperada tras aplicar setZeroes.
        """
        self.solution.setZeroes(matrix)
        
