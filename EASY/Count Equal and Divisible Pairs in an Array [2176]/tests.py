import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([3, 1, 2, 2, 2, 1, 3], 2, 4),           # Ejemplo típico con varias parejas válidas
            ([1, 2, 3, 4], 1, 0),                    # Todos diferentes, ninguna pareja válida
            ([1, 1, 1, 1], 1, 6),                    # Todas iguales y 1 divide todo producto => todas las parejas válidas
            ([1, 2, 1, 2, 1], 3, 2),                 # Algunas coincidencias y restricción con k
            ([1, 1, 1], 5, 0),                       # Todas iguales pero ningún producto i*j divisible por k
            ([5, 5, 5, 5], 10, 2),                   # Algunas parejas cumplen la divisibilidad
            ([2, 2, 2, 2, 2], 4, 4),                 # 10 posibles parejas, pero solo algunas con producto divisible por 4
            ([1], 1, 0),                             # Arreglo con un solo elemento
            ([], 1, 0),                              # Arreglo vacío
        ]
    )
    def test_count_pairs(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar la cantidad de pares (i, j) válidos.

        Args:
            nums (List[int]): Lista de enteros.
            k (int): Valor con el que se valida si el producto de índices es divisible.
            expected_output (int): Cantidad esperada de pares válidos.
        """
        assert self.solution.countPairs(nums, k) == expected_output
