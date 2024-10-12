import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, t, expected_output",
        [
            ("abcd", "abcde", "e"),            # Caso simple con un carácter adicional 'e'
            ("", "y", "y"),                    # Caso donde s es una cadena vacía y t tiene un solo carácter
            ("a", "aa", "a"),                  # Caso donde el carácter adicional es el mismo que ya estaba en la cadena
            ("abc", "cbad", "d"),              # Caso con caracteres en diferentes órdenes y un carácter adicional
            ("abc", "abcd", "d"),              # Otro caso simple con un carácter adicional
            ("xyz", "xyzx", "x"),              # Caso con repetición de caracteres
        ]
    )
    def test_find_the_difference(self, s, t, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método findTheDifference.

        Args:
            s (str): La cadena base sin el carácter adicional.
            t (str): La cadena con el carácter adicional.
            expected_output (str): El carácter esperado como resultado.
        """
        assert self.solution.findTheDifference(s, t) == expected_output
