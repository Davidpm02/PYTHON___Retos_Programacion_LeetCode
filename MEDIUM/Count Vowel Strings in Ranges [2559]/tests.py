import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, queries, expected_output",
        [
            (["apple", "orange", "banana", "umbrella"], [[0, 2], [1, 3], [0, 3]], [2, 2, 3]),    # Caso con varios elementos
            (["apple", "orange", "banana"], [[0, 1], [1, 2]], [1, 2]),                            # Consulta con sublistas pequeñas
            (["a", "e", "i", "o", "u"], [[0, 4]], [5]),                                               # Todos los elementos son válidos
            (["ab", "ei", "aia"], [[0, 2]], [2]),                                                  # Un caso con subcadenas que inician y finalizan con vocales
            (["cat", "dog", "ear", "ate", "up"], [[0, 4], [1, 2]], [2, 1]),                         # Prueba con varios casos de no validas
            (["tea", "ome", "ape", "iqo"], [[1, 3], [0, 2]], [3, 2]),                             # Caso con palabras que empiezan y terminan con vocales
            ([], [[0, 0]], [0]),                                                                  # Lista vacía
            (["apple", "orange", "banana"], [[2, 2]], [0])                                         # Solo una cadena que no cumple con los requisitos
        ]
    )
    def test_vowel_strings(self, words, queries, expected_output):
        """
        Prueba parametrizada para validar la función vowelStrings.

        Args:
            words (List[str]): Lista de palabras a verificar.
            queries (List[List[int]]): Lista de consultas con rangos de índices.
            expected_output (List[int]): Resultado esperado para cada consulta.
        """
        assert self.solution.vowelStrings(words, queries) == expected_output
