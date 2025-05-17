import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "words, groups, expected_output",
        [
            # Caso básico: alternancia perfecta 0,1,0,1
            (
                ["a", "b", "c", "d"],
                [0, 1, 0, 1],
                ["a", "b", "c", "d"],
            ),

            # Caso sin alternancia: todos grupos iguales, se debe elegir solo una palabra
            (
                ["hello", "world", "foo"],
                [0, 0, 0],
                ["hello"],  # solo la primera palabra
            ),

            # Caso con alternancia interrumpida: debe saltar para mantener alternancia
            (
                ["apple", "banana", "cherry", "date"],
                [0, 0, 1, 1],
                ["apple", "cherry"],
            ),

            # Caso donde alternancia máxima es 3 elementos
            (
                ["one", "two", "three", "four", "five"],
                [1, 0, 1, 1, 0],
                ["one", "two", "three", "five"],
            ),

            # Caso con alternancia mínima, secuencia de longitud 1
            (
                ["x"],
                [0],
                ["x"],
            ),

            # Caso vacío: no hay palabras
            (
                [],
                [],
                [],
            ),

            # Caso con alternancia 0 y 1 repetida de forma irregular
            (
                ["a", "b", "c", "d", "e"],
                [0, 1, 1, 0, 1],
                ["a", "b", "d", "e"],
            ),
        ]
    )
    def test_get_longest_subsequence(self, words, groups, expected_output):
        """
        Prueba parametrizada para validar distintos escenarios
        del método getLongestSubsequence.

        Args:
            words (List[str]): Lista de palabras.
            groups (List[int]): Lista de grupos asociados a cada palabra.
            expected_output (List[str]): Subsecuencia más larga esperada.
        """
        assert self.solution.getLongestSubsequence(words, groups) == expected_output
