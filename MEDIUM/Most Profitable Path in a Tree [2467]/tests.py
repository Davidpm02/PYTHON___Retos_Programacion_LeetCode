import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "edges, bob, amount, expected_profit",
        [
            ([[0, 1], [1, 2], [1, 3]], 3, [3, 2, 1, 4], 3),  # Caso básico con árbol pequeño
            ([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], 6, [10, -5, -2, 7, 6, -3, 4], 13),  # Árbol balanceado
            ([[0, 1], [1, 2], [2, 3], [3, 4]], 4, [5, 4, 3, 2, 1], 5),  # Árbol lineal
            ([[0, 1], [1, 2], [2, 3], [3, 4]], 2, [10, 10, 10, 10, 10], 20),  # Caso con valores positivos
            ([[0, 1], [1, 2], [2, 3], [3, 4]], 2, [-10, -10, -10, -10, -10], -10)  # Caso con valores negativos
        ]
    )
    def test_mostProfitablePath(self, edges, bob, amount, expected_profit):
        """
        Prueba parametrizada para validar la función mostProfitablePath con diferentes grafos.
        """
        assert self.solution.mostProfitablePath(edges, bob, amount) == expected_profit
