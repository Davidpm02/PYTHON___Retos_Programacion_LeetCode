import pytest
from challenge import Solution  # Importamos la clase Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (22, 2),       # Representación binaria: 10110, distancia máxima entre bits 1 = 2
            (5, 2),        # Representación binaria: 101, distancia máxima entre bits 1 = 2
            (6, 1),        # Representación binaria: 110, distancia máxima entre bits 1 = 1
            (8, 0),        # Representación binaria: 1000, no hay bits 1 adyacentes
            (1, 0),        # Representación binaria: 1, no hay bits 1 adyacentes
            (15, 3),       # Representación binaria: 1111, distancia máxima entre bits 1 = 3
            (129, 7),      # Representación binaria: 10000001, distancia máxima entre bits 1 = 7
            (17, 4),       # Representación binaria: 10001, distancia máxima entre bits 1 = 4
            (1024, 0),     # Representación binaria: 10000000000, no hay bits 1 adyacentes
            (1023, 9),     # Representación binaria: 1111111111, distancia máxima entre bits 1 = 9
        ]
    )
    def test_binary_gap(self, n, expected_output):
        """
        Prueba parametrizada para validar la función binaryGap.

        Args:
            n (int): El número cuyo valor de distancia máxima entre bits 1 debe calcularse.
            expected_output (int): El valor esperado de la distancia máxima entre bits 1.
        """
        assert self.solution.binaryGap(n) == expected_output
