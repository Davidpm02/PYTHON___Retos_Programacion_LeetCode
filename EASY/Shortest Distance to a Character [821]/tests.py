import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution desde el reto.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, c, expected_output",
        [
            ("abcabc", "b", [1, 0, 1, 1, 0, 1]),    # Distancias a 'b' en una cadena repetida
            ("hello", "l", [2, 1, 0, 1, 2]),          # Caso con letras repetidas
            ("distance", "e", [3, 2, 1, 0, 1, 2, 3, 4, 5]), # Distancias a 'e' en la palabra 'distance'
            ("openai", "o", [0, 1, 2, 1, 0, 1, 2]),   # Distancias a 'o' en "openai"
            ("hello world", "o", [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0]),  # Distancias a 'o' en un espacio
            ("", "z", []),                            # Cadena vacía, sin elementos
            ("abcd", "a", [0, 1, 2, 3]),              # Distancias a 'a' cuando 'a' está al principio
            ("abcdefgh", "h", [7, 6, 5, 4, 3, 2, 1, 0]), # Distancias a 'h' cuando 'h' está al final
            ("banana", "n", [1, 0, 1, 0, 1, 0]),      # Distancias a 'n' en "banana"
            ("abcdabcd", "c", [2, 1, 0, 1, 2, 1, 0, 1]),  # Distancias a 'c' en "abcdabcd"
        ]
    )
    def test_shortest_to_char(self, s, c, expected_output):
        """
        Prueba parametrizada para validar la función shortestToChar.

        Args:
            s (str): La cadena sobre la que se calcularán las distancias.
            c (str): El carácter para el cual calcularemos las distancias.
            expected_output (List[int]): La lista de distancias esperadas.
        """
        result = self.solution.shortestToChar(s, c)
        assert result == expected_output
