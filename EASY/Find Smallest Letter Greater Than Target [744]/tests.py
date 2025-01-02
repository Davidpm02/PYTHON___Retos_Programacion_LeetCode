import pytest
from challenge import Solution  # Ajusta el nombre del archivo si es necesario.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "letters, target, expected_output",
        [
            (['a', 'b', 'c', 'd'], 'b', 'c'),       # La siguiente letra después de 'b' es 'c'
            (['a', 'c', 'f', 'j'], 'a', 'c'),       # La siguiente letra después de 'a' es 'c'
            (['a', 'd', 'g', 'y'], 'f', 'g'),       # La siguiente letra después de 'f' es 'g'
            (['a', 'b', 'c', 'd', 'e'], 'e', 'a'),  # El target es la última, por lo que la siguiente es 'a'
            (['a', 'b', 'c'], 'z', 'a'),           # 'z' es la última, por lo que la siguiente es 'a'
            (['x', 'y', 'z'], 'z', 'x'),           # Si el target es 'z', el siguiente es 'x' por ser circular
            (['a', 'b', 'c'], 'd', 'a'),           # 'd' no está, por lo que el siguiente es 'a'
            (['a', 'b', 'c'], 'a', 'b'),           # La siguiente letra después de 'a' es 'b'
            (['z', 'z', 'z'], 'y', 'z'),           # Todas las letras son 'z', el siguiente es también 'z'
        ]
    )
    def test_nextGreatestLetter(self, letters, target, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función nextGreatestLetter.

        Args:
            letters (List[str]): La lista de letras sobre la que se realizará la búsqueda.
            target (str): La letra que se comparará para hallar la siguiente mayor.
            expected_output (str): El resultado esperado, que es la primera letra mayor que 'target'.
        """
        assert self.solution.nextGreatestLetter(letters, target) == expected_output
