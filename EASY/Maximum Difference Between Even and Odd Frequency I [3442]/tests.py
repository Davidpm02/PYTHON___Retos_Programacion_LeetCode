import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("aabbccd", 3),     # a:2, b:2, c:2, d:1 → odd:1 (d), even:2 (a/b/c) → 1-2 = -1 → max odd = 1, min even = 2 → 1-2=-1
            ("aaaabb", 4),      # a:4, b:2 → odd: ninguno, error evitado, test de comportamiento inválido
            ("aabbccdde", 3),   # a,b,c,d:2, e:1 → max odd:1, min even:2 → 1-2 = -1
            ("abcabcabcabc", 4),# a,b,c:4 → solo pares → no debería funcionar (IndexError esperado)
            ("aabbbcccc", 3),   # a:2, b:3, c:4 → odd=3 (b), even=2 (a) → 3-2 = 1
            ("aaabbbcccdddeee", 3),  # a,b,c,d,e:3 → sin pares → IndexError
            ("aabbccddeeffggh", 1),  # a..g:2, h:1 → max odd = 1, min even = 2 → 1-2 = -1
            ("zzzyyyxxxwwvvv", 3),  # z,y,x,w,v:3 → solo impares → IndexError
            ("aabbbbcccddee", 3),  # a:2, b:4, c:3, d,e:2 → max odd:3 (c), min even:2 (a/d/e) → 3-2 = 1
        ]
    )
    def test_max_difference(self, input_str, expected_output):
        """
        Valido el resultado devuelto por maxDifference con diversas combinaciones de repeticiones de caracteres.

        Args:
            input_str (str): Cadena de entrada.
            expected_output (int): Resultado esperado como la diferencia entre el mayor impar y menor par.
        """
        assert self.solution.maxDifference(input_str) == expected_output
