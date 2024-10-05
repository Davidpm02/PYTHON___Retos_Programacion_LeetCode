import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("hello", "holle"),                         # Caso básico con vocales
            ("leetcode", "leotcede"),                   # Inversión de vocales en una cadena
            ("aA", "Aa"),                               # Vocales mayúsculas y minúsculas
            ("", ""),                                   # Cadena vacía
            ("", ""),                                   # Cadena vacía
            ("AeIoU", "UoIeA"),                         # Todas las vocales en mayúsculas
            ("This is a test.", "Thas os e tist."),    # Cadena con consonantes y vocales
            ("", ""),                                   # Cadena vacía
            ("UOIEA", "AEIOU"),                         # Todas las vocales en mayúsculas
            ("hEllO WoRld", "hOllE WoRld"),            # Mezcla de mayúsculas y minúsculas
        ]
    )
    def test_reverse_vowels(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función reverseVowels.

        Args:
            input_str (str): La cadena que se probará para invertir las vocales.
            expected_output (str): La nueva cadena esperada con las vocales invertidas.
        """
        assert self.solution.reverseVowels(input_str) == expected_output
