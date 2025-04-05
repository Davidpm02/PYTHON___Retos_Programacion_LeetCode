import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 2, 3], 0),                     # No se puede formar un valor positivo: (1 - 2) * 3 = -3
            ([3, 2, 1], 2),                     # (3 - 1) * 1 = 2
            ([5, 1, 3, 4], 12),                 # (5 - 1) * 3 = 12
            ([10, 2, 8, 1, 9], 72),             # (10 - 2) * 9 = 72
            ([1, 5, 2, 4, 3], 12),              # (5 - 2) * 4 = 12
            ([1, 1, 1], 0),                     # Todos los valores iguales, resultado siempre 0
            ([1, 100, 1], 0),                   # (1 - 100) * 1 = -99 → no mejora sobre 0
            ([1, 2], 0),                        # Menos de 3 elementos, no se puede formar un triplete
            ([10, 5, 2, 8, 7], 64),             # (10 - 2) * 8 = 64
            ([3, 1, 5, 0, 4], 20),              # (5 - 0) * 4 = 20
            ([100, 1, 1, 1, 100], 9900),        # (100 - 1) * 100 = 9900
            ([0, 0, 0, 10], 0),                 # Todos ceros excepto nums[k] → resultado 0
            ([7, 8, 9, 10], 20),                # (9 - 8) * 10 = 10, (10 - 9) * 10 = 10 → (9 - 7) * 10 = 20
        ]
    )
    def test_maximum_triplet_value(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método maximumTripletValue.

        Args:
            nums (List[int]): Lista de enteros con la que se probará el método.
            expected_output (int): Valor esperado como salida para el input dado.
        """
        assert self.solution.maximumTripletValue(nums) == expected_output
