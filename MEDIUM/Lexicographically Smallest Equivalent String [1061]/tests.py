import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s1, s2, baseStr, expected_output",
        [
            ("abc", "cde", "eed", "aad"),              # Ejemplo básico con equivalencias cruzadas
            ("leetcode", "programs", "sourcecode", "aauaaaaada"),  # Caso con palabras más largas
            ("", "", "abc", "abc"),                     # Sin equivalencias, baseStr no cambia
            ("abc", "abc", "abc", "abc"),               # Equivalencias directas idénticas, resultado igual
            ("abc", "def", "fed", "abc"),               # Equivalencias que no afectan a baseStr
            ("abc", "bcd", "abcd", "aaaa"),             # Cadena base con varios reemplazos mínimos
            ("xyz", "abc", "xyz", "abc"),               # Reemplazos totales a mínimos
            ("az", "by", "abcxyz", "aaxxyz"),           # Mezcla de equivalencias parciales
            ("a", "z", "a", "a"),                        # Una equivalencia que no afecta la baseStr
            ("qwerty", "asdfgh", "poiuyt", "aoiuyt"),  # Caso aleatorio con sustituciones
        ]
    )
    def test_smallest_equivalent_string(self, s1, s2, baseStr, expected_output):
        """
        Prueba parametrizada para validar casos diferentes del método smallestEquivalentString.

        Args:
            s1 (str): Primera cadena de equivalencias.
            s2 (str): Segunda cadena de equivalencias.
            baseStr (str): Cadena base para la transformación.
            expected_output (str): Resultado esperado lexicográficamente mínimo.
        """
        assert self.solution.smallestEquivalentString(s1, s2, baseStr) == expected_output
