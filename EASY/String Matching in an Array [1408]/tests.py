import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, expected_output",
        [
            (["mass", "as", "hero", "superhero"], ["as"]),                # "as" es subcadena de "mass"
            (["leetcoder", "leetcode", "od", "ham", "ram"], ["od"]),      # "od" es subcadena de "leetcoder" y "od"
            (["blue", "green", "bu"], ["bu"]),                            # "bu" es subcadena de "blue"
            (["bananas", "apple", "pencil", "ana"], ["ana"]),             # "ana" es subcadena de "bananas"
            (["hello", "world", "hell"], ["hell"]),                       # "hell" es subcadena de "hello"
            (["test", "case", "set"], ["set"]),                           # "set" es subcadena de "test" y "case"
            (["javascript", "script", "java", "type"], ["java", "script"]) # "java" es subcadena de "javascript", y "script" es subcadena de "javascript"
        ]
    )
    def test_string_matching(self, words, expected_output):
        """
        Prueba parametrizada para validar la función stringMatching.

        Args:
            words (List[str]): Lista de palabras.
            expected_output (List[str]): Las palabras que son subcadenas de otras en la lista.
        """
        assert sorted(self.solution.stringMatching(words)) == sorted(expected_output)
