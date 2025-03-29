import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 2, 3], 2, 6),                    # Caso básico con 3 números
            ([5, 3, 7, 2], 3, 945),               # Caso con varios números y operaciones limitadas
            ([10, 10, 10], 1, 10),                # Caso donde todos los números son iguales
            ([10, 20, 30], 0, 1),                 # Caso con 0 operaciones disponibles
            ([100, 50, 25], 5, 500000000),       # Caso con números grandes
            ([2, 3, 5, 7], 4, 210),              # Caso con números primos y 4 operaciones
            ([8, 16, 24], 2, 384),               # Caso con múltiplos de 8
            ([7, 7, 7, 7], 4, 2401),             # Caso donde todos los números son iguales y hay muchas operaciones
            ([1, 1, 1, 1, 1], 3, 1),             # Caso donde todos los números son 1
        ]
    )
    def test_maximum_score(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maximumScore.

        Args:
            nums (List[int]): El array de enteros.
            k (int): El número de operaciones disponibles.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.maximumScore(nums, k) == expected_output
