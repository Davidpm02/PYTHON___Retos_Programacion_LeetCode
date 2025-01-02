import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("Hello World", 5),                # Caso típico con dos palabras
            ("   fly me   to   the moon   ", 4),  # Palabra con espacios adicionales alrededor
            ("a", 1),                           # Cadena con una sola palabra
            ("", 0),                            # Cadena vacía
            ("I am learning Python", 6),        # Palabra larga en el final
            ("a b c d", 1),                    # Con varias palabras cortas
            ("test", 4),                        # Una palabra simple
            ("singlewordwithspacesend    ", 5),  # Solo al final con la palabra corta
            ("space before   ", 6),             # Espacios antes de la palabra
        ]
    )
    def test_length_of_last_word(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función lengthOfLastWord.

        Args:
            input_str (str): La cadena de texto para la prueba.
            expected_output (int): La longitud de la última palabra esperada.
        """
        assert self.solution.lengthOfLastWord(input_str) == expected_output
