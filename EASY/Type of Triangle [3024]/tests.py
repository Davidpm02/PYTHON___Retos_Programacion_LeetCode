import pytest
from challenge import Solution  # Asegúrate de que challenge.py contiene la clase Solution

class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "sides, expected_output",
        [
            ([3, 3, 3], "equilateral"),   # Todos los lados iguales → equilátero
            ([4, 4, 5], "isosceles"),     # Dos lados iguales → isósceles
            ([5, 4, 3], "scalene"),       # Todos los lados diferentes → escaleno
            ([1, 2, 3], "none"),          # No se cumple la desigualdad triangular
            ([10, 1, 1], "none"),         # No se puede formar triángulo
            ([2, 2, 3], "isosceles"),     # Dos lados iguales, uno diferente
            ([7, 10, 5], "scalene"),      # Triángulo válido escaleno
            ([6, 6, 6], "equilateral"),   # Equilátero con otros valores
            ([0, 0, 0], "none"),          # No es posible formar triángulo con ceros
            ([100, 100, 200], "isosceles"),  # Isósceles válido
        ]
    )
    def test_triangle_type(self, sides, expected_output):
        """
        Prueba parametrizada para verificar el tipo de triángulo que se puede formar
        con las longitudes proporcionadas.

        Args:
            sides (List[int]): Lista de enteros que representan los lados del triángulo.
            expected_output (str): Tipo de triángulo esperado.
        """
        assert self.solution.triangleType(sides) == expected_output
