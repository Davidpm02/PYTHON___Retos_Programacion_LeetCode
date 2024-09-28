import pytest
from challenge import Solution  # Se asume que el archivo del reto se llama challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([3, 0, 1], 2),               # Caso en el que falta el 2
            ([0], 1),                     # Caso con una sola entrada, falta el 1
            ([0, 1], 2),                  # Faltando el mayor número (2) en el rango [0,2]
            ([9,6,4,2,3,5,7,0,1], 8),     # Caso con números no secuenciales, falta el 8
            ([0, 1, 2, 3, 4, 5], 6),      # Faltando el último número en una secuencia completa
            ([], 0),                      # Lista vacía, faltando el 0
            ([1], 0),                     # Lista de un solo elemento, faltando el 0
        ]
    )
    def test_missing_number(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función missingNumber.

        Args:
            nums (List[int]): Lista de números donde se evaluará el número faltante.
            expected_output (int): El resultado esperado, es decir, el número faltante.
        """
        assert self.solution.missingNumber(nums) == expected_output
