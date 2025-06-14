import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, p, expected_output",
        [
            ([1, 3, 6, 19, 20], 2, 2),             # Puedo formar 2 pares: (1,3) y (19,20)
            ([10, 1, 2, 7, 6, 5], 3, 1),           # Puedo formar 3 pares con diff <= 1: (1,2), (5,6), (7,10)
            ([4, 2, 1, 3], 1, 1),                  # Un solo par (1,2) es suficiente
            ([1, 1000000000], 0, 0),               # No se necesitan pares, resultado 0
            ([1, 2, 3, 4, 5, 6], 3, 1),            # Tres pares consecutivos con diff 1
            ([1, 3, 4, 9, 10], 2, 1),              # (3,4) y (9,10)
            ([1, 6, 19, 20, 21, 22], 2, 1),        # (20,21) y (21,22) posibles
            ([1, 2], 1, 1),                        # Solo un par posible
            ([1, 3], 1, 2),                        # Solo un par pero con diff mayor
            ([5, 2, 1, 3], 2, 1),                  # Dos pares (1,2) y (3,5)
        ]
    )
    def test_minimize_max(self, nums, p, expected_output):
        """
        Prueba parametrizada para validar múltiples escenarios del método minimizeMax.

        Args:
            nums (List[int]): Lista de números a emparejar.
            p (int): Número mínimo de pares requeridos.
            expected_output (int): Diferencia mínima máxima posible.
        """
        assert self.solution.minimizeMax(nums, p) == expected_output
