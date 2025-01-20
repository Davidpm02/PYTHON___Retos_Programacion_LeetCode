import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "derived, expected_output",
        [
            ([1, 1, 1, 1], True),                  # Paridad de '1's es par (4), debería retornar True
            ([1, 0, 1, 1], False),                 # Paridad de '1's es impar (3), debería retornar False
            ([0, 0, 0], True),                    # No hay '1's, paridad de '1's es 0 (par), debería retornar True
            ([1, 1], True),                       # Paridad de '1's es par (2), debería retornar True
            ([1], False),                         # Paridad de '1's es impar (1), debería retornar False
            ([0, 1, 1, 1, 0, 1, 0], False),       # Paridad de '1's es impar (4), debería retornar False
            ([0, 1, 1], False),                   # Paridad de '1's es impar (2), debería retornar False
            ([1, 0, 0, 1, 1, 0], True),           # Paridad de '1's es par (4), debería retornar True
            ([1, 1, 1, 0, 0], True),              # Paridad de '1's es par (3), debería retornar True
            ([0], True),                          # Cadena con un solo elemento 0, debería retornar True
        ]
    )
    def test_does_valid_array_exist(self, derived, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función doesValidArrayExist.

        Args:
            derived (List[int]): La lista de enteros que se verifica si puede provenir de un array binario.
            expected_output (bool): El resultado esperado para cada lista dada.
        """
        assert self.solution.doesValidArrayExist(derived) == expected_output
