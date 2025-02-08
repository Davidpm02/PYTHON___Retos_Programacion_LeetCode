import pytest
from challenge import Solution  # Importo la clase Solution desde el fichero del reto


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([2, 3, 4, 6], 8),  # Caso base con valores pequeños
            ([1, 2, 4, 5, 10], 16),  # Diferentes combinaciones de productos
            ([1, 2, 3, 4, 6, 12], 40),  # Más números, más combinaciones
            ([1, 2, 3], 0),  # No hay combinaciones válidas
            ([2, 2, 2, 2], 24),  # Casos con números repetidos
            ([10, 20, 30, 40, 50], 8),  # Conjunto de números más grandes
            ([1, 1, 1, 1, 1, 1], 240),  # Todos los números iguales
            ([100, 200, 300, 400], 8),  # Números grandes
            ([3, 5, 15, 30, 10, 2], 40),  # Combinaciones variadas
        ]
    )
    def test_tuple_same_product(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función tupleSameProduct.

        Args:
            nums (List[int]): La lista de números a evaluar.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.tupleSameProduct(nums) == expected_output