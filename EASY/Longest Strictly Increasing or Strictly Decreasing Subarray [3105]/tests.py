import pytest
from challenge import Solution  # Asegúrate de que el archivo donde tienes el código se llama challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_nums, expected_output",
        [
            ([1, 2, 3, 4, 5], 5),               # Subarray creciente completo
            ([5, 4, 3, 2, 1], 5),               # Subarray decreciente completo
            ([1, 2, 3, 1, 2, 3, 4], 4),         # Subarrays crecientes y decrecientes alternados
            ([1, 3, 2, 1, 4, 5, 6], 4),         # Subarray creciente y decreciente
            ([1, 3, 2, 1, 3, 5], 3),            # Mezcla de subarrays con diferentes longitudes
            ([1, 1, 1, 1], 4),                 # Subarray constante (creciente o decreciente)
            ([1, 2, 2, 3, 4], 4),               # Subarray creciente y constante
            ([1, 3, 2, 4, 5], 3),               # Subarray decreciente y luego creciente
            ([1], 1),                          # Caso con solo un elemento
            ([], 0),                           # Caso con lista vacía
        ]
    )
    def test_longest_monotonic_subarray(self, input_nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función longestMonotonicSubarray.

        Args:
            input_nums (List[int]): La lista de enteros que se probará para encontrar el subarray más largo monótono.
            expected_output (int): La longitud esperada del subarray monótono más largo.
        """
        assert self.solution.longestMonotonicSubarray(input_nums) == expected_output
