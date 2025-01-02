import pytest
from challenge import Solution  # Asegúrate de que el archivo de la solución sea challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "g, s, expected_output",
        [
            ([1, 2, 3], [1, 1], 1),        # Solo un niño puede estar contento, el niño que necesita tamaño 1 puede ser satisfecho por una galleta de tamaño 1
            ([1, 2], [1, 2, 3], 2),        # Todos los niños pueden ser felices con una galleta que cubra sus necesidades
            ([10, 9, 8], [1, 2, 3], 0),    # Ningún niño puede estar contento porque las galletas son demasiado pequeñas
            ([1, 2, 3], [1, 2, 3], 3),     # Todos los niños pueden estar contentos con las galletas correspondientes
            ([1, 2], [3], 1),              # Solo un niño puede estar satisfecho por una galleta, el otro queda sin galleta
            ([1, 2, 3, 4], [1, 3], 2),     # Con pocos tamaños de galletas, solo 2 niños pueden estar contentos
            ([1, 3, 2], [1, 2, 3], 3),     # Se cubren perfectamente todos los niños con las galletas
            ([5, 6], [6, 5], 2),           # Todos los niños pueden estar contentos al coincidir perfectamente
            ([1, 3], [1, 2], 1),           # Solo un niño puede estar satisfecho
            ([1, 5, 6], [2, 3, 4, 6], 3),  # Todos los niños pueden estar contentos, tienen galletas suficientes
        ]
    )
    def test_find_content_children(self, g, s, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findContentChildren.

        Args:
            g (List[int]): Los tamaños de galleta que los niños necesitan.
            s (List[int]): Los tamaños de las galletas disponibles.
            expected_output (int): El número esperado de niños satisfechos.
        """
        assert self.solution.findContentChildren(g, s) == expected_output
