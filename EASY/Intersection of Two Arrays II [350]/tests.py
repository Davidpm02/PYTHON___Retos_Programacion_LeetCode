import pytest
from collections import Counter
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums1, nums2, expected_output",
        [
            ([1, 2, 2, 1], [2, 2], [2, 2]),                # Caso con intersección de elementos repetidos
            ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),          # Caso con múltiples intersecciones
            ([1, 2, 3], [4, 5, 6], []),                    # Caso sin intersección
            ([], [1, 2, 3], []),                           # Caso con el primer array vacío
            ([1, 2, 3], [], []),                           # Caso con el segundo array vacío
            ([], [], []),                                  # Caso con ambos arrays vacíos
            ([1], [1], [1]),                               # Caso con un solo elemento en ambos arrays
            ([1, 1, 1], [1, 1, 1], [1, 1, 1]),             # Caso con elementos repetidos y coincidencia completa
            ([1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4]),    # Caso con arrays iguales en diferente orden
            ([1, 2, 2, 3], [2, 2, 2, 3], [2, 2, 3]),       # Caso con más repeticiones en un array
        ]
    )
    def test_intersect(self, nums1, nums2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función intersect.

        Args:
            nums1 (List[int]): El primer array.
            nums2 (List[int]): El segundo array.
            expected_output (List[int]): El resultado esperado de la intersección.
        """
        result = self.solution.intersect(nums1, nums2)
        assert sorted(result) == sorted(expected_output), f"Se esperaba {expected_output} pero se obtuvo {result}"
