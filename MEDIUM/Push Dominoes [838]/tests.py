import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "dominoes, expected_output",
        [
            ("RR.L", "RR.L"),          # Caso simple donde la fuerza hacia la derecha no afecta el dominó que está en el medio
            ("R.L", "R.L"),            # Dominó con espacio vacío que no recibe fuerza de ninguno de los lados
            ("L.R", "L.R"),            # El domino es equilibrado, las fuerzas se contrarrestan
            (".L.R.", "LL.RR."),       # Caso donde el dominó en el medio recibe fuerzas de ambos lados
            ("...R..L", "...RRLL"),    # Caso de dominós con espacio en el medio que se desplazan
            ("...L...R...", "LL.RR..."),  # Fuerzas que se aplican en ambas direcciones, resultado con varios dominós afectados
            ("R", "R"),                # Solo un dominó empujado a la derecha, el resultado es igual
            ("L", "L"),                # Solo un dominó empujado a la izquierda, el resultado es igual
            ("....", "...."),          # Caso con sólo dominós en posición vertical, no cambia nada
            ("R.L.L", "RR.L.L"),       # Caso con fuerzas a la derecha y la izquierda en posiciones alternas
        ]
    )
    def test_push_dominoes(self, dominoes, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método pushDominoes.

        Args:
            dominoes (str): Cadena que representa el estado inicial de los dominós.
            expected_output (str): El estado final esperado después de aplicar las fuerzas.
        """
        assert self.solution.pushDominoes(dominoes) == expected_output
