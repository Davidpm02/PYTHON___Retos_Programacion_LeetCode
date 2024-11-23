import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_a, input_b, expected_output",
        [
            ("abc", "def", 3),       # Cadenas diferentes, ambas de longitud 3
            ("aaa", "aaa", -1),     # Cadenas iguales
            ("abcd", "ef", 4),      # Longitud mayor en 'a'
            ("xy", "uvwxyz", 6),    # Longitud mayor en 'b'
            ("", "a", 1),           # Una cadena vacía y otra no
            ("", "", -1),           # Ambas cadenas vacías
            ("longer", "short", 6), # 'a' es más larga que 'b'
            ("same", "same", -1),   # Ambas cadenas iguales
            ("unique", "uniq", 6),  # Una cadena más larga y diferente
            ("a", "aa", 2),         # Longitud mayor en 'b'
        ]
    )
    def test_find_lus_length(self, input_a, input_b, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findLUSlength.

        Args:
            input_a (str): Primera cadena de entrada.
            input_b (str): Segunda cadena de entrada.
            expected_output (int): Longitud esperada de la subsecuencia más larga.
        """
        assert self.solution.findLUSlength(input_a, input_b) == expected_output
