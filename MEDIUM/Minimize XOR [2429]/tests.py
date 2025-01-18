import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num1, num2, expected_output",
        [
            (3, 5, 5),  # Caso básico, buscamos el número con el mismo número de bits fijados de num2 (5 -> 0101 en binario)
            (2, 3, 3),  # Ambos números con bits similares
            (7, 10, 11), # El número resultante con la cantidad correcta de bits (7 -> 0111, 10 -> 1010, mínimo Xor 1011 = 11)
            (0, 3, 3),   # Caso donde num1 es cero, y num2 tiene 2 bits fijados
            (8, 12, 12),  # 1000 y 1100, la mejor forma de ajustar es 1100
            (10, 13, 15),  # 1010 y 1101, el mejor ajuste de bits es 1111
            (1, 8, 8),    # 0001 y 1000, resultado más cercano sería 1000
            (0, 31, 31),  # 0 tiene 0 bits y 31 tiene 5 bits, la opción resultante es 31
            (7, 7, 7),    # Ambos números con los mismos bits ya fijados
            (16, 29, 29),  # 16 -> 10000 y 29 -> 11101, el valor más cercano es 11101 (29)
        ]
    )
    def test_minimize_xor(self, num1, num2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minimizeXor.

        Args:
            num1 (int): El primer número para el cual minimizamos el XOR.
            num2 (int): El segundo número que debe tener el mismo número de bits fijados.
            expected_output (int): El número que minimiza el XOR con el mismo número de bits fijados que num2.
        """
        assert self.solution.minimizeXor(num1, num2) == expected_output
