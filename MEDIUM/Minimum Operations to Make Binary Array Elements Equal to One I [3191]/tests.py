import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 1, 1], 0),            # No se requieren operaciones
            ([0, 1, 1], 1),            # Un solo flip en el primer elemento
            ([0, 0, 1], 1),            # Un flip en los primeros dos elementos
            ([0, 0, 0], -1),           # Imposible convertir a todos en 1
            ([1, 0, 0, 1], 1),         # Un flip en los dos elementos centrales
            ([1, 0, 0, 0, 1], -1),     # No se puede convertir toda la lista
            ([0, 0, 0, 0, 0, 0], -1),  # Todo ceros, imposible
            ([1, 0, 1, 0, 1, 0], 3),   # Tres flips necesarios
            ([0, 1, 0, 1, 0, 1], 3),   # También requiere tres flips
        ]
    )
    def test_min_operations(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minOperations.

        Args:
            nums (List[int]): Lista de entrada con 0s y 1s.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.minOperations(nums) == expected_output
