import pytest
from challenge import Solution  # Asegúrate de que el archivo se llama challenge.py y la clase Solution está definida allí.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            # Casos comunes con cadenas que contienen grupos grandes.
            ("abbxxxxzzy", [[3, 6]]),               # Un solo grupo grande: "xxxx"
            ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),  # Tres grupos grandes de diferentes longitudes.
            ("aabbcc", []),                        # No hay grupos grandes (todos tienen menos de 3 caracteres consecutivos).
            ("aaa", [[0, 2]]),                     # Un único grupo grande con toda la cadena: "aaa".
            ("", []),                              # Cadena vacía: no hay grupos grandes.
            ("aaaaa", [[0, 4]]),                   # Un grupo grande con toda la cadena: "aaaaa".
            ("abc", []),                           # Ningún grupo grande (todos son de longitud 1).
            ("aaabbbbcccccddd", [[0, 2], [3, 6], [7, 11]]),  # Varios grupos grandes de distintas longitudes.
        ]
    )
    def test_large_group_positions(self, input_str, expected_output):
        """
        Prueba parametrizada para validar la función largeGroupPositions.

        Args:
            input_str (str): La cadena de caracteres que se analizará.
            expected_output (List[List[int]]): El resultado esperado que indica los grupos grandes.
        """
        assert self.solution.largeGroupPositions(input_str) == expected_output
