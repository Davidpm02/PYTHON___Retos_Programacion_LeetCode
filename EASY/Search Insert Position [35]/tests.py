import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, target, expected_output",
        [
            ([1, 3, 5, 6], 5, 2),      # El target 5 ya está en la lista en el índice 2
            ([1, 3, 5, 6], 2, 1),      # El target 2 debería insertarse en el índice 1
            ([1, 3, 5, 6], 7, 4),      # El target 7 debería insertarse al final (índice 4)
            ([1, 3, 5, 6], 0, 0),      # El target 0 debería insertarse en el primer índice (índice 0)
            ([1, 3, 5, 6], 8, 4),      # El target 8 debería insertarse al final (índice 4)
            ([1], 1, 0),               # El target 1 ya está en la lista en el índice 0
            ([1], 0, 0),               # El target 0 debería insertarse en el primer índice (índice 0)
            ([1, 2, 3, 4, 5], 0, 0),   # El target 0 debería insertarse en el índice 0
            ([10, 20, 30, 40], 25, 2), # El target 25 debería insertarse en el índice 2
        ]
    )
    def test_search_insert(self, nums, target, expected_output):
        """
        Prueba parametrizada para validar la función searchInsert.

        Args:
            nums (List[int]): Lista de números ordenados.
            target (int): Número que queremos insertar o encontrar en la lista.
            expected_output (int): Índice esperado donde se encuentra o se debería insertar el target.
        """
        result = self.solution.searchInsert(nums, target)
        assert result == expected_output
