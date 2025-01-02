import pytest
from challenge import Solution  # Importamos la clase Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (5, True),        # Binario de 5: 101, tiene bits alternos (1, 0, 1)
            (7, False),       # Binario de 7: 111, no tiene bits alternos
            (10, True),       # Binario de 10: 1010, tiene bits alternos (1, 0, 1, 0)
            (11, False),      # Binario de 11: 1011, no tiene bits alternos
            (8, False),       # Binario de 8: 1000, no tiene bits alternos
            (1, True),        # Binario de 1: 1, tiene solo un bit, por lo que se considera alternante
            (2, True),        # Binario de 2: 10, tiene bits alternos (1, 0)
            (3, False),       # Binario de 3: 11, no tiene bits alternos
            (4, False),       # Binario de 4: 100, no tiene bits alternos
            (6, True),        # Binario de 6: 110, tiene bits alternos (1, 0)
        ]
    )
    def test_has_alternating_bits(self, n, expected_output):
        """
        Prueba parametrizada para validar la función hasAlternatingBits.

        Args:
            n (int): El número cuya representación binaria se analizará.
            expected_output (bool): El resultado esperado para verificar si tiene bits alternos.
        """
        assert self.solution.hasAlternatingBits(n) == expected_output
