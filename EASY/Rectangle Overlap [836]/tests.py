import pytest
from challenge import Solution  # Asegúrate de que el archivo se llame challenge.py y la clase Solution esté definida allí.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "rec1, rec2, expected_output",
        [
            # Rectángulos que se solapan
            ([0, 0, 2, 2], [1, 1, 3, 3], True),   # Se solapan parcialmente
            ([0, 0, 3, 3], [1, 1, 2, 2], True),   # Rec1 cubre parcialmente a Rec2

            # Rectángulos que no se solapan
            ([0, 0, 1, 1], [1, 1, 2, 2], False),  # No hay solapamiento
            ([0, 0, 1, 1], [2, 2, 3, 3], False),  # No hay solapamiento

            # Casos de solapamientos en los bordes
            ([0, 0, 2, 2], [2, 0, 3, 2], False),  # Toque justo en un borde (sin solapamiento)
            ([0, 0, 2, 2], [0, 2, 2, 3], False),  # Toque justo en un borde (sin solapamiento)

            # Casos de rectángulos con área nula (líneas o puntos)
            ([0, 0, 0, 0], [1, 1, 2, 2], False),  # Rec1 es un punto
            ([0, 0, 2, 2], [2, 0, 2, 2], False),  # Rec2 es una línea (sin solapamiento)
        ]
    )
    def test_isRectangleOverlap(self, rec1, rec2, expected_output):
        """
        Prueba parametrizada para validar la función isRectangleOverlap.

        Args:
            rec1 (List[int]): Las coordenadas de los dos rectángulos, cada una con su esquina inferior izquierda y superior derecha.
            rec2 (List[int]): El segundo rectángulo, similar a rec1.
            expected_output (bool): El resultado esperado, que será True si se solapan, False en caso contrario.
        """
        assert self.solution.isRectangleOverlap(rec1, rec2) == expected_output
