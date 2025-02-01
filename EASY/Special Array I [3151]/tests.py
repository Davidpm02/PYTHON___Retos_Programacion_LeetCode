import pytest
from challenge import Solution  # Asegúrate de que el archivo challenge.py contiene la clase Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 2, 3, 4, 5], True),                    # Paridad alternante, debe ser True
            ([2, 3, 4, 5, 6], True),                    # Paridad alternante, debe ser True
            ([2, 4, 6, 8], False),                      # Todos son pares, debe ser False
            ([1, 3, 5, 7], False),                      # Todos son impares, debe ser False
            ([1, 2, 3, 4], True),                       # Paridad alternante, debe ser True
            ([1, 2, 4, 6], True),                       # Paridad alternante, debe ser True
            ([2, 1, 2], True),                          # Paridad alternante, debe ser True
            ([1, 2, 3, 4, 5, 6], True),                 # Paridad alternante, debe ser True
            ([1, 1, 1], False),                         # Todos impares, debe ser False
            ([2, 2, 2], False),                         # Todos pares, debe ser False
            ([1], True),                                # Un solo elemento, se considera válido
            ([], True),                                 # Lista vacía, se considera válida
        ]
    )
    def test_is_array_special(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método isArraySpecial.

        Args:
            nums (List[int]): La lista de enteros que se probará.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.isArraySpecial(nums) == expected_output
