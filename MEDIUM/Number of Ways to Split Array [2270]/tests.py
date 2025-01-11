import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([10, 4, -8, 7], 2),        # Caso con una lista simple de enteros
            ([1, 2, 3, 4, 5], 1),       # Caso en que solo hay una división válida
            ([1, 1, 1, 1], 3),          # Caso con una lista con todos los elementos iguales
            ([5, 10, 15], 1),           # Caso con números ascendentes y una sola división válida
            ([1, 2, 3, 4], 2),          # Caso con una lista más corta y 2 divisiones válidas
            ([0, 0, 0, 0], 3),          # Caso con una lista de ceros
            ([1, 1, 1, 1, 1], 4),       # Caso con una lista de unos y múltiples divisiones
            ([3, 1, 2, 4, 6], 3),       # Caso con una combinación de números positivos
            ([5, 7, 10, 20, 30], 2),    # Caso con una lista ascendente
            ([1, 2, 3, 10, 10, 2], 3),  # Caso con varios elementos que provocan divisiones válidas
            ([10], 0),                  # Caso con una sola cantidad (no puede dividirse)
        ]
    )
    def test_ways_to_split_array(self, nums, expected_output):
        """
        Prueba parametrizada para validar la función waysToSplitArray.

        Args:
            nums (List[int]): Lista de enteros a dividir.
            expected_output (int): El número esperado de divisiones válidas para la lista dada.
        """
        assert self.solution.waysToSplitArray(nums) == expected_output
