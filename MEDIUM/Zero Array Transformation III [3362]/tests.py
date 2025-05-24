import pytest
from challenge import Solution  # Asegúrate de que challenge.py contiene la clase Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution para las pruebas."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, queries, expected_output",
        [
            # Caso básico donde es posible eliminar 2 queries y aún reducir a cero
            (
                [3, 2, 1],
                [[0, 2], [0, 1], [1, 2]],
                2
            ),
            # Caso donde no es posible hacer el array 0, retorno -1
            (
                [1, 2, 3],
                [[0, 0], [1, 1]],
                -1
            ),
            # Caso donde el array ya es todo ceros, se pueden eliminar todas las queries
            (
                [0, 0, 0],
                [[0, 2], [1, 1]],
                2
            ),
            # Caso con un solo elemento y una query
            (
                [1],
                [[0, 0]],
                0
            ),
            # Caso donde solo se puede eliminar una query de dos
            (
                [2, 2],
                [[0, 0], [1, 1], [0, 1]],
                2
            ),
            # Caso con queries no solapadas que pueden eliminarse todas
            (
                [1, 1, 1],
                [[0, 0], [1, 1], [2, 2]],
                3
            ),
            # Caso con múltiples queries para cubrir una sola posición
            (
                [2],
                [[0, 0], [0, 0], [0, 0]],
                2
            ),
            # Caso donde es imposible reducir completamente a cero
            (
                [5, 5, 5],
                [[0, 0], [1, 1], [2, 2]],
                -1
            ),
            # Caso con un array largo y queries amplios
            (
                [1]*10,
                [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],
                5
            ),
        ]
    )
    def test_max_removal(self, nums, queries, expected_output):
        """
        Test parametrizado para validar distintos casos del método maxRemoval.

        Args:
            nums (List[int]): Array inicial con valores enteros.
            queries (List[List[int]]): Lista de queries para aplicar decrementos.
            expected_output (int): Valor esperado que representa el máximo número
                                   de queries que se pueden eliminar, o -1 si no es posible.
        """
        assert self.solution.maxRemoval(nums, queries) == expected_output
