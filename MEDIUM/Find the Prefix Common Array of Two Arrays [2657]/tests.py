import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "A, B, expected_output",
        [
            ([1, 3, 2, 4], [3, 1, 2, 4], [0, 1, 2, 3]),  # Caso con algunos elementos comunes a partir del índice 1
            ([1, 2, 3], [3, 2, 1], [0, 1, 2]),           # Lista más pequeña con común desde el primer índice
            ([1, 5, 3], [5, 3, 1], [0, 1, 2]),           # Elementos comunes en el primer y último índice
            ([1, 2, 3], [4, 5, 6], [0, 0, 0]),           # Sin elementos comunes, debe devolver [0, 0, 0]
            ([10, 20, 30], [5, 10, 20], [0, 1, 2]),      # Primeros números comunes, sin coincidencias en el último
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [0, 1, 2, 3, 4]),  # Casos donde todos los números coinciden en su respectivo índice
            ([100, 200, 300], [100, 300, 200], [0, 1, 2]),  # El orden no importa pero los números son iguales
            ([1, 4, 6], [4, 6, 2], [0, 1, 2]),           # Intersección gradual de los números a lo largo de los índices
            ([9, 7, 5], [7, 9, 5], [0, 1, 2]),           # Orden aleatorio pero todos los números comunes
            ([1, 2, 3, 4], [5, 6, 7, 8], [0, 0, 0, 0]),  # Ningún elemento común, todos ceros
        ]
    )
    def test_find_the_prefix_common_array(self, A, B, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findThePrefixCommonArray.

        Args:
            A (List[int]): La primera lista de enteros.
            B (List[int]): La segunda lista de enteros.
            expected_output (List[int]): La lista de resultados esperados con los elementos comunes en cada índice.
        """
        assert self.solution.findThePrefixCommonArray(A, B) == expected_output
