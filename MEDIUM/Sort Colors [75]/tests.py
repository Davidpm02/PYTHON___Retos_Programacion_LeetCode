import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_list, expected_output",
        [
            ([3, 2, 1, 0, 2, 1, 3], [0, 1, 1, 2, 2, 3, 3]),  # Caso general
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),              # Ya ordenado
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),              # Orden inverso
            ([1], [1]),                                      # Un único elemento
            ([], []),                                        # Lista vacía
            ([2, 2, 2, 2], [2, 2, 2, 2]),                    # Todos iguales
            ([0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1]),        # Solo ceros y unos
        ],
    )
    def test_sort_colors(self, input_list, expected_output):
        """
        Prueba parametrizada para validar el método sortColors que ordena la lista in-place.

        Args:
            input_list (List[int]): Lista desordenada de números.
            expected_output (List[int]): Lista ordenada esperada.
        """
        self.solution.sortColors(input_list)
        assert input_list == expected_output
