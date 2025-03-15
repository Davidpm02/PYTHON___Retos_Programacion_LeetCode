import pytest
from challenge import Solution  # Importo la clase Solution desde el archivo del reto


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "word, k, expected_output",
        [
            ("aeioubcdef", 2, 3),  # Caso con todas las vocales y consonantes distribuidas
            ("aeiouxyz", 1, 3),   # Caso con consonantes separadas
            ("aeioubc", 3, 0),    # Caso sin suficientes consonantes para formar subcadenas
            ("abcdeiou", 2, 4),   # Caso con consonantes entre vocales
            ("aeiouaeiou", 0, 10), # Solo vocales, sin consonantes
            ("bcdfgh", 2, 0),     # Solo consonantes, sin vocales
            ("aeiou", 1, 0),      # Solo vocales, sin consonantes para contar
            ("aeioubcdfgh", 3, 6), # Mezcla de vocales y consonantes con diferentes distribuciones
        ]
    )
    def test_count_of_substrings(self, word, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countOfSubstrings.

        Args:
            word (str): La cadena de entrada.
            k (int): Número exacto de consonantes requeridas en la subcadena.
            expected_output (int): El número esperado de subcadenas válidas.
        """
        assert self.solution.countOfSubstrings(word, k) == expected_output
