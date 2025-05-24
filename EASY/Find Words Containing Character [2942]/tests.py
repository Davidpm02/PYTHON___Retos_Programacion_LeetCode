import pytest
from challenge import Solution  # Asumo que el código está en challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution para ejecutar los tests."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, x, expected_output",
        [
            (["hello", "world", "python", "code"], "o", [0, 1, 2]),  # 'o' aparece en "hello", "world", "python"
            (["apple", "banana", "cherry"], "a", [0, 1]),           # 'a' aparece en "apple", "banana"
            (["test", "testing", "tested"], "z", []),                # 'z' no aparece en ninguna palabra
            ([], "a", []),                                            # lista vacía de palabras
            (["repeat", "repeat", "repeat"], "e", [0, 1, 2]),        # todas contienen 'e'
            (["case", "Case", "CASE"], "C", [1, 2]),                 # 'C' mayúscula aparece en 1 y 2
            (["mix", "match", "max"], "m", [0, 1, 2]),               # 'm' aparece en todos
            (["single"], "s", [0]),                                   # 's' aparece en "single"
            ([""], "a", []),                                          # palabra vacía, ningún carácter
        ]
    )
    def test_findWordsContaining(self, words, x, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método findWordsContaining.

        Args:
            words (List[str]): Lista de palabras a evaluar.
            x (str): Carácter a buscar dentro de las palabras.
            expected_output (List[int]): Índices esperados de palabras que contienen el carácter.
        """
        assert self.solution.findWordsContaining(words, x) == expected_output
