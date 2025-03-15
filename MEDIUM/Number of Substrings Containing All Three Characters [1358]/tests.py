import pytest
from challenge import Solution  # Importo la clase Solution desde el archivo del reto


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected_output",
        [
            ("abcabc", 10),    # Ejemplo con múltiples repeticiones de 'a', 'b' y 'c'
            ("aaabbbccc", 27), # Caso con grupos de caracteres en orden
            ("abc", 1),        # Caso mínimo con los tres caracteres
            ("aabbcc", 8),     # Caso con pares de caracteres
            ("ababab", 10),    # Alternancia de caracteres
            ("aaa", 0),        # Solo un tipo de carácter, sin subcadenas válidas
            ("", 0),           # Caso de cadena vacía
            ("abacbca", 15),   # Caso con distribución irregular de los caracteres
        ]
    )
    def test_number_of_substrings(self, s, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función numberOfSubstrings.

        Args:
            s (str): La cadena de entrada.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.numberOfSubstrings(s) == expected_output