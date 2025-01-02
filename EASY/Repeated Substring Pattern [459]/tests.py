import pytest
from challenge import Solution  # Asegúrate de que el archivo se llame challenge.py y la clase Solution esté definida allí.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected_output",
        [
            # Casos en los que la cadena puede ser formada con una subcadena repetida
            ("abab", True),                      # "ab" repetida dos veces
            ("abcabcabcabc", True),              # "abc" repetida cuatro veces
            ("aaaa", True),                      # "a" repetida cuatro veces
            ("ababab", True),                    # "ab" repetida tres veces
            ("abababab", True),                  # "ab" repetida cuatro veces

            # Casos en los que no se puede formar la cadena con subcadena repetida
            ("abc", False),                      # No hay ninguna subcadena que se repita para formar "abc"
            ("abca", False),                     # "a", "b", "c" y "a" no se repiten en la secuencia completa
            ("abcdef", False),                   # No hay ninguna subcadena que se repita para formar "abcdef"

            # Casos con una longitud de cadena pequeña
            ("a", False),                        # Solo una letra no puede tener una subcadena repetida
            ("aa", True),                        # "a" repetida dos veces
            ("abcabcabc", True),                 # "abc" repetida tres veces
        ]
    )
    def test_repeatedSubstringPattern(self, s, expected_output):
        """
        Prueba parametrizada para validar si una cadena puede ser formada a partir
        de la repetición de una subcadena.

        Args:
            s (str): Cadena a verificar.
            expected_output (bool): Resultado esperado (True o False).
        """
        assert self.solution.repeatedSubstringPattern(s) == expected_output
