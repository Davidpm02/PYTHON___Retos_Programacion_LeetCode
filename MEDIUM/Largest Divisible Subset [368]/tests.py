import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_outputs",
        [
            ([1, 2, 3], [[1, 2], [1, 3]]),  # Hay dos subconjuntos válidos posibles
            ([1, 2, 4, 8], [[1, 2, 4, 8]]),  # Todos los elementos forman un subconjunto divisible
            ([3, 5, 10, 20, 21], [[5, 10, 20]]),  # Subconjunto más largo válido
            ([1], [[1]]),  # Caso con un solo número
            ([1, 3, 6, 24], [[1, 3, 6, 24]]),  # Todos se encadenan por divisibilidad
            ([2, 3, 4, 9, 8], [[2, 4, 8]]),  # Subconjunto divisible más largo
            ([], [[]]),  # Entrada vacía debe devolver lista vacía
            ([5, 10, 100, 2, 20], [[2, 10, 100], [5, 10, 20]]),  # Varias soluciones posibles
        ]
    )
    def test_largest_divisible_subset(self, nums, expected_outputs):
        """
        Pruebo distintos casos del método largestDivisibleSubset verificando que
        el resultado sea un subconjunto válido y esté entre los esperados.

        Args:
            nums (List[int]): Lista de entrada con enteros positivos.
            expected_outputs (List[List[int]]): Subconjuntos válidos esperados.
        """
        result = self.solution.largestDivisibleSubset(nums)

        # Compruebo que el resultado está en la lista de posibles subconjuntos esperados
        assert result in expected_outputs

        # Verifico que todos los elementos del resultado forman una cadena divisible
        for i in range(len(result)):
            for j in range(i):
                assert result[i] % result[j] == 0
