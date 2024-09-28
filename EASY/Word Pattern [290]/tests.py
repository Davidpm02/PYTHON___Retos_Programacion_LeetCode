import pytest
from challenge import Solution  # Se asume que el archivo del reto se llama challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "pattern, s, expected_output",
        [
            ("abba", "dog cat cat dog", True),                # El patrón se respeta
            ("abba", "dog cat cat fish", False),              # El patrón no se respeta
            ("aaaa", "dog cat cat dog", False),               # Los mismos caracteres, pero palabras diferentes
            ("abba", "dog dog dog dog", False),               # Palabras repetidas no coinciden con el patrón
            ("", "", True),                                   # Patrón y cadena vacía coinciden
            ("a", "hello", True),                             # Patrón de un solo carácter
            ("abc", "a b c", True),                           # Cada letra del patrón mapea a una palabra única
            ("abc", "a b a", False),                          # Una letra en el patrón mapea a dos palabras diferentes
            ("aabb", "red blue blue red", True),             # El patrón se respeta
            ("aabb", "red blue blue green", False),          # El patrón no se respeta
        ]
    )
    def test_word_pattern(self, pattern, s, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función wordPattern.

        Args:
            pattern (str): El patrón que se evaluará.
            s (str): La cadena de texto que se evaluará.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.wordPattern(pattern, s) == expected_output
