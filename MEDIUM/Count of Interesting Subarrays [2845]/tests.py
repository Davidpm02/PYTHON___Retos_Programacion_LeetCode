import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, modulo, k, expected_output",
        [
            ([3, 1, 9, 6], 3, 0, 5),             # Muchos subarrays donde cnt % 3 == 0
            ([2, 3, 3, 2, 2], 5, 2, 5),           # Buscamos cnt tal que cnt % 5 == 2
            ([1, 2, 3, 4, 5], 2, 1, 9),           # Subarrays con elementos impares
            ([1, 1, 1, 1], 2, 0, 4),              # Subarrays donde la cantidad de 1s es par
            ([0, 0, 0], 1, 0, 6),                 # Todos los subarrays son interesantes
            ([5, 7, 11, 13], 4, 3, 4),             # Subarrays donde (número % 4) == 3
            ([], 3, 1, 0),                        # Array vacío, no hay subarrays
            ([1], 1, 0, 1),                       # Único elemento donde 1 % 1 == 0
            ([1, 2, 3, 4, 5, 6], 3, 2, 7),        # Probando con varios subarrays mezclados
            ([10, 20, 30], 10, 0, 6),             # Cada número divisible por 10
        ]
    )
    def test_count_interesting_subarrays(self, nums, modulo, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countInterestingSubarrays.

        Args:
            nums (List[int]): Lista de números de entrada.
            modulo (int): Valor de módulo para calcular la condición.
            k (int): Residuo deseado.
            expected_output (int): Número esperado de subarrays interesantes.
        """
        assert self.solution.countInterestingSubarrays(nums, modulo, k) == expected_output
