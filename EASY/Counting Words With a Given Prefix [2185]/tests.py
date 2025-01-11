import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, pref, expected_output",
        [
            (["apple", "applause", "appetizer", "banana"], "app", 3),  # Tres palabras comienzan con "app"
            (["grape", "green", "banana"], "gr", 2),  # "grape" y "green" comienzan con "gr"
            (["cat", "cattle", "car", "dog"], "ca", 3),  # "cat", "cattle" y "car" comienzan con "ca"
            (["dog", "dot", "dove"], "do", 3),   # Todas las palabras comienzan con "do"
            (["hello", "world", "hero"], "he", 2),  # "hello" y "hero" comienzan con "he"
            (["cow", "cat", "dog", "hen"], "ho", 0),  # Ninguna palabra comienza con "ho"
            (["cat", "bat", "rat", "mat"], "ma", 1),  # Solo "mat" comienza con "ma"
            ([], "no", 0),   # Caso con lista vacía
            (["pencil", "pen", "page"], "pen", 1),  # Solo "pen" comienza con "pen"
            (["television", "telephone", "test"], "te", 3)  # Todas las palabras comienzan con "te"
        ]
    )
    def test_prefix_count(self, words, pref, expected_output):
        """
        Prueba parametrizada para validar la función prefixCount.

        Args:
            words (List[str]): Lista de palabras a verificar.
            pref (str): El prefijo a buscar en las palabras.
            expected_output (int): El número esperado de palabras que contienen el prefijo.
        """
        assert self.solution.prefixCount(words, pref) == expected_output
