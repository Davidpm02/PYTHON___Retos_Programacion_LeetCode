import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([12, 345, 2, 6, 7896], 2),           # 12 y 7896 tienen un número par de dígitos
            ([555, 901, 482, 1771], 1),           # Solo 1771 tiene longitud par
            ([1, 22, 333, 4444, 55555], 2),       # 22 y 4444 cumplen la condición
            ([0], 0),                             # 0 tiene solo 1 dígito, no es válido
            ([10, 100, 1000, 10000], 2),          # 10 (2 dígitos), 1000 (4 dígitos)
            ([123456], 1),                        # 6 dígitos, válido
            ([100000, 999999], 2),                # Ambos tienen 6 dígitos
            ([7, 88, 999, 1234, 56789, 0], 2),     # 88 y 1234
            ([], 0),                              # Lista vacía, resultado 0
            ([111, 222, 333], 0),                 # Todos con longitud impar
        ]
    )
    def test_find_numbers(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método findNumbers.

        Args:
            nums (List[int]): Lista de enteros de entrada.
            expected_output (int): Número esperado de elementos con longitud par.
        """
        assert self.solution.findNumbers(nums) == expected_output
