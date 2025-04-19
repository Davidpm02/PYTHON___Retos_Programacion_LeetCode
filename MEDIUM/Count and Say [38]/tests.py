import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, "1"),                  # Primer término de la secuencia
            (2, "11"),                 # Un uno => "11"
            (3, "21"),                 # Dos unos => "21"
            (4, "1211"),               # Un dos, un uno => "1211"
            (5, "111221"),             # Un uno, un dos, dos unos => "111221"
            (6, "312211"),             # Tres unos, dos doses, un uno => "312211"
            (7, "13112221"),           # Traducción directa del anterior
            (8, "1113213211"),         # Y así sucesivamente...
            (9, "31131211131221"),
            (10, "13211311123113112211"),
        ]
    )
    def test_count_and_say(self, n, expected_output):
        """
        Prueba parametrizada para validar la generación de la secuencia Count and Say.

        Args:
            n (int): Número de iteraciones de la secuencia.
            expected_output (str): Resultado esperado correspondiente a la n-ésima iteración.
        """
        assert self.solution.countAndSay(n) == expected_output
