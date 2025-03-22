import pytest
from challenge import Solution  # Importamos la clase Solution desde challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([3, 3, 2, 2, 1, 1], True),   # Todos los números aparecen en parejas
            ([1, 2, 3, 4], False),        # No se pueden formar parejas
            ([5, 5, 5, 5, 6, 6], True),   # Se pueden formar parejas con cada número
            ([7, 7, 8, 8, 9], False),     # Cantidad impar de números, imposible dividir
            ([10, 10, 10, 10], True),     # Todos los números pueden formar parejas
            ([1, 1, 2, 2, 3, 3, 3], False),  # Un número con frecuencia impar impide la división
            ([0, 0, 0, 0, 0, 0], True),   # Todos ceros, se pueden formar parejas
        ]
    )
    def test_divide_array(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función divideArray.

        Args:
            nums (List[int]): Lista de números enteros.
            expected_output (bool): El resultado esperado de la función divideArray.
        """
        assert self.solution.divideArray(nums) == expected_output
