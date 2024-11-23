import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("hello world", "olleh dlrow"),              # Palabras normales invertidas
            ("Python is fun", "nohtyP si nuf"),          # Frase con palabras variadas
            ("a b c", "a b c"),                          # Palabras de un solo carácter
            ("racecar", "racecar"),                      # Palíndromo que permanece igual
            ("", ""),                                    # Cadena vacía
            (" ", ""),                                   # Espacios solamente (deben eliminarse)
            ("   hello   world   ", "olleh dlrow"),      # Espacios iniciales y finales, deben eliminarse
            ("reverse these words", "esrever eseht sdrow"),  # Frase con palabras más largas
        ]
    )
    def test_reverse_words(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función reverseWords.

        Args:
            input_str (str): Cadena de entrada con palabras a invertir.
            expected_output (str): Resultado esperado después de invertir las palabras.
        """
        assert self.solution.reverseWords(input_str) == expected_output
