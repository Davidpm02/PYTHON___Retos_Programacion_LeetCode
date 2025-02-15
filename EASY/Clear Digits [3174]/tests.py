import pytest
from challenge import Solution  

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("abc123def", "abdef"),   # Elimina 1,2,3 y los caracteres previos
            ("1a2b3c", ""),           # Se eliminan todos los caracteres
            ("hello42world", "hellorld"), # Se eliminan '2', '4' y caracteres previos
            ("a1b2c3d4e5", ""),      # Todo queda eliminado
            ("noDigitsHere", "noDigitsHere"),  # Sin cambios si no hay dígitos
            ("5start", "tart"),      # Se elimina '5' y el carácter previo (s)
            ("middle9test", "midtest"), # Se elimina '9' y el carácter previo (e)
            ("98number", "mber"),    # Se eliminan '8', '9' y caracteres previos (nu)
            ("0leading", "eading"),  # Se elimina '0' y el carácter previo (l)
            ("final7", "final"),     # Se elimina '7' y el carácter previo (l)
        ]
    )
    def test_clear_digits(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función clearDigits.

        Args:
            input_str (str): La cadena de entrada.
            expected_output (str): El resultado esperado después del procesamiento.
        """
        assert self.solution.clearDigits(input_str) == expected_output
