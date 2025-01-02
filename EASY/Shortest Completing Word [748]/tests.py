import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "licensePlate, words, expected_output",
        [
            ("1s3 PSt", ["step", "steps", "stripe", "stepple"], "steps"),  # Ejemplo de caso con espacios y números en la placa
            ("", ["hello", "world", "apple"], "hello"),                     # Caso vacío en 'licensePlate'
            ("Ah616", ["hello", "hey", "he", "howdy", "hurrah"], "howdy"),  # Contando todas las letras en 'licensePlate' ignorando números
            ("abc", ["ab", "ac", "abc", "abcd"], "abc"),                    # Caso con letras repetidas
            ("abc", ["ax", "by", "cz"], "ax"),                              # Caso con palabras que no completan todas las letras
            ("Le Ts", ["let", "best", "sets"], "sets"),                     # Palabra completa con caracteres mezclados en mayúsculas y minúsculas
            ("xy1", ["xy", "xyz", "abcd"], "xyz"),                          # Caso con letras al final
            ("xyz", ["xyz", "xxyz", "zzzxy", "zzxy"], "xyz"),               # Caso con varias posibles opciones
            ("abcD", ["abcd", "ab", "adbc", "Dabc", "dbca"], "abcd"),      # Caso con letras y mayúsculas
            ("xy Z", ["zxy", "yzx", "zyx", "xy", "yx"], "zxy"),             # Palabra con letras intercambiadas
        ]
    )
    def test_shortest_completing_word(self, licensePlate, words, expected_output):
        """
        Prueba parametrizada para validar la función shortestCompletingWord.

        Args:
            licensePlate (str): La cadena que contiene caracteres no relevantes (como números y espacios).
            words (List[str]): La lista de palabras con las que se comparará.
            expected_output (str): La palabra que debería ser la respuesta correcta.
        """
        result = self.solution.shortestCompletingWord(licensePlate, words)
        assert result == expected_output
