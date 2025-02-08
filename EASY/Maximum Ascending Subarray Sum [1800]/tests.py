import pytest
from challenge import Solution  # Asegúrate de que el archivo donde tienes el código se llama challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_nums, expected_output",
        [
            ([1, 2, 3, 4, 5], 15),               # La suma máxima es 1+2+3+4+5 = 15
            ([5, 4, 3, 2, 1], 5),                # No hay subarrays ascendentes, solo el máximo es el primer número
            ([1, 3, 2, 3, 5], 8),                # La subsecuencia ascendente máxima es [2, 3, 5] -> suma = 8
            ([10, 20, 30, 40], 100),             # Suma de toda la subsecuencia ascendente
            ([1, 2, 3, 2, 3, 4, 5], 15),         # La suma máxima es la subsecuencia [1, 2, 3, 2, 3, 4, 5] -> suma = 15
            ([3, 2, 1], 3),                     # Solo un número
            ([1], 1),                           # Caso con solo un elemento
            ([1, 2, 1, 2, 3, 4, 5], 15),         # La subsecuencia ascendente máxima es [1, 2, 3, 4, 5] -> suma = 15
            ([1, 2, 3, 4, 1, 2, 3], 10),         # Suma máxima de la subsecuencia ascendente [1, 2, 3, 4]
            ([100, 200, 100, 200, 300], 600),    # La subsecuencia ascendente máxima es [100, 200, 300] -> suma = 600
            ([], 0),                            # Caso con lista vacía, la suma es 0
        ]
    )
    def test_max_ascending_sum(self, input_nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maxAscendingSum.

        Args:
            input_nums (List[int]): La lista de enteros para calcular la suma máxima de subsecuencia ascendente.
            expected_output (int): El valor esperado de la suma máxima.
        """
        assert self.solution.maxAscendingSum(input_nums) == expected_output
