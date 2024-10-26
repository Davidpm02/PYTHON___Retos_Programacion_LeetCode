import pytest
from challenge import Solution  # Importamos la clase Solution para acceder al método a probar


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("Hello, my name is John", 5),                # Caso típico con múltiples palabras
            ("   Hello   world  ", 2),                    # Caso con espacios múltiples en los extremos y entre palabras
            ("Hello", 1),                                 # Caso con una sola palabra
            ("", 0),                                      # Cadena vacía, sin segmentos
            ("      ", 0),                                # Cadena solo con espacios, sin segmentos
            ("Hello, world!", 2),                         # Dos segmentos separados por caracteres especiales
            ("This is a test string.", 5),                # Caso con una cadena típica de prueba
            ("      SingleWord       ", 1),               # Caso de una palabra rodeada de espacios
            ("Another  example     here   ", 3),          # Caso con palabras rodeadas por espacios múltiples
            ("One two three   four", 4),                  # Palabras con múltiples espacios intercalados al final
        ]
    )
    def test_count_segments(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método countSegments.

        Args:
            input_str (str): La cadena de texto en la que se cuentan los segmentos.
            expected_output (int): El número esperado de segmentos.
        """
        assert self.solution.countSegments(input_str) == expected_output
