import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words1, words2, expected_output",
        [
            (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"], ["facebook", "google"]),  # Ejemplo con palabras que cumplen las condiciones
            (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"], ["apple", "google", "leetcode"]),  # Palabras que contienen las letras "l" y "e"
            (["amazon", "apple", "facebook", "google", "leetcode"], ["x", "z"], []),  # No hay palabras que contengan las letras "x" y "z"
            (["alibaba", "baidu", "tencent", "alipay"], ["a", "b", "i"], ["alibaba", "baidu", "alipay"]),  # Algunas palabras cumplen las condiciones
            (["bob", "ben", "beer", "ban", "but"], ["b", "e"], ["bob", "beer", "ben", "ban", "but"]),  # Palabras con "b" y "e"
            (["start", "stare", "staring"], ["s", "t", "r"], ["start", "stare", "staring"]),  # Palabras con "s", "t" y "r"
            (["zoom", "zoo", "sonic", "opera", "op"], ["o", "e"], ["zoom", "zoo", "sonic", "opera", "op"]),  # Palabras con "o" y "e"
            ([], ["e", "o"], []),  # Caso vacío de 'words1'
            (["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"]),  # Palabras simples que cumplen la condición exacta
            (["abcdefg", "xyz"], ["a", "c"], ["abcdefg"]),  # Un caso donde una palabra cumple con "a" y "c"
        ]
    )
    def test_word_subsets(self, words1, words2, expected_output):
        """
        Prueba parametrizada para validar la función wordSubsets.

        Args:
            words1 (List[str]): La lista de palabras en las que vamos a buscar las subcadenas.
            words2 (List[str]): La lista de palabras que deben cumplirse como subcadenas de las palabras en 'words1'.
            expected_output (List[str]): El resultado esperado de las palabras de 'words1' que cumplen la condición.
        """
        assert self.solution.w
