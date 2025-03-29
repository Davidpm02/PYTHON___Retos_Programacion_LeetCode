import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, rectangles, expected_output",
        [
            (5, [[1, 1, 3, 3], [4, 1, 5, 3], [1, 4, 5, 5]], True),  # Ejemplo con corte válido
            (5, [[1, 1, 2, 2], [2, 1, 3, 2], [3, 1, 4, 2]], False), # No hay forma de cortar en 3 partes
            (6, [[1, 1, 3, 3], [3, 1, 6, 3], [1, 4, 6, 6]], True),  # Corte horizontal posible
            (4, [[1, 1, 2, 2], [3, 1, 4, 2], [1, 3, 4, 4]], True),  # Corte vertical posible
            (5, [[1, 1, 5, 5]], False),  # Solo un rectángulo, no se puede partir en 3 grupos
        ]
    )
    def test_check_valid_cuts(self, n, rectangles, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función checkValidCuts.

        Args:
            n (int): Dimensión del espacio.
            rectangles (List[List[int]]): Lista de rectángulos.
            expected_output (bool): Resultado esperado.
        """
        assert self.solution.checkValidCuts(n, rectangles) == expected_output