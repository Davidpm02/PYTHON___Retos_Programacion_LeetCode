import pytest
from challenge import Solution

class TestSolution:
    
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_matrix, expected_output",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),  # Caso estándar 3x3
            ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),  # Caso 2x2
            ([[1], [2], [3]], [[1, 2, 3]]),  # Caso 3x1 (traspuesta debe ser 1x3)
            ([[1]], [[1]]),  # Caso 1x1 (la matriz no cambia)
            ([[1, 2, 3, 4]], [[1], [2], [3], [4]]),  # Caso 1x4 (traspuesta debe ser 4x1)
            ([[5, 6, 7], [8, 9, 10]], [[5, 8], [6, 9], [7, 10]]),  # Caso 2x3
            ([[], []], [[], []]),  # Caso de matrices vacías
        ]
    )
    def test_transpose(self, input_matrix, expected_output):
        """
        Prueba parametrizada para validar la función transpose.

        Args:
            input_matrix (List[List[int]]): La matriz que será transpuesta.
            expected_output (List[List[int]]): El resultado esperado después de la transposición.
        """
        assert self.solution.transpose(input_matrix) == expected_output
