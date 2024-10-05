import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str_list, expected_output",
        [
            (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),  # Ejemplo básico
            (["a", "b", "c"], ["c", "b", "a"]),                    # Ejemplo con tres caracteres
            (["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "c", "e", "c", "a", "r"]),  # Palíndromo
            ([], []),                                              # Caso vacío
            (["A"], ["A"]),                                      # Solo un carácter
            (["H", "e", "l", "l", "o"], ["o", "l", "l", "e", "H"]),  # Diferentes caracteres
            (["1", "2", "3", "4"], ["4", "3", "2", "1"]),        # Números como cadenas
            ([" ", "a", " "], [" ", "a", " "]),                  # Espacios alrededor de un carácter
        ]
    )
    def test_reverse_string(self, input_str_list, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función reverseString.

        Args:
            input_str_list (List[str]): El array de strings que se probará para invertir.
            expected_output (List[str]): El resultado esperado después de invertir el array.
        """
        self.solution.reverseString(input_str_list)
        assert input_str_list == expected_output
