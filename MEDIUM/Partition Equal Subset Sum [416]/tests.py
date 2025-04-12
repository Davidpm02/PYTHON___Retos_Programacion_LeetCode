import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 5, 11, 5], True),            # Puede dividirse en [1, 5, 5] y [11]
            ([1, 2, 3, 5], False),            # No puede dividirse en dos subconjuntos con la misma suma
            ([2, 2, 3, 5], False),            # Suma total impar (12), pero no se puede particionar
            ([1, 1], True),                  # Caso simple: dos números iguales
            ([1, 2, 5], False),              # No se puede alcanzar la mitad de la suma total
            ([3, 3, 3, 4, 5], True),         # Subconjuntos: [3, 3, 4] y [3, 5]
            ([100], False),                 # Un solo número no puede particionarse
            ([1]*100, True),                # 100 unos, suma par, se puede dividir en dos subconjuntos de 50
            ([2, 2, 2, 2, 2, 2], True),     # Todos iguales, número par de elementos
            ([1, 2, 3, 4, 6], True),        # Puede dividirse en [1, 3, 6] y [2, 4, 4]
        ]
    )
    def test_can_partition(self, nums, expected_output):
        """
        Prueba parametrizada para verificar distintos escenarios para canPartition.

        Args:
            nums (List[int]): Lista de enteros positivos.
            expected_output (bool): Resultado esperado que indica si la lista se puede dividir.
        """
        assert self.solution.canPartition(nums) == expected_output
