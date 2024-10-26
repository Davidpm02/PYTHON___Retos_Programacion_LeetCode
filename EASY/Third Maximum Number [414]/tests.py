import pytest
from challenge import Solution  # Importamos la clase Solution para acceder al método a probar


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_nums, expected_output",
        [
            ([3, 2, 1], 1),                     # Caso básico con tres elementos distintos
            ([1, 2], 2),                        # Menos de tres elementos, retorna el máximo
            ([2, 2, 3, 1], 1),                  # Caso con elementos repetidos
            ([5, 2, 2, 4, 1, 6], 4),            # Tres máximos distintos en lista con duplicados
            ([1, 1, 1], 1),                     # Todos los elementos son iguales
            ([1, 2, 3, 4, 5], 3),               # Lista ordenada de menor a mayor
            ([5, 4, 3, 2, 1], 3),               # Lista ordenada de mayor a menor
            ([10, 9, 8, 8, 8, 7, 6], 8),        # Lista con duplicados y tercer máximo bien definido
            ([-1, -2, -3, -4], -3),             # Lista con números negativos
            ([3, 3, 3, 3, 3], 3),               # Lista con elementos repetidos, uno único
        ]
    )
    def test_third_max(self, input_nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método thirdMax.

        Args:
            input_nums (List[int]): La lista de enteros para la cual se quiere encontrar el tercer máximo.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.thirdMax(input_nums) == expected_output
