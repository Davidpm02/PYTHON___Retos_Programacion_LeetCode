import pytest
from challenge import Solution  # Ajusta el nombre del archivo o el módulo según corresponda

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "paragraph, banned, expected_output",
        [
            # Caso clásico con palabras comunes y palabras prohibidas
            ("Bob hit a ball, the hit ball flew far.", ["hit"], "ball"),
            
            # Caso sin palabras prohibidas
            ("This is a simple test, a simple example.", [], "a"),
            
            # Caso donde la palabra prohibida es la más frecuente
            ("What a nice day, what a beautiful day.", ["what"], "a"),
            
            # Caso con varias palabras repetidas pero las prohibidas están presentes
            ("The quick brown fox jumps over the lazy dog.", ["the", "quick"], "fox"),
            
            # Caso con solo una palabra
            ("Single word repeated word word", ["repeated"], "word"),
            
            # Caso con un solo espacio o con palabras unidas
            ("! ! ! !", [], " "),
            
            # Caso con signos de puntuación y palabras repetidas
            ("Hello, hello! What a beautiful world.", ["world"], "hello"),
            
            # Caso con todas las palabras prohibidas en el párrafo
            ("I am here but I won't stay here.", ["i", "here"], "but")
        ]
    )
    def test_most_common_word(self, paragraph, banned, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función mostCommonWord.

        Args:
            paragraph (str): La cadena de texto que se procesará.
            banned (List[str]): Lista de palabras prohibidas.
            expected_output (str): La palabra más común, excluyendo las palabras prohibidas.
        """
        assert self.solution.mostCommonWord(paragraph, banned) == expected_output
