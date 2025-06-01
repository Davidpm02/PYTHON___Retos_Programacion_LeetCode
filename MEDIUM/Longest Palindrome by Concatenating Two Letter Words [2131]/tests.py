import pytest
from challenge import Solution  # Importo la clase Solution desde el módulo challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, expected_output",
        [
            (["ab", "ba"], 4),                  # Dos palabras reversas forman un palíndromo de 4 caracteres
            (["aa", "aa", "bb", "bb"], 8),     # Pares de palíndromos "aa" y "bb" suman 8 caracteres
            (["aa", "bb", "cc"], 2),            # Solo un palíndromo central (2 caracteres)
            (["ab", "ty", "yt", "lc", "cl", "ab"], 8), # Varias parejas reversas y palabra extra
            (["cc", "ll", "xx", "cc", "ll", "xx"], 12), # Pares múltiples de palíndromos
            ([], 0),                           # Lista vacía no forma palíndromo
            (["aa"], 2),                      # Un solo palíndromo, puede ser centro
            (["ab"], 0),                      # Palabra sin reverso, no contribuye
            (["ab", "ba", "aa", "aa", "cc"], 8),  # Combinación de reversos y palíndromos con centro
            (["aa", "bb", "aa", "bb", "aa"], 10),  # Uso de centro con múltiples pares
        ]
    )
    def test_longestPalindrome(self, words, expected_output):
        """
        Valido distintos casos para la función longestPalindrome, incluyendo:

        - Pares de palabras reversas.
        - Palíndromos usados como centro.
        - Combinaciones mixtas.
        - Casos borde como listas vacías o con una sola palabra.
        """
        assert self.solution.longestPalindrome(words) == expected_output
