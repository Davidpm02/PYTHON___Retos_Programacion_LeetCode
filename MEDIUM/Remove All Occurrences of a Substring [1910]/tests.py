import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, part, expected_output",
        [
            ("axxxxyxxxa", "xx", "aaxa"),               # Eliminar todas las ocurrencias de "xx"
            ("abcdef", "z", "abcdef"),                   # No hay ocurrencias de "z", la cadena permanece igual
            ("hellohellohello", "hello", ""),            # Eliminar todas las ocurrencias de "hello"
            ("aaaaa", "a", ""),                          # Eliminar todas las ocurrencias de "a"
            ("abcdef", "bc", "adef"),                    # Eliminar la ocurrencia "bc"
            ("abcabcabc", "abc", ""),                    # Eliminar todas las ocurrencias de "abc"
            ("aabbcc", "b", "aac"),                      # Eliminar todas las ocurrencias de "b"
            ("aaaabaaa", "aa", "ab"),                    # Eliminar todas las ocurrencias de "aa"
        ]
    )
    def test_remove_occurrences(self, s, part, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función removeOccurrences.

        Args:
            s (str): La cadena original donde se eliminan las ocurrencias.
            part (str): La subcadena que debe ser eliminada.
            expected_output (str): El resultado esperado después de las eliminaciones.
        """
        assert self.solution.removeOccurrences(s, part) == expected_output
