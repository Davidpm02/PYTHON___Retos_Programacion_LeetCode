import pytest
from challenge import Solution  # Asegúrate de que el nombre del archivo donde resides la clase Solution sea "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("A man, a plan, a canal: Panama", True),     # Ejemplo clásico de palíndromo
            ("race a car", False),                        # Ejemplo de una cadena que no es un palíndromo
            (" ", True),                                  # Una cadena vacía o solo con espacios es un palíndromo
            ("", True),                                   # Una cadena vacía es un palíndromo
            ("No 'x' in Nixon", True),                    # Palíndromo con caracteres especiales y mayúsculas
            ("12321", True),                              # Palíndromo numérico
            ("12345", False),                             # Número que no es un palíndromo
            ("Madam", True),                              # Palíndromo con mayúsculas y minúsculas
            ("Able was I ere I saw Elba", True),          # Palíndromo conocido
        ]
    )
    def test_is_palindrome(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función isPalindrome.

        Args:
            input_str (str): La cadena que se probará si es palíndromo.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.isPalindrome(input_str) == expected_output

