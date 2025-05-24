import pytest
from challenge import Solution  # challenge.py debe contener la clase Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, queries, expected_output",
        [
            # Caso base: aplicar operaciones que dejan todos los elementos a 0
            ([1, 1, 1], [[0, 0], [1, 1], [2, 2]], True),

            # Caso donde una posición queda sin suficientes decrementos
            ([2, 1, 1], [[0, 0], [1, 1], [2, 2]], False),

            # Todas las posiciones ya están a 0, sin queries
            ([0, 0, 0], [], True),

            # Caso sin suficiente cobertura en los queries
            ([1, 1, 1], [[0, 1]], False),

            # Reducción justa para todos los elementos
            ([2, 2, 2], [[0, 2], [0, 2]], True),

            # Aplicación de reducción solo parcial, uno se queda sin cubrir
            ([3, 2, 1], [[0, 1], [0, 1]], False),

            # Un solo elemento cubierto completamente
            ([3], [[0, 0], [0, 0], [0, 0]], True),

            # Un solo elemento sin suficiente cobertura
            ([3], [[0, 0], [0, 0]], False),

            # Largos rangos con solapamiento que dejan el array a cero
            ([3, 3, 3, 3], [[0, 2], [1, 3], [0, 3]], True),

            # Edge case: los queries no hacen nada por fuera del rango
            ([1, 1, 1], [[0, 0], [2, 2], [1, 1], [3, 5]], True),
        ]
    )
    def test_is_zero_array(self, nums, queries, expected_output):
        """
        Prueba parametrizada para validar distintos casos del método isZeroArray.

        Args:
            nums (List[int]): Array original con valores a reducir.
            queries (List[List[int]]): Rango de índices donde aplicar reducción.
            expected_output (bool): Resultado esperado tras aplicar todas las queries.
        """
        assert self.solution.isZeroArray(nums, queries) == expected_output
