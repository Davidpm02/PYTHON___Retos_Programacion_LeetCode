import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected_output",
        [
            ("011101", 4),   # Split en "011|101", 2 bits "0" a la izquierda, 2 bits "1" a la derecha. Máxima puntuación es 4.
            ("00111", 3),    # Split en "00|111", 2 bits "0" a la izquierda, 1 bit "1" a la derecha. Máxima puntuación es 3.
            ("1111", 2),     # Split en "1|111", 0 bits "0" a la izquierda, 3 bits "1" a la derecha. Máxima puntuación es 3.
            ("00000", 0),    # Split en "0|0000", 1 bit "0" a la izquierda, 0 bits "1" a la derecha. Máxima puntuación es 1.
            ("1", 0),        # Sólo un bit "1", no se puede hacer split, la puntuación es 0.
            ("0", 1),        # Sólo un bit "0", no se puede hacer split, la puntuación es 1.
            ("010101010", 5), # La máxima puntuación se logra en el split en "010|101010", 3 bits "0" a la izquierda y 2 bits "1" a la derecha.
        ]
    )
    def test_max_score(self, s, expected_output):
        """
        Prueba parametrizada para validar la función maxScore.

        Args:
            s (str): La cadena binaria que se dividirá.
            expected_output (int): La máxima puntuación esperada.
        """
        assert self.solution.maxScore(s) == expected_output
