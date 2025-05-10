import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, 1),       # Solo 1 forma con una ficha de dominó vertical
            (2, 2),       # Dos formas: dos dominós verticales o dos horizontales
            (3, 5),       # Se puede usar trominós en L además de dominós
            (4, 11),      # Combinaciones posibles crecen con n
            (5, 24),      # Verificado contra soluciones dinámicas conocidas
            (10, 1255),   # Caso más grande para validar rendimiento
            (20, 98950096),  # Validamos contra valores de referencia más grandes
        ]
    )
    def test_num_tilings(self, n, expected_output):
        """
        Prueba parametrizada para verificar el número de formas de embaldosar un tablero 2×n.

        Args:
            n (int): Ancho del tablero.
            expected_output (int): Número esperado de formas de embaldosar.
        """
        assert self.solution.numTilings(n) == expected_output