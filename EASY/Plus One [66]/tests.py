import pytest
from challenge import Solution  # Asegúrate de que el nombre de la clase y el archivo coincidan

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "digits, expected_output",
        [
            # Casos comunes
            ([1, 2, 3], [1, 2, 4]),  # Ejemplo típico: 123 + 1 = 124
            ([9, 9, 9], [1, 0, 0, 0]),  # Ejemplo con acarreo: 999 + 1 = 1000
            ([0], [1]),  # Caso donde el número es 0: 0 + 1 = 1
            ([8, 9, 9], [9, 0, 0]),  # Caso con acarreo: 899 + 1 = 900
            ([4, 3, 2], [4, 3, 3]),  # Caso general sin acarreo: 432 + 1 = 433
            ([9], [1, 0]),  # Caso con un solo 9: 9 + 1 = 10
            ([1, 0, 0, 0], [1, 0, 0, 1]),  # Caso con 1000 + 1 = 1001
            ([1, 9, 9, 9], [2, 0, 0, 0]),  # Caso con 1999 + 1 = 2000
            ([0, 0], [0, 1]),  # Caso con ceros al inicio: 00 + 1 = 01
        ]
    )
    def test_plus_one(self, digits, expected_output):
        """
        Prueba parametrizada para validar la función plusOne.

        Args:
            digits (List[int]): El array de dígitos que representa un número.
            expected_output (List[int]): El array esperado con el número + 1.
        """
        assert self.solution.plusOne(digits) == expected_output
