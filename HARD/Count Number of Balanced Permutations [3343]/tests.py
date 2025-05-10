import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            ("12321", 2),  # Caso con permutaciones balanceadas válidas
            ("112233", 0),  # No puede ser balanceado debido a que la suma de los dígitos es impar
            ("111222", 2),  # Permutaciones balanceadas que suman correctamente
            ("123", 0),     # No tiene permutaciones balanceadas debido a la suma impar de los dígitos
            ("111", 0),     # Solo tiene un dígito repetido, imposible balancear
            ("4444", 2),    # Permutaciones balanceadas, todos los dígitos son iguales
            ("9876543210", 0),  # Caso de dígitos sin posibilidad de balancear
            ("222222", 1),      # Solo un dígito repetido, debe ser balanceado
            ("333333333", 0),   # La suma de los dígitos es impar, no se puede balancear
            ("123123", 6),      # Permutaciones balanceadas posibles
        ]
    )
    def test_count_balanced_permutations(self, num, expected_output):
        """
        Prueba parametrizada para validar el número de permutaciones balanceadas en una cadena numérica.

        Args:
            num (str): La cadena de dígitos cuya permutación se va a analizar.
            expected_output (int): El número esperado de permutaciones balanceadas.
        """
        assert self.solution.countBalancedPermutations(num) == expected_output

    def test_invalid_character_in_string(self):
        """Prueba para asegurar que se lanza una excepción si el string contiene caracteres no válidos."""
        with pytest.raises(ValueError):
            self.solution.countBalancedPermutations("123a45")
