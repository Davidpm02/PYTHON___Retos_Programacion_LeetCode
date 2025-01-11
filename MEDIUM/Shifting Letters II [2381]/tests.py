import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, shifts, expected_output",
        [
            ("abcdef", [[0, 2, 1], [2, 4, 0]], "azcdef"),     # Desplazamientos hacia la derecha en posiciones 0-2, 2-4
            ("xyz", [[0, 2, 0]], "vwx"),                      # Desplazamiento hacia la izquierda en toda la cadena
            ("abc", [[0, 1, 1], [1, 2, 0]], "acc"),            # Desplazamientos de carácter 0-1 hacia la derecha y 1-2 hacia la izquierda
            ("hello", [[0, 2, 1], [3, 4, 0]], "izllm"),        # Varios desplazamientos en diferentes partes de la cadena
            ("testing", [[0, 1, 1], [1, 3, 0], [4, 6, 1]], "ufsfubk"),  # Desplazamientos múltiples con mezcla de direcciones
            ("abcxyz", [[1, 4, 0], [3, 5, 1]], "zffybc"),      # Varias posiciones de desplazamiento con ambas direcciones
            ("openai", [[0, 1, 1], [2, 3, 0]], "obnfai"),      # Combinación de desplazamientos hacia la derecha e izquierda
            ("abcd", [[1, 2, 1]], "azcd"),                   # Desplazamiento en subcadena
            ("aeiou", [[0, 4, 0]], "zdozv"),                 # Desplazamiento hacia la izquierda de toda la cadena
            ("zxy", [[0, 0, 1]], "axy"),                    # Un solo carácter desplazado hacia la derecha
            ("abc", [[0, 2, 1]], "abc"),                    # No desplazamiento
        ]
    )
    def test_shifting_letters(self, s, shifts, expected_output):
        """
        Prueba parametrizada para validar la función shiftingLetters.

        Args:
            s (str): Cadena inicial a modificar con desplazamientos.
            shifts (List[List[int]]): Lista de desplazamientos a realizar.
            expected_output (str): Resultado esperado luego de aplicar los desplazamientos.
        """
        assert self.solution.shiftingLetters(s, shifts) == expected_output
