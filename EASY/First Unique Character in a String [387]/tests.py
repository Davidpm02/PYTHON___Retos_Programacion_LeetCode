import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected_output",
        [
            ("leetcode", 0),                   # 'l' es el primer carácter único, índice 0
            ("loveleetcode", 2),               # 'v' es el primer carácter único, índice 2
            ("aabb", -1),                      # No hay caracteres únicos, retorna -1
            ("", -1),                          # Cadena vacía, no hay caracteres, retorna -1
            ("abcabc", -1),                    # Todos los caracteres están repetidos, retorna -1
            ("z", 0),                          # Única letra 'z', índice 0
            ("aabbccd", 6),                    # 'd' es el primer carácter único, índice 6
        ]
    )
    def test_first_uniq_char(self, s, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método firstUniqChar.

        Args:
            s (str): La cadena que se evaluará para encontrar el primer carácter único.
            expected_output (int): El índice esperado como resultado.
        """
        assert self.solution.firstUniqChar(s) == expected_output
