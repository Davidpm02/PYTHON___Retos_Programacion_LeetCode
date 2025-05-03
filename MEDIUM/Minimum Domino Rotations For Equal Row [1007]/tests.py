import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "tops, bottoms, expected_output",
        [
            ([2, 1, 2, 4, 2, 2], [2, 2, 2, 2, 2, 4], 2),  # Caso donde se puede hacer igual todos los tops o bottoms con 2 rotaciones
            ([3, 5, 1, 2, 6], [3, 3, 3, 3, 3], 2),          # Todos los bottoms ya son iguales, 2 rotaciones en tops
            ([4, 4, 4, 4], [4, 4, 4, 4], 0),                  # Todos los tops y bottoms son iguales, sin rotaciones
            ([1, 2, 3], [3, 2, 1], -1),                       # No es posible hacer que todos sean iguales
            ([1, 1, 1], [1, 1, 1], 0),                        # Ya están todos los valores iguales en tops y bottoms
            ([6, 6, 6, 2], [6, 6, 6, 6], 1),                  # Un cambio en bottoms para que todo sea 6
            ([1, 1, 1], [2, 2, 2], 3),                        # Todos los tops y bottoms son diferentes, necesitamos 3 cambios
            ([3, 3, 3], [4, 4, 4], 3),                        # Casos con valores distintos pero ambos con la misma cantidad de rotaciones
            ([4, 1, 2, 3], [4, 4, 4, 4], 1),                  # Casos donde los cambios se pueden hacer fácilmente
            ([2, 3, 1, 2], [2, 2, 2, 2], 2),                  # Necesitamos 2 rotaciones para hacer que todos sean 2
        ]
    )
    def test_min_domino_rotations(self, tops, bottoms, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método minDominoRotations.

        Args:
            tops (List[int]): Lista de números en la parte superior de los dominós.
            bottoms (List[int]): Lista de números en la parte inferior de los dominós.
            expected_output (int): Número esperado de rotaciones o -1 si no es posible.
        """
        assert self.solution.minDominoRotations(tops, bottoms) == expected_output
