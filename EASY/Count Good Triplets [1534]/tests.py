import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "arr, a, b, c, expected_output",
        [
            ([3, 0, 1, 1, 9, 7], 7, 2, 3, 4),          # Ejemplo típico con múltiples tripletes válidos
            ([1, 1, 2, 2, 3], 0, 0, 1, 0),             # Restricciones muy estrictas: ningún triplete válido
            ([1, 2, 3, 4, 5], 10, 10, 10, 10),         # Restricciones muy permisivas: todos los tripletes válidos
            ([1, 2, 3], 1, 1, 1, 0),                   # Solo un triplete posible, pero no cumple restricciones
            ([1, 1, 1], 0, 0, 0, 1),                   # Solo un triplete (0,1,2) cumple porque todos los elementos son iguales
            ([1, 3, 5, 7], 2, 2, 2, 0),                # Distancias demasiado grandes, ningún triplete cumple
            ([1, 2, 1, 2], 1, 1, 1, 4),                # Hay repeticiones que dan lugar a múltiples tripletes válidos
        ]
    )
    def test_count_good_triplets(self, arr, a, b, c, expected_output):
        """
        Prueba parametrizada para validar la cantidad de buenos tripletes encontrados.

        Args:
            arr (List[int]): Lista de enteros sobre la que se buscarán tripletes válidos.
            a (int): Límite máximo para |arr[i] - arr[j]|.
            b (int): Límite máximo para |arr[j] - arr[k]|.
            c (int): Límite máximo para |arr[i] - arr[k]|.
            expected_output (int): Número esperado de buenos tripletes que cumplen todas las condiciones.
        """
        assert self.solution.countGoodTriplets(arr, a, b, c) == expected_output
