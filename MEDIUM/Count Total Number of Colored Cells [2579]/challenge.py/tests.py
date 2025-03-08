import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, 1),   # En el primer minuto solo se colorea una celda.
            (2, 5),   # En el segundo minuto, hay 5 celdas coloreadas.
            (3, 13),  # En el tercer minuto, hay 13 celdas coloreadas.
            (4, 25),  # En el cuarto minuto, se espera 4^2 + 3^2 = 25 celdas.
            (5, 41),  # En el quinto minuto, se espera 5^2 + 4^2 = 41 celdas.
            (6, 61),  # En el sexto minuto, se espera 6^2 + 5^2 = 61 celdas.
            (10, 181),# En el décimo minuto, se espera 10^2 + 9^2 = 181 celdas.
        ]
    )
    def test_colored_cells(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función coloredCells.

        Args:
            n (int): Número de minutos transcurridos.
            expected_output (int): Número esperado de celdas coloreadas.
        """
        assert self.solution.coloredCells(n) == expected_output