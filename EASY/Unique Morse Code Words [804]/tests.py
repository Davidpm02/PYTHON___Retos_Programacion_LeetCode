import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution

class TestSolution:

    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_words, expected_output",
        [
            (["gin", "zen", "gig", "msg"], 2),  # Dos representaciones únicas en morse
            (["a", "b", "c", "d", "e"], 5),     # Cinco representaciones únicas (cada letra es diferente)
            (["a", "a", "a"], 1),               # Solo una representación porque todas son iguales
            (["hello", "world", "python"], 3),  # Tres palabras con representaciones diferentes
            (["sos", "sos", "sos"], 1),         # Tres veces la misma palabra "sos" (una sola representación)
            (["code", "words", "morse"], 3),    # Tres palabras con transformaciones únicas
            (["abc", "acb", "bca"], 1),         # Tres permutaciones de letras con la misma representación morse
            ([], 0),                           # Lista vacía, debe devolver 0
            ([""], 1)                          # Lista con una cadena vacía, la transformación es única
        ]
    )
    def test_unique_morse_representations(self, input_words, expected_output):
        """
        Prueba parametrizada para validar la función uniqueMorseRepresentations.

        Args:
            input_words (List[str]): Lista de palabras a transformar.
            expected_output (int): Número esperado de representaciones morse únicas.
        """
        assert self.solution.uniqueMorseRepresentations(input_words) == expected_output
