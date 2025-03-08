import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, True),   # 1 es 3^0, por lo que es una potencia de 3.
            (3, True),   # 3 es 3^1.
            (9, True),   # 9 es 3^2.
            (12, True),  # 12 = 3^0 + 3^1 + 3^2.
            (21, True),  # 21 = 3^0 + 3^2.
            (28, False), # 28 no se puede representar solo con potencias de 3.
            (91, False), # 91 no es suma de potencias de 3.
            (27, True),  # 27 es 3^3.
            (30, False), # 30 no puede expresarse con potencias de 3.
            (243, True), # 243 es 3^5.
        ]
    )
    def test_check_powers_of_three(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función checkPowersOfThree.

        Args:
            n (int): El número que se probará si puede expresarse como suma de potencias de 3.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.checkPowersOfThree(n) == expected_output