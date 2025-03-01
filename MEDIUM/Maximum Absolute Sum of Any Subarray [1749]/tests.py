import pytest
from challenge import Solution  # Importamos la clase Solution desde el archivo del reto

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, -3, 2, 3, -4], 5),  # El subarray [2, 3] da la suma máxima 5
            ([2, -5, 1, -4, 3, -2], 6),  # El subarray [-5, 1, -4] da la suma mínima -8 (abs(8) = 8)
            ([1, 2, 3, 4, 5], 15),  # Todo el array tiene la suma máxima positiva
            ([-1, -2, -3, -4, -5], 5),  # Todo el array tiene la suma mínima negativa (abs(-5) = 5)
            ([0, 0, 0, 0, 0], 0),  # Todos los valores son 0, la suma absoluta máxima es 0
            ([1000, -1000, 1000, -1000, 1000], 1000),  # Alternando valores altos positivos y negativos
            ([-10, 2, -5, 7, -3, 4, -8, 9], 14),  # El subarray [7, -3, 4, -8, 9] da la máxima suma absoluta 14
            ([5], 5),  # Un único elemento positivo
            ([-5], 5),  # Un único elemento negativo
            ([10, -10, 10, -10, 10, -10], 10),  # Alternancia entre valores positivos y negativos
        ]
    )
    def test_max_absolute_sum(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maxAbsoluteSum.
        
        Args:
            nums (List[int]): La lista de números a evaluar.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.maxAbsoluteSum(nums) == expected_output