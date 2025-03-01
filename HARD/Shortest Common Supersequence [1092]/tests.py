import pytest
from challenge import Solution  # Importo la clase Solution desde el archivo challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "str1, str2, expected_output",
        [
            ("abac", "cab", "cabac"),            # Caso con cadenas que se superponen parcialmente
            ("abc", "abc", "abc"),              # Caso donde las cadenas son iguales
            ("abc", "def", "abcdef"),           # Caso donde las cadenas no tienen caracteres comunes
            ("abc", "ab", "abc"),               # Caso donde una cadena es prefijo de la otra
            ("", "abc", "abc"),                 # Caso donde una cadena está vacía
            ("abc", "", "abc"),                 # Caso donde una cadena está vacía
            ("ace", "abc", "acebc"),            # Caso con caracteres comunes intercalados
            ("a", "b", "ab"),                   # Caso con una sola letra diferente
            ("pqr", "xyz", "pqrxyz"),           # Caso con ninguna letra en común
            ("x", "x", "x"),                    # Caso con una sola letra igual
            ("abcdefgh", "acefh", "abcdefgh")  # Caso con algunos caracteres comunes dispersos
        ]
    )
    def test_shortestCommonSupersequence(self, str1, str2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función shortestCommonSupersequence.

        Args:
            str1 (str): La primera cadena que se probará.
            str2 (str): La segunda cadena que se probará.
            expected_output (str): El resultado esperado para la supersecuencia común más corta.
        """
        assert self.solution.shortestCommonSupersequence(str1, str2) == expected_output
