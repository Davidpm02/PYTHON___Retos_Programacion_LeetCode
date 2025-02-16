import pytest
from challenge import Solution  # Importamos la clase Solution desde el archivo del reto

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_n, expected_output",
        [
            (1, [1]),
            (2, [2, 1, 2]),
            (3, [3, 1, 2, 3, 2]),
            (4, [4, 2, 3, 2, 4, 3, 1]),
            (5, [5, 3, 1, 4, 3, 5, 2, 4, 2]),
            (6, [6, 4, 2, 5, 2, 4, 6, 3, 5, 1, 3]),
            (7, [7, 5, 3, 6, 4, 3, 5, 7, 4, 6, 2, 1, 2]),
            (8, [8, 6, 4, 2, 7, 2, 4, 6, 8, 5, 3, 7, 1, 3, 5]),
            (9, [9, 7, 5, 3, 8, 6, 3, 5, 7, 9, 4, 6, 8, 2, 4, 2, 1]),
            (10, [10, 8, 6, 9, 3, 1, 7, 3, 6, 8, 10, 5, 9, 7, 4, 2, 5, 2, 4]),
            (20, [20, 18, 19, 15, 13, 17, 10, 16, 7, 5, 3, 14, 12, 3, 5, 7, 10, 13, 15, 18, 20, 19, 17, 16, 12, 14, 11, 9, 4, 6, 8, 2, 4, 2, 1, 6, 9, 11, 8]),
        ]
    )
    def test_construct_distanced_sequence(self, input_n, expected_output):
        """
        Prueba parametrizada para validar la función constructDistancedSequence con diferentes valores de n.

        Args:
            input_n (int): El valor de n que define la secuencia a generar.
            expected_output (List[int]): La secuencia esperada para el valor dado de n.
        """
        assert self.solution.constructDistancedSequence(input_n) == expected_output