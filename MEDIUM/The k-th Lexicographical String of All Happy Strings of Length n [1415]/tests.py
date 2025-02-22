import pytest
from challenge import Solution  # Se importa la clase Solution desde challenge.py

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, k, expected_output",
        [
            (1, 1, "a"),     # Caso base con una sola letra
            (1, 3, "c"),     # Última opción posible para n=1
            (3, 1, "aba"),   # Primera combinación lexicográfica con n=3
            (3, 9, "cbc"),   # Última combinación lexicográfica con n=3
            (2, 2, "ba"),    # Segunda combinación para n=2
            (3, 4, "aca"),   # Verificación en el medio de la lista
            (4, 10, "bcac"), # Chequeo con una longitud mayor
            (4, 100, ""),    # k mayor que el total de combinaciones posibles
        ]
    )
    def test_get_happy_string(self, n, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función getHappyString.

        Args:
            n (int): Longitud de la cadena.
            k (int): Índice lexicográfico.
            expected_output (str): La cadena de salida esperada.
        """
        assert self.solution.getHappyString(n, k) == expected_output
