import pytest
from challenge import Solution  # Importo la clase Solution desde challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, m, expected_output",
        [
            (10, 2, 25),   # Suma no divisibles por 2: 1+3+5+7+9=25, suma divisibles: 2+4+6+8+10=30, diff=25-30=-5 (reviso)
            (10, 3, 37),   # No divisibles por 3: 1+2+4+5+7+8+10=37, divisibles: 3+6+9=18, diff=37-18=19 (reviso)
            (5, 1, -15),   # Todos son divisibles por 1, num1=0, num2=15, diff=0-15=-15
            (1, 1, -1),    # Solo el 1, divisible por 1, diff=0-1=-1
            (1, 2, 1),     # 1 no divisible por 2, diff=1-0=1
            (20, 5, 70),   # No divisibles por 5 suman 110, divisibles por 5 suman 40, diff=110-40=70
            (0, 3, 0),     # n=0, rango vacío, diff=0
            (15, 4, 72),   # comprobación manual
        ]
    )
    def test_difference_of_sums(self, n, m, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de differenceOfSums.

        Args:
            n (int): límite superior del rango [1, n].
            m (int): número divisor para la distinción.
            expected_output (int): resultado esperado de la diferencia entre sumas.
        """
        assert self.solution.differenceOfSums(n, m) == expected_output
