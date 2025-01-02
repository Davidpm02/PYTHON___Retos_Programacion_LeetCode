import pytest
from challenge import Solution  # Importamos la clase Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "area, expected_output",
        [
            (1, [1, 1]),         # Caso donde el área es 1, el rectángulo debe ser 1x1
            (4, [2, 2]),         # El área es 4, por lo tanto 2x2 es la forma más eficiente
            (6, [3, 2]),         # El área es 6, el rectángulo más adecuado es 3x2
            (9, [3, 3]),         # El área es 9, el rectángulo debe ser 3x3
            (12, [4, 3]),        # El área es 12, el rectángulo de 4x3 es la forma más eficiente
            (16, [4, 4]),        # Área de 16, el mejor rectángulo es 4x4 (un cuadrado)
            (100, [10, 10]),     # Para área de 100, se obtiene un rectángulo de 10x10
            (30, [6, 5]),        # Área 30, el rectángulo óptimo es 6x5
            (1000, [40, 25]),    # El área es 1000, el rectángulo mejor ajustado es 40x25
        ]
    )
    def test_construct_rectangle(self, area, expected_output):
        """
        Prueba parametrizada para validar la función constructRectangle.

        Args:
            area (int): El área del rectángulo.
            expected_output (List[int]): El resultado esperado para las dimensiones del rectángulo.
        """
        assert self.solution.constructRectangle(area) == expected_output
