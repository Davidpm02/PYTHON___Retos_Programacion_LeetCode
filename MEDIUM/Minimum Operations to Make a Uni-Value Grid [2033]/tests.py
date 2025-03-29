import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, x, expected_output",
        [
            ([[2, 4], [6, 8]], 2, 4),  # Caso base con números pares
            ([[1, 5], [9, 13]], 2, -1), # Caso donde no es posible igualar valores
            ([[3, 3, 3], [3, 3, 3]], 1, 0),  # Todos los valores son iguales
            ([[1, 3, 5], [7, 9, 11]], 2, 9),  # Serie aritmética con diferencia 2
            ([[4, 8, 12], [16, 20, 24]], 4, 12),  # Serie con diferencia múltiplo de x
        ]
    )
    def test_min_operations(self, grid, x, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minOperations.

        Args:
            grid (List[List[int]]): Matriz de valores.
            x (int): Incremento permitido en cada operación.
            expected_output (int): Resultado esperado.
        """
        assert self.solution.minOperations(grid, x) == expected_output