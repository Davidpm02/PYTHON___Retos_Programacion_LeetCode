import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_arr, expected_output",
        [
            ([2, 6, 4, 1], False),                         # No hay suficientes impares consecutivos
            ([1, 3, 5], True),                             # Tres impares consecutivos exactos
            ([2, 1, 3, 5], True),                          # Tres impares consecutivos empezando desde la segunda posición
            ([1, 2, 3, 5, 7], True),                       # Hay una secuencia de tres impares consecutivos más adelante
            ([1, 3, 5, 7, 9], True),                       # Más de tres impares consecutivos
            ([1, 2, 1, 3, 5], True),                       # Impares interrumpidos y luego una secuencia válida
            ([1, 2, 3, 4, 5], False),                      # Aunque hay impares, no hay tres seguidos
            ([2, 4, 6, 8], False),                         # Ningún número impar
            ([1, 3, 2, 5, 7], False),                      # Dos secuencias de dos impares, pero interrumpidas
            ([], False),                                   # Lista vacía
            ([1], False),                                  # Solo un número impar
            ([1, 3], False),                               # Solo dos impares consecutivos
            ([2, 1, 3, 5, 2, 1, 3, 5], True),              # Dos secuencias válidas, la primera ya valida el retorno
        ]
    )
    def test_three_consecutive_odds(self, input_arr, expected_output):
        """
        Test parametrizado para verificar múltiples casos del método threeConsecutiveOdds.

        Args:
            input_arr (List[int]): Lista de enteros a evaluar.
            expected_output (bool): Resultado esperado del método.
        """
        assert self.solution.threeConsecutiveOdds(input_arr) == expected_output
