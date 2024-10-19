import pytest
from challenge import Solution  # Asumo que el código original está en el archivo challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, t, expected_output",
        [
            ("abc", "ahbgdc", True),      # Caso típico: subsecuencia válida
            ("axc", "ahbgdc", False),     # Caso típico: no es una subsecuencia válida
            ("", "ahbgdc", True),         # Una cadena vacía es siempre una subsecuencia válida
            ("abc", "", False),           # Una cadena no vacía no puede ser subsecuencia de una cadena vacía
            ("abc", "abc", True),         # Subcadena exacta
            ("ace", "abcde", True),       # Saltando caracteres
            ("aec", "abcde", False),      # Orden incorrecto
            ("longsubsequence", "longlonglongsubsequence", True),  # Subsequencia repetida varias veces en t
        ]
    )
    def test_is_subsequence(self, s, t, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función isSubsequence.

        Args:
            s (str): La cadena que se verificará como subsecuencia.
            t (str): La cadena original en la que se buscará la subsecuencia.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.isSubsequence(s, t) == expected_output
