import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums1, nums2, expected_output",
        [
            ([1, 2, 3], [1, 2, 3], 1),        # Ejemplo básico: un único triplete válido
            ([1, 2, 3], [3, 2, 1], 0),        # No se puede formar ningún triplete válido
            ([1, 3, 2], [3, 1, 2], 1),        # Un triplete válido se puede formar
            ([1, 2, 3, 4], [4, 3, 2, 1], 0),  # Ningún triplete válido, todos están en orden inverso
            ([1, 2, 3, 4], [1, 2, 3, 4], 4),  # Cada combinación de tripletes es válida
            ([1, 3, 2, 4], [1, 4, 3, 2], 2),  # Dos tripletes válidos se pueden formar
            ([1, 2, 3, 4], [4, 3, 1, 2], 0),  # Ningún triplete válido por posiciones desordenadas
            ([1, 2], [2, 1], 0),              # Con solo dos elementos no es posible formar un triplete
            ([1, 3, 5, 7], [7, 5, 3, 1], 0),  # Todos los elementos están invertidos, no se puede formar triplete
        ]
    )
    def test_good_triplets(self, nums1, nums2, expected_output):
        """
        Prueba parametrizada para validar el número de tripletes válidos.

        Args:
            nums1 (List[int]): Primer arreglo con enteros.
            nums2 (List[int]): Segundo arreglo con enteros.
            expected_output (int): Resultado esperado de los tripletes válidos.
        """
        assert self.solution.goodTriplets(nums1, nums2) == expected_output
