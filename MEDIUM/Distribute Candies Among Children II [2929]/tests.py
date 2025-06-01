import pytest
from challenge import Solution  # Importo la clase Solution con el método distributeCandies


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia Solution para usar en los tests."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, limit, expected_output",
        [
            (3, 1, 10),   # Caso simple: 3 caramelos, límite 1 por niño
            (5, 2, 21),   # Más caramelos y límite 2
            (0, 5, 1),    # Sin caramelos, solo una forma (todos 0)
            (10, 0, 1),   # Límite 0: todos deben tener 0 o menos, solo 1 forma (0,0,10) no válido, por límite 0 sólo (0,0,0)
            (6, 3, 28),   # Caso más grande
            (7, 10, 36),  # Límite mayor que n, debería coincidir con combinaciones sin límite
            (2, 1, 6),    # Pequeño número de caramelos y límite pequeño
        ]
    )
    def test_distribute_candies(self, n, limit, expected_output):
        """
        Test parametrizado para validar diferentes casos del reparto de caramelos.

        Args:
            n (int): Número total de caramelos.
            limit (int): Límite máximo de caramelos por niño.
            expected_output (int): Número esperado de combinaciones válidas.
        """
        assert self.solution.distributeCandies(n, limit) == expected_output
