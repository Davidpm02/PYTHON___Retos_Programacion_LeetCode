import pytest
from challenge import Solution  # Importa la clase Solution desde tu archivo de reto

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            (100, "202"),            # Caso típico de número positivo, en base 7: 100 -> 202
            (7, "10"),               # Caso con el número exacto de base 7
            (0, "0"),                # Caso con cero, la base 7 de 0 es simplemente "0"
            (-7, "-10"),             # Caso con número negativo, base 7 de -7 es "-10"
            (-100, "-202"),          # Caso con número negativo, base 7 de -100 es "-202"
            (6, "6"),                # Caso con número menor a 7, no hay conversión, es el mismo número en base 7
            (49, "101"),             # Caso con múltiplo exacto de 7, 49 -> 101
            (344, "1013"),           # Un número más grande, 344 -> 1013 en base 7
            (-344, "-1013"),         # Caso con número negativo grande, -344 -> -1013 en base 7
        ]
    )
    def test_convert_to_base7(self, num, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función convertToBase7.

        Args:
            num (int): El número a convertir a base 7.
            expected_output (str): El resultado esperado para la conversión a base 7.
        """
        assert self.solution.convertToBase7(num) == expected_output
