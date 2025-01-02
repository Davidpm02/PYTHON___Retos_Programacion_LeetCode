import pytest
from challenge import Solution  # Importamos la clase Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, goal, expected_output",
        [
            ("ab", "ba", True),        # Caso en el que intercambiar los caracteres nos da las dos cadenas iguales
            ("ab", "ab", False),       # Las cadenas son iguales pero no se puede formar una cadena con intercambio
            ("aaaaaaabc", "aaaaaaacb", True),  # Intercambio de dos caracteres para coincidir las cadenas
            ("", "", False),           # Cadenas vacías, no es posible hacer intercambio válido
            ("abc", "bca", False),     # No se pueden intercambiar solo dos caracteres y que coincidan las cadenas
            ("abcaa", "aacbb", False), # Número de caracteres diferentes más de dos
            ("abcd", "abcd", False),   # Cadenas iguales, no se pueden intercambiar caracteres, no se puede hacer buddy string
            ("abcde", "abcde", False), # Sin caracteres repetidos en las mismas posiciones
            ("aabbcc", "aabcbc", True),   # Un intercambio en cadenas con caracteres repetidos
            ("abcdefgh", "abcdgfhe", True), # Otro caso con más caracteres alternando
            ("fgh", "hfg", True)       # Tres caracteres en el caso de que uno de los caracteres repetidos con intercambio
        ]
    )
    def test_buddy_strings(self, s, goal, expected_output):
        """
        Prueba parametrizada para validar la función buddyStrings.

        Args:
            s (str): La primera cadena.
            goal (str): La segunda cadena.
            expected_output (bool): El resultado esperado para la validación de buddy strings.
        """
        assert self.solution.buddyStrings(s, goal) == expected_output
