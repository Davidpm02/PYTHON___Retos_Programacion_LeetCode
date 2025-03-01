import pytest
from challenge import Solution  # Importo la clase Solution desde el archivo challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "arr, expected_output",
        [
            ([1, 2, 3, 4, 5, 6, 7, 8], 5),       # Subsequencia Fibonacci-like más larga: [1, 2, 3, 5, 8]
            ([1, 3, 7, 11, 12, 14, 18], 3),      # Subsequencia Fibonacci-like más larga: [3, 7, 11]
            ([1, 2, 3], 3),                      # La subsecuencia Fibonacci-like más corta posible
            ([1, 1, 1, 1, 1], 0),                # No se puede formar una subsecuencia Fibonacci-like
            ([1, 2, 4, 5, 7, 11, 12, 13, 14, 18], 5),  # Subsequencia Fibonacci-like más larga: [1, 2, 3, 5, 8]
            ([5, 8, 13, 21, 34, 55], 6),         # Secuencia Fibonacci perfecta
            ([1, 2, 4, 6, 8, 10], 0),            # No se puede formar subsecuencia Fibonacci-like
            ([1, 2, 3, 5, 7, 11, 13, 19, 27], 5), # Subsequencia Fibonacci-like más larga: [1, 2, 3, 5, 8]
            ([1, 1, 2, 3, 5, 8, 13, 21, 34], 9), # Secuencia Fibonacci completa
            ([10, 20, 30, 50, 80, 130], 5),      # Subsequencia Fibonacci-like más larga
        ]
    )
    def test_lenLongestFibSubseq(self, arr, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función lenLongestFibSubseq.

        Args:
            arr (List[int]): El array con el que se probará la función.
            expected_output (int): El resultado esperado para la longitud de la subsecuencia.
        """
        assert self.solution.lenLongestFibSubseq(arr) == expected_output
