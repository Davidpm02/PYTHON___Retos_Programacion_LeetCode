import pytest
from challenge import Solution  # Ajusta el nombre del archivo o el módulo de importación según corresponda


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 3, 5, 4, 7], 4),           # Secuencia ascendente más larga: [1, 3, 5] o [4, 7]
            ([2, 2, 2, 2, 2], 1),           # Todos los elementos son iguales, no hay secuencia ascendente
            ([1, 2, 3, 4, 5], 5),           # Secuencia ascendente continua: [1, 2, 3, 4, 5]
            ([5, 4, 3, 2, 1], 1),           # Secuencia descendente, no hay ascendente
            ([1, 3, 2, 3, 4, 5], 4),        # Secuencia ascendente más larga: [2, 3, 4, 5]
            ([10, 9, 8, 7, 6, 5, 4, 3], 1), # Secuencia descendente de largo: 1
            ([100, 200, 300, 10, 20], 3),   # Secuencia ascendente más larga: [100, 200, 300]
            ([5], 1),                       # Solo un elemento, la longitud de la secuencia es 1
            ([1, 2, 3, 1, 2, 3, 4], 4),     # Secuencia ascendente más larga: [1, 2, 3, 4]
            ([], 0),                        # Lista vacía, no hay secuencia
        ]
    )
    def test_find_length_of_lcis(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método findLengthOfLCIS.

        Args:
            nums (List[int]): Lista de enteros a analizar.
            expected_output (int): Longitud esperada de la subsecuencia más larga ascendente.
        """
        assert self.solution.findLengthOfLCIS(nums) == expected_output
