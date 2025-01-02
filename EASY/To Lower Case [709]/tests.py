import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution

class TestSolution:
    
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("Hello", "hello"),               # Caso básico, convierte a minúsculas
            ("HELLO", "hello"),               # Caso con todos caracteres en mayúsculas
            ("", ""),                         # Caso con cadena vacía, no debe cambiar
            ("HeLlO WoRlD", "hello world"),   # Caso con mezcla de mayúsculas y minúsculas
            ("123 ABC", "123 abc"),           # Caso con números y letras, solo afecta a las letras
            ("   SPACE   ", "   space   "),   # Caso con espacios, deben permanecer sin cambios
            ("UPPERCASE", "uppercase"),       # Otro caso con todo en mayúsculas
            ("already lowercase", "already lowercase"),  # Caso con todo en minúsculas
        ]
    )
    def test_to_lower_case(self, input_str, expected_output):
        """
        Prueba parametrizada para validar la función toLowerCase.

        Args:
            input_str (str): La cadena que será transformada a minúsculas.
            expected_output (str): El resultado esperado después de la transformación.
        """
        assert self.solution.toLowerCase(input_str) == expected_output
