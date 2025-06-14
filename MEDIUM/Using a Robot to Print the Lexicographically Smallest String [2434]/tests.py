import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("zza", "azz"),               # Caso simple con repetidos y orden lex pequeño
            ("bac", "abc"),               # Ordenar lexicográficamente a partir del método
            ("bdda", "addb"),             # Cadena con repetidos y orden mixto
            ("leetcode", "cdelotee"),     # Caso más largo con letras variadas
            ("a", "a"),                   # Caso base: una letra
            ("", ""),                     # Caso base: cadena vacía
            ("cba", "abc"),               # Orden inverso para validar correcto orden
            ("azbycx", "abcxyz"),         # Cadena con alternancia de letras
            ("ababab", "aaabbb"),         # Repetidos alternos
            ("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz"),  # Reversa total
        ]
    )
    def test_robot_with_string(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función robotWithString.

        Args:
            input_str (str): La cadena de entrada.
            expected_output (str): El resultado esperado lexicográficamente mínimo.
        """
        assert self.solution.robotWithString(input_str) == expected_output
