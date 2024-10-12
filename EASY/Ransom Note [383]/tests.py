import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "ransomNote, magazine, expected_output",
        [
            ("a", "b", False),                # No se puede construir 'a' con 'b'
            ("aa", "ab", False),              # No se puede construir 'aa' con 'ab'
            ("aa", "aab", True),              # 'aa' se puede construir con 'aab'
            ("", "anything", True),           # Una cadena vacía siempre se puede construir
            ("abc", "defg", False),           # 'abc' no se puede construir con 'defg'
            ("abc", "cba", True),             # 'abc' se puede construir con 'cba'
            ("abcdef", "fedcba", True),       # 'abcdef' se puede construir con 'fedcba'
            ("aabbcc", "abccbaab", True),     # 'aabbcc' se puede construir con 'abccbaab'
            ("longnote", "shortmagazine", False), # 'longnote' no se puede construir con 'shortmagazine'
            ("xxy", "yxxxy", True),           # 'xxy' se puede construir con 'yxxxy'
        ]
    )
    def test_can_construct(self, ransomNote, magazine, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método canConstruct.

        Args:
            ransomNote (str): La cadena que queremos formar.
            magazine (str): La cadena con los caracteres disponibles.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.canConstruct(ransomNote, magazine) == expected_output
