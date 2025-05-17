import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, groups, expected_output",
        [
            # Caso base simple: palabras alternan grupos, mismas longitudes, dist Hamming=1
            (
                ["abc", "abd", "aXd", "bXd"],
                [0, 1, 0, 1],
                ["abc", "abd", "aXd", "bXd"],
            ),

            # Caso con varias palabras, sólo algunas cumplen la condición de hamming=1 y grupos alternos
            (
                ["cat", "bat", "bet", "bed", "bad"],
                [0, 1, 0, 1, 0],
                ["cat", "bat", "bet", "bed"],
            ),

            # Caso sin palabras que cumplan hamming=1 con grupos alternos -> subsecuencia tamaño 1
            (
                ["hello", "world", "words"],
                [0, 1, 0],
                ["hello"],  # solo la primera palabra (por defecto)
            ),

            # Caso con varias longitudes distintas: sólo palabras con misma longitud se consideran
            (
                ["abc", "abcd", "abce", "abcf", "abcg"],
                [0, 1, 0, 1, 0],
                ["abc", "abce", "abcf"],  # subsecuencia válida de longitud 3
            ),

            # Caso con una única palabra
            (
                ["solo"],
                [0],
                ["solo"],
            ),

            # Caso vacío
            (
                [],
                [],
                [],
            ),

            # Caso donde hay una cadena larga de alternancia y cambio de un solo caracter
            (
                ["aaa", "aab", "abb", "bbb", "bbc", "bcc"],
                [0, 1, 0, 1, 0, 1],
                ["aaa", "aab", "abb", "bbb", "bbc", "bcc"],
            ),
        ]
    )
    def test_get_words_in_longest_subsequence(self, words, groups, expected_output):
        """
        Prueba parametrizada para validar distintos escenarios
        del método getWordsInLongestSubsequence.

        Args:
            words (List[str]): Lista de palabras.
            groups (List[int]): Lista de grupos.
            expected_output (List[str]): Subsecuencia más larga esperada.
        """
        assert self.solution.getWordsInLongestSubsequence(words, groups) == expected_output
