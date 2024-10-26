import pytest
from challenge import Solution  # Importamos la clase Solution para acceder al método a probar


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),        # Caso típico con varios números ausentes
            ([1, 1], [2]),                             # Caso con duplicados y un número faltante
            ([2, 2], [1]),                             # Caso donde falta el número inicial
            ([], []),                                  # Array vacío, sin números ausentes
            ([1, 2, 3, 4, 5], []),                     # Caso donde no falta ningún número
            ([10, 2, 5, 5, 2, 1, 3, 7, 9, 8], [4, 6]), # Caso mixto con varios duplicados y números ausentes
            ([1], []),                                 # Array con un solo número sin ausentes
            ([2], [1]),                                # Array con un solo número donde falta el primer elemento
            ([7, 7, 7, 7, 7], [1, 2, 3, 4, 5, 6]),     # Caso con duplicados y faltantes en un rango completo
            ([5, 4, 6, 7, 9, 10], [1, 2, 3, 8]),       # Caso con rango parcial y múltiples ausentes
        ]
    )
    def test_find_disappeared_numbers(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método findDisappearedNumbers.

        Args:
            nums (List[int]): Lista de números para verificar los ausentes.
            expected_output (List[int]): Lista de los números esperados como ausentes.
        """
        assert self.solution.findDisappearedNumbers(nums) == expected_output
