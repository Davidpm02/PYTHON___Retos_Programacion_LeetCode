import pytest
from challenge import Solution  # Importamos la clase Solution para acceder al método a probar


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (5, 2),       # Caso básico: 5 monedas completan 2 filas
            (8, 3),       # Caso básico: 8 monedas completan 3 filas
            (1, 1),       # Un único escalón se completa con 1 moneda
            (0, 0),       # Sin monedas, sin filas completas
            (10, 4),      # 10 monedas completan 4 filas
            (15, 5),      # 15 monedas completan 5 filas exactas
            (20, 5),      # 20 monedas no alcanzan para una sexta fila, completando solo 5
            (100, 13),    # 100 monedas completan 13 filas
            (5050, 100),  # 5050 monedas completan 100 filas exactas
            (5000, 99),   # 5000 monedas completan 99 filas, no alcanzando para la fila 100
        ]
    )
    def test_arrange_coins(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método arrangeCoins.

        Args:
            n (int): Número de monedas disponibles para construir la escalera.
            expected_output (int): Número de escalones completos esperados.
        """
        assert self.solution.arrangeCoins(n) == expected_output
