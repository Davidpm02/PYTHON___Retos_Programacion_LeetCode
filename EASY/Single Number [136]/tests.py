import pytest
from challenge import Solution  # Asegúrate de que el nombre del archivo donde resides la clase Solution sea "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([2, 2, 1], 1),                  # Caso básico donde 1 es el único elemento no duplicado
            ([4, 1, 2, 1, 2], 4),            # Caso donde 4 es el único elemento no duplicado
            ([1], 1),                        # Caso con un solo elemento
            ([0, 1, 0, 1, 0, 1, 99], 99),    # Caso con múltiples duplicados, un único elemento no duplicado
            ([-1, -1, -2], -2),              # Caso con números negativos
            ([10, 10, 10, -10], -10),        # Caso con duplicados de un mismo número y un único negativo
            ([3, 3, 3], 3),                  # Caso donde todos los números son iguales, sólo uno debería aparecer una vez
        ]
    )
    def test_single_number(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método singleNumber.

        Args:
            nums (list[int]): El array de enteros en el que se buscará el único número no duplicado.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.singleNumber(nums) == expected_output
