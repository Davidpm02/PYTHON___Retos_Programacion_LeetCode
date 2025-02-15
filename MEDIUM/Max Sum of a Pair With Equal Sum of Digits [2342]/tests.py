import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([51, 71, 17, 42], 93),         # Ejemplo: 51 y 42 tienen la misma suma de dígitos (5 + 1 = 4 + 2 = 6)
            ([1, 2, 3, 4], -1),             # No hay dos números con la misma suma de dígitos
            ([10, 12, 21, 13], 33),         # Ejemplo: 21 y 12 tienen la misma suma de dígitos (2 + 1 = 1 + 2 = 3)
            ([1, 2, 3, 4, 5, 6, 7, 8], -1), # Todos los números tienen sumas de dígitos diferentes
            ([11, 22, 33, 44], 77),         # Ejemplo: 33 y 44 tienen la misma suma de dígitos (3 + 3 = 4 + 4 = 6)
            ([123, 231, 321], 654),         # Ejemplo: 123 y 231 tienen la misma suma de dígitos (1 + 2 + 3 = 2 + 3 + 1 = 6)
            ([111, 123, 132, 213], 345),    # Ejemplo: 132 y 213 tienen la misma suma de dígitos (1 + 3 + 2 = 2 + 1 + 3 = 6)
            ([99, 18, 45, 36], 135),        # Ejemplo: 99 y 36 tienen la misma suma de dígitos (9 + 9 = 3 + 6 = 18)
        ]
    )
    def test_maximum_sum(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maximumSum.

        Args:
            nums (List[int]): La lista de números para probar.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.maximumSum(nums) == expected_output
