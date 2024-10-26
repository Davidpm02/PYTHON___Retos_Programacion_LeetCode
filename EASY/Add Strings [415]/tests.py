import pytest
from challenge import Solution  # Importamos la clase Solution para acceder al método a probar


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num1, num2, expected_output",
        [
            ("123", "456", "579"),                # Suma de números positivos
            ("0", "0", "0"),                      # Caso de ceros
            ("999", "1", "1000"),                 # Suma con acarreo simple
            ("123456789", "987654321", "1111111110"),  # Suma de números grandes
            ("5000", "2500", "7500"),             # Suma con múltiplos de diez
            ("1000000000000000", "999999999999999", "1999999999999999"),  # Números muy grandes
            ("50", "75", "125"),                  # Caso básico de suma sin acarreo
            ("1234", "4321", "5555"),             # Números simétricos
            ("", "1234", "1234"),                 # Suma con una cadena vacía (si se permite esta entrada)
        ]
    )
    def test_add_strings(self, num1, num2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método addStrings.

        Args:
            num1 (str): Primer número en formato de cadena para la suma.
            num2 (str): Segundo número en formato de cadena para la suma.
            expected_output (str): El resultado esperado de la suma como cadena.
        """
        assert self.solution.addStrings(num1, num2) == expected_output
