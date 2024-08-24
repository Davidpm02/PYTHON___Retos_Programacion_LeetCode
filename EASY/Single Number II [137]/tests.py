import pytest
from challenge import Solution  # Asegúrate de que el nombre del archivo donde resides la clase Solution sea "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([2, 2, 3, 2], 3),                  # Ejemplo donde 3 es el número único
            ([0, 1, 0, 1, 0, 1, 99], 99),       # Ejemplo donde 99 es el número único
            ([30000, 500, 100, 30000, 100, 30000, 100], 500),  # Número grande único
            ([1, 1, 1, 2], 2),                  # Caso simple con 2 como número único
            ([-1, -1, -1, -2], -2),             # Ejemplo con números negativos
            ([10], 10),                         # Caso con solo un elemento en la lista
            ([2, 2, 2, 2], 2),                  # Caso donde todos los elementos son iguales
        ]
    )
    def test_single_number(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función singleNumber.

        Args:
            nums (list): Lista de enteros que se probará.
            expected_output (int): El resultado esperado, es decir, el número único en la lista.
        """
        assert self.solution.singleNumber(nums) == expected_output
