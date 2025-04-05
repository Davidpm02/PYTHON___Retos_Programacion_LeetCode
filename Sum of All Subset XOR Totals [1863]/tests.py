import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 3], 6),                          # Ejemplo básico con dos elementos
            ([5, 1, 6], 28),                      # Ejemplo con tres elementos
            ([3, 4, 5, 6, 7, 8], 480),            # Ejemplo con seis elementos
            ([2, 5, 6], 1),                       # Ejemplo de una pequeña lista con resultado conocido
            ([1, 2, 3], 12),                      # Otro caso sencillo
            ([10], 10),                           # Un solo elemento en el array
            ([1], 1),                             # Caso con solo un elemento
            ([0, 0, 0], 0),                      # Caso con elementos 0
            ([1, 1, 1], 3),                      # Tres elementos iguales
            ([1, 2, 3, 4, 5, 6, 7, 8], 1020),     # Caso con más elementos
        ]
    )
    def test_subset_xor_sum(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función subsetXORSum.

        Args:
            nums (List[int]): La lista de enteros que se probará.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.subsetXORSum(nums) == expected_output
