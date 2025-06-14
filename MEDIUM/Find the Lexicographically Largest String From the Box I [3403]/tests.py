import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "word, numFriends, expected_output",
        [
            ("abcde", 1, "abcde"),               # Un solo amigo, debe devolver la cadena completa
            ("abcde", 2, "bcde"),                # Dividir en 2 partes, mayor lexicográficamente
            ("abcde", 3, "cde"),                 # División en 3 subcadenas
            ("abcde", 5, "e"),                   # Cada amigo recibe 1 caracter
            ("abcde", 6, ""),                    # Más amigos que letras, no hay división válida, espera cadena vacía
            ("zzzzzz", 3, "zzz"),                # Todos caracteres iguales
            ("azbycx", 2, "zbycx"),              # Mezcla de letras, elegir subcadena más grande lex
            ("a", 1, "a"),                      # Caso mínimo, un solo carácter y un amigo
            ("a", 2, ""),                       # Más amigos que caracteres, resultado vacio
            ("abcdefg", 4, "defg"),              # Caso general con 4 amigos
        ]
    )
    def test_answer_string(self, word, numFriends, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método answerString.

        Args:
            word (str): Cadena original.
            numFriends (int): Número de subcadenas en que se divide.
            expected_output (str): La subcadena lexicográficamente mayor esperada.
        """
        assert self.solution.answerString(word, numFriends) == expected_output
