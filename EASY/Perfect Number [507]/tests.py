import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            # Casos positivos de números perfectos
            (6, True),   # 6 es un número perfecto: 1 + 2 + 3 = 6
            (28, True),  # 28 es un número perfecto: 1 + 2 + 4 + 7 + 14 = 28
            (496, True), # 496 es un número perfecto: 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496
            (8128, True),# 8128 es un número perfecto: 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064 = 8128
            
            # Casos negativos (números no perfectos)
            (10, False),   # 10 no es un número perfecto: divisores son 1, 2, 5, pero 1 + 2 + 5 = 8 != 10
            (12, False),   # 12 no es un número perfecto: divisores son 1, 2, 3, 4, 6, pero 1 + 2 + 3 + 4 + 6 = 16 != 12
            (20, False),   # 20 no es un número perfecto: divisores son 1, 2, 4, 5, 10, pero 1 + 2 + 4 + 5 + 10 = 22 != 20
            (50, False),   # 50 no es un número perfecto: divisores son 1, 2, 5, 10, 25, pero 1 + 2 + 5 + 10 + 25 = 43 != 50
            
            # Casos con números más pequeños (que no son perfectos)
            (1, False),    # 1 no es un número perfecto: no tiene divisores, pero no es perfecto
            (2, False),    # 2 no es un número perfecto: divisores son 1, pero 1 != 2
            
            # Casos de valores grandes (mayores que 10000)
            (100000, False), # Este es un número que no es perfecto, un caso más grande
        ]
    )
    def test_checkPerfectNumber(self, num, expected_output):
        """
        Prueba parametrizada para validar la función checkPerfectNumber.

        Args:
            num (int): El número a evaluar.
            expected_output (bool): El resultado esperado si el número es perfecto o no.
        """
        assert self.solution.checkPerfectNumber(num) == expected_output
