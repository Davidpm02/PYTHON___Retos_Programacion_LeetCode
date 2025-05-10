import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums1, nums2, expected_output",
        [
            ([1, 2, 3], [3, 2, 1], 6),        # Las dos listas ya tienen la misma suma
            ([0, 2, 3], [3, 2, 1], 6),        # Un cero en nums1, la suma debe igualar a 6
            ([1, 0, 3], [3, 2, 1], 6),        # Un cero en nums1, la suma debe igualar a 6
            ([1, 0, 3], [2, 2, 1], -1),       # No es posible igualar las sumas con los ceros
            ([0, 0, 0], [0, 0, 0], 3),       # Reemplazando los ceros por 1, la suma es 3
            ([0, 0, 0], [1, 1, 1], 3),       # Reemplazando ceros por 1 en nums1, sumando 3
            ([1, 1, 0], [1, 0, 1], 3),       # Ambos tienen ceros, el mínimo target es 3
            ([0, 0, 0], [0, 0, 2], 3),       # Caso donde el target mínimo es 3
            ([5, 0, 3], [3, 0, 1], 9),       # El objetivo es 9 después de reemplazar ceros
            ([0, 0], [0, 0], 2),             # Reemplazando ceros por 1, la suma es 2
            ([1, 2, 0], [0, 0, 0], 5),       # No puede alcanzar la igualdad si se rellenan ceros
            ([5, 0, 0], [2, 2, 0], 7),       # Necesita remplazar ceros para hacer la suma igual
        ]
    )
    def test_min_sum(self, nums1, nums2, expected_output):
        """
        Prueba parametrizada para validar el mínimo de la suma de las dos listas al reemplazar ceros.

        Args:
            nums1 (List[int]): Primera lista de enteros.
            nums2 (List[int]): Segunda lista de enteros.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.minSum(nums1, nums2) == expected_output

    def test_edge_case(self):
        """Prueba para verificar comportamiento con listas vacías o con ceros repetidos."""
        # Caso cuando ambas listas están vacías
        assert self.solution.minSum([], []) == 0
        # Caso cuando una lista está vacía y la otra tiene ceros
        assert self.solution.minSum([0, 0], []) == 2  # Reemplazo de ceros por 1 en la primera lista
        # Caso cuando una lista tiene ceros y la otra no tiene ceros
        assert self.solution.minSum([0, 0], [3, 2]) == -1  # No es posible balancear
