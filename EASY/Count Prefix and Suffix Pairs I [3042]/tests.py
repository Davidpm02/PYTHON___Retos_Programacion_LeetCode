import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, expected_output",
        [
            (["abc", "ab", "cab", "bc"], 1),        # "ab" es prefijo y sufijo de "abc"
            (["hello", "hell", "hellworld", "world"], 2),  # "hell" es prefijo y sufijo de "hello" y "world"
            (["hello", "ell", "ellword", "world"], 1),  # "ell" es prefijo y sufijo de "ellword"
            (["abc", "def", "ghi"], 0),            # Ninguna palabra es prefijo y sufijo de otra
            (["cat", "catalog", "catal", "dog"], 3), # "cat" es prefijo y sufijo de "catalog", "catal" y "catal" en sí mismo
            (["sun", "sung", "king", "sund"], 1),    # "sun" es prefijo y sufijo de "sung"
            (["track", "cracker", "trac", "crack"], 1),  # "track" es prefijo y sufijo de "cracker"
            (["letter", "er", "letterer", "etter"], 3), # "er" es prefijo y sufijo de "letterer" y "letter"
            (["go", "go", "go", "go"], 6),          # "go" es prefijo y sufijo de todos
            (["alphabet", "alpha", "bet", "bete"], 1),  # "alpha" es prefijo y sufijo de "alphabet"
            ([], 0),                               # Caso donde la lista está vacía
        ]
    )
    def test_count_prefix_suffix_pairs(self, words, expected_output):
        """
        Prueba parametrizada para validar la función countPrefixSuffixPairs.

        Args:
            words (List[str]): Lista de cadenas en las que se buscarán prefijos y sufijos.
            expected_output (int): El resultado esperado, que es la cantidad de parejas de palabras 
                                   donde una es prefijo y sufijo de la otra.
        """
        assert self.solution.countPrefixSuffixPairs(words) == expected_output
