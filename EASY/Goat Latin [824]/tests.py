import pytest
from challenge import Solution  # Ajusta este import si el nombre del archivo es diferente.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "sentence, expected_output",
        [
            ("I speak Goat Latin", "Imaa speakma aa Goatma aaa Latinma aaaa"),         # Ejemplo general
            ("The quick brown fox", "heTma uickqma ownbrma oxfma aaa"),                # Empieza con consonante
            ("A apple a a", "Amaa applema aaaa amaaaa"),                               # Palabra que comienza con vocal
            ("hello world", "ellohma orldwma aaa"),                                      # Palabras con consonantes
            ("i am excited", "imaa amma aa excitedma aaa"),                            # Consonantes y vocales combinados
            ("", "")                                                                   # Cadena vacía
        ]
    )
    def test_toGoatLatin(self, sentence, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función toGoatLatin.

        Args:
            sentence (str): La oración que se convertirá en Goat Latin.
            expected_output (str): El resultado esperado tras la conversión a Goat Latin.
        """
        assert self.solution.toGoatLatin(sentence) == expected_output
