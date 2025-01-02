import pytest
from challenge import Solution  # Ajusta el nombre del archivo o el módulo según corresponda


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 12, -5, -6, 50, 3], 4, 12.75),  # Subconjunto de longitud 4 con media máxima
            ([5, 2, 3, 1, 4], 2, 4.0),           # Subconjunto de longitud 2 con media máxima
            ([1, 1, 1, 1], 2, 1.0),              # Todos los números iguales
            ([-1, -2, -3, -4], 3, -2.0),         # Subconjunto negativo
            ([1, 2, 3, 4, 5], 1, 5.0),           # Subconjunto con solo 1 número
            ([0, 0, 0, 0], 2, 0.0),              # Subconjunto con ceros
            ([10, 20, 30, 40, 50], 3, 40.0),      # Subconjunto de longitud 3
            ([10, 1, 2, 3, 4, 5], 3, 6.0),        # El mejor conjunto es [3,4,5]
            ([3, 3, 3, 3], 4, 3.0),              # Todos son iguales, la media será siempre 3
            ([1, -1, 2, 5, 4, 3], 2, 6.0),        # Subconjunto máximo de longitud 2 con los mejores valores
        ]
    )
    def test_find_max_average(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findMaxAverage.

        Args:
            nums (List[int]): La lista de enteros con los cuales se calculará la media.
            k (int): La longitud del subconjunto a considerar.
            expected_output (float): La media máxima esperada de cualquier subconjunto.
        """
        assert self.solution.findMaxAverage(nums, k) == expected_output
