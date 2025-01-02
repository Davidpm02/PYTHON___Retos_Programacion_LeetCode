import pytest
from challenge import Solution 


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("abccccdd", 7),   # Caso típico con caracteres repetidos. Palíndromo más largo: "dccaccd"
            ("a", 1),           # Solo un carácter, el palíndromo es él mismo.
            ("bb", 2),          # Dos caracteres iguales forman un palíndromo: "bb"
            ("abc", 1),         # Cada carácter es único, la longitud de un palíndromo es 1.
            ("abccccdddcba", 11), # Secuencia con palíndromo con todos los caracteres adecuados.
            ("abcdd", 5),       # Palíndromo con múltiples caracteres.
            ("aabbcc", 6),      # Todos los caracteres tienen paridad, maximo palíndromo "aabbcc"
            ("xyzxyzxyzxyzxyz", 15),  # Muchos caracteres repetidos pero falta uno para completar el par
            ("abcabcabcabcabc", 9), # Todos los caracteres tienen paridad, maximo palíndromo "abcabcabc"
            ("", 0),            # Cadena vacía, no se puede formar ningún palíndromo.
            ("aaabbbccc", 5),    # Caso con múltiplos de caracteres, se puede formar "abcba"
            ("zxyzy", 5),        # Palíndromo exacto "zxyzy"
        ]
    )
    def test_longest_palindrome(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método longestPalindrome.

        Args:
            input_str (str): Cadena sobre la cual se probará la formación del palíndromo.
            expected_output (int): Longitud esperada del palíndromo más grande que se puede formar.
        """
        assert self.solution.longestPalindrome(input_str) == expected_output
