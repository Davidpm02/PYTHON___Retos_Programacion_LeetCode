import pytest
from challenge import Solution  # Importo la clase Solution desde el archivo del reto


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, -1, 2, -2, 3, -3], 3),     # Igual cantidad de positivos y negativos
            ([5, 10, 15, 20], 4),           # Solo números positivos
            ([-5, -10, -15, -20], 4),       # Solo números negativos
            ([0, 0, 0], 0),                 # Solo ceros, ningún positivo ni negativo
            ([1, 2, 3, -1, -2, -3, -4], 4), # Más negativos que positivos
            ([7, -8, 9, 10, -11], 3),       # Más positivos que negativos
            ([0, -1, -2, -3, -4, -5], 5),   # Solo negativos y ceros
            ([0, 1, 2, 3, 4, 5], 5),        # Solo positivos y ceros
            ([], 0),                        # Lista vacía
        ]
    )
    def test_maximum_count(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maximumCount.

        Args:
            nums (List[int]): La lista de enteros que se probará.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.maximumCount(nums) == expected_output