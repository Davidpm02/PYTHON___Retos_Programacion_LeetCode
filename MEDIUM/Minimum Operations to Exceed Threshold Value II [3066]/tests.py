import pytest
from challenge import Solution  

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 2, 3, 9, 10, 12], 7, 2),  # Se requieren dos operaciones para que todos los elementos sean >= 7
            ([5, 6, 7, 8, 9], 10, 1),      # Solo una operación es necesaria
            ([10, 20, 30], 5, 0),          # Todos los números ya son >= k, no se requieren operaciones
            ([1, 1, 1, 1], 10, 3),         # Se requieren múltiples operaciones para superar 10
            ([1, 2], 10, 1),               # Caso con solo dos elementos
        ]
    )
    def test_min_operations(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minOperations.

        Args:
            nums (List[int]): Lista de números enteros.
            k (int): Límite mínimo deseado.
            expected_output (int): El número mínimo de operaciones esperadas.
        """
        assert self.solution.minOperations(nums, k) == expected_output
