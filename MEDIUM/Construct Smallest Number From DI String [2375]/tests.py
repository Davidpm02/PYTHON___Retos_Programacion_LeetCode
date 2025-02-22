import pytest
from challenge import Solution  # Se importa la clase Solution desde challenge.py

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "pattern, expected_output",
        [
            ("I", "12"),     # Caso más simple con un solo incremento
            ("D", "21"),     # Caso más simple con un solo decremento
            ("ID", "132"),   # Alternancia de incremento y decremento
            ("DD", "321"),   # Dos decrementos consecutivos
            ("II", "123"),   # Dos incrementos consecutivos
            ("DID", "2143"), # Caso intercalado
            ("IID", "1234"), # Dos incrementos seguidos de un decremento
            ("DDI", "3214"), # Dos decrementos seguidos de un incremento
        ]
    )
    def test_smallest_number(self, pattern, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función smallestNumber.

        Args:
            pattern (str): El patrón de restricciones sobre los dígitos.
            expected_output (str): La cadena de salida esperada.
        """
        assert self.solution.smallestNumber(pattern) == expected_output
