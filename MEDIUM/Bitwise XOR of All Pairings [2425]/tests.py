import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums1, nums2, expected_output",
        [
            ([1, 2, 3], [6, 5], 6),                   # Caso mixto con XOR calculado
            ([0], [0], 0),                            # XOR de listas con ceros
            ([1, 1, 1], [2, 2], 1),                  # Valores repetidos
            ([0, 0, 0], [1, 1, 1], 1),               # Lista con ceros frente a lista con unos
            ([1, 2, 4], [], 0),                      # XOR con lista vacía
            ([], [3, 5, 7], 0),                      # XOR con lista vacía al otro lado
            ([15, 3], [2, 10], 8),                   # Diferentes números
            ([8, 8, 8], [8, 8], 0),                  # Números repetidos en ambas listas
            ([1, 0, 1], [1, 0, 1, 0], 0),            # Mezcla de ceros y unos
            ([1024, 2048], [4096, 8192], 12288),     # Números grandes
        ]
    )
    def test_xor_all_nums(self, nums1, nums2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función xorAllNums.

        Args:
            nums1 (List[int]): Lista de enteros, primera entrada del método.
            nums2 (List[int]): Lista de enteros, segunda entrada del método.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.xorAllNums(nums1, nums2) == expected_output
