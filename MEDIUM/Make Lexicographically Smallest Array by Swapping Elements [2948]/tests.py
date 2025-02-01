import pytest
from challenge import Solution  # Asegúrate de que el archivo challenge.py contiene la clase Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, limit, expected_output",
        [
            ([3, 1, 2, 4], 1, [1, 2, 3, 4]),  # Los elementos pueden unirse, ya que las diferencias son <= 1
            ([1, 3, 2, 4], 2, [1, 2, 3, 4]),  # Los elementos pueden unirse, ya que las diferencias son <= 2
            ([5, 4, 3, 2], 0, [2, 3, 4, 5]),  # Los elementos deben ser ordenados, no se pueden unir
            ([1, 5, 3, 2, 4], 1, [1, 2, 3, 4, 5]),  # Ordenados lexicográficamente dentro del límite
            ([10, 20, 30], 5, [10, 20, 30]),  # No hay cambios posibles debido a las diferencias mayores al límite
            ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),  # Ningún cambio necesario, ya está ordenado
            ([10, 15, 5, 20], 10, [5, 10, 15, 20]),  # Ordenación por componentes
        ]
    )
    def test_lexicographically_smallest_array(self, nums, limit, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método lexicographicallySmallestArray.

        Args:
            nums (List[int]): Lista de números que se probarán.
            limit (int): Límite de diferencia para agrupar los números.
            expected_output (List[int]): El resultado esperado después de ordenar el array de forma lexicográfica.
        """
        assert self.solution.lexicographicallySmallestArray(nums, limit) == expected_output
