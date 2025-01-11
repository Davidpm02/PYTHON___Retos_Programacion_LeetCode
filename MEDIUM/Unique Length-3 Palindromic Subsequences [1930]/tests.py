import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected_output",
        [
            ("aabca", 2),          # Palíndromos posibles: "a...a" y "bcb"
            ("abcba", 1),          # Un solo palíndromo "bcb"
            ("aaa", 1),            # Un palíndromo por todos los caracteres iguales
            ("abb", 1),            # Un solo palíndromo "b"
            ("aab", 0),            # No hay subcadenas de 3 caracteres que sean palíndromos
            ("zzabczz", 2),        # Palíndromos "zzz" y "zzz"
            ("abccba", 1),         # Palíndromo "bcb"
            ("abcd", 0),           # No hay subcadenas palindrómicas
            ("aabac", 1),          # Palíndromo "a...a"
            ("xaayz", 0),          # No hay subcadenas palindrómicas de longitud 3
            ("yzy", 1),            # Un solo palíndromo
            ("racecar", 2),        # Palíndromos "racecar" y "cec"
            ("xyzzyx", 2),         # Palíndromos "xyzzyx" y "yzzy"
        ]
    )
    def test_count_palindromic_subsequence(self, s, expected_output):
        """
        Prueba parametrizada para validar la función countPalindromicSubsequence.

        Args:
            s (str): La cadena a analizar para contar las subsecuencias palindrómicas de longitud 3.
            expected_output (int): El número de subsecuencias palindrómicas de longitud 3 esperadas.
        """
        assert self.solution.countPalindromicSubsequence(s) == expected_output
