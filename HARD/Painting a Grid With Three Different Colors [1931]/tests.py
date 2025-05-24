import pytest
from challenge import Solution  # Asegúrate de que el archivo del reto se llama challenge.py

class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "m, n, expected_output",
        [
            (1, 1, 3),      # 3 formas de pintar una única celda
            (1, 2, 6),      # Cada celda de la columna debe ser diferente al anterior (3 * 2)
            (2, 1, 6),      # Se generan las combinaciones posibles de colores sin repetición vertical
            (2, 2, 18),     # Combinaciones válidas horizontales y verticales
            (3, 1, 12),     # Patrones válidos en una sola columna de altura 3
            (3, 2, 54),     # Solución precomputada para cuadrícula 3x2
            (1, 3, 6),      # 3 colores en cada celda con restricción de adyacencia
        ]
    )
    def test_color_the_grid(self, m, n, expected_output):
        """
        Prueba parametrizada para validar distintos tamaños de cuadrícula m x n
        y comprobar si el número de formas de colorear es el esperado.

        Args:
            m (int): número de filas.
            n (int): número de columnas.
            expected_output (int): número esperado de formas válidas de colorear.
        """
        assert self.solution.colorTheGrid(m, n) == expected_output
