import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([3, 3, 3, 3, 3, 3], 0),  # Todos los elementos son iguales
            ([1, 2, 2, 2, 3, 4, 2, 2], 4),  # Caso típico con dominante claro
            ([4, 4, 2, 4, 4, 4, 2, 2], 3),  # Dominante en ambos lados
            ([5, 1, 5, 5, 2, 5, 5, 3, 5], 5),  # Dominante intercalado
            ([7, 7, 7, 7, 8, 9, 7, 7], 3),  # División clara
            ([1, 2, 3, 4, 5, 6], -1),  # Sin dominante válido
            ([10], -1),  # Un solo elemento
        ]
    )
    def test_minimum_index(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minimumIndex.

        Args:
            nums (List[int]): Lista de enteros a evaluar.
            expected_output (int): Índice esperado de división.
        """
        assert self.solution.minimumIndex(nums) == expected_output
