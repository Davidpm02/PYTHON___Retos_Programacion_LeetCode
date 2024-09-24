import pytest
from challenge import Solution  # Asegúrate de que el nombre del archivo donde resides la clase Solution sea "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 2, 3, 1], 3, True),             # Duplicado 1 con distancia 3
            ([1, 0, 1, 1], 1, True),             # Duplicado 1 con distancia 1
            ([1, 2, 3, 4, 5], 1, False),         # No hay duplicados
            ([1, 2, 1, 2, 1], 1, True),          # Duplicado 1 con distancia 1
            ([1, 2, 3, 4, 1, 5], 4, True),       # Duplicado 1 con distancia 4
            ([1, 1, 1, 1, 1], 1, True),          # Todos los elementos son duplicados con distancia 1
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, False),  # No hay duplicados
            ([3, 3], 0, True),                   # Duplicados con distancia 0
            ([2, 2, 2, 2], 3, True),              # Duplicado 2 con distancia 3
        ]
    )
    def test_contains_nearby_duplicate(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función containsNearbyDuplicate.

        Args:
            nums (List[int]): Lista de enteros que se probará.
            k (int): Distancia máxima permitida.
            expected_output (bool): El resultado esperado tras aplicar containsNearbyDuplicate.
        """
        assert self.solution.containsNearbyDuplicate(nums, k) == expected_output
