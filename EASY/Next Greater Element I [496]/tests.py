import pytest
from challenge import Solution  # Ajusta el nombre del archivo o el módulo según corresponda

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums1, nums2, expected_output",
        [
            # Caso común con números de ejemplo
            ([4,1,2], [1,3,4,2,5], [5, 3, -1]),  # Ejemplo típico donde cada número de nums1 tiene un siguiente mayor en nums2
            
            # Caso con números de nums1 que no tienen un siguiente mayor
            ([4,3,2], [1,3,4,2,5], [-1, -1, -1]), # Todos los números no tienen un siguiente mayor
            
            # Caso donde nums1 tiene números más pequeños que todos en nums2
            ([1,2], [3,4,5], [3, 3]),  # Los números de nums1 tienen el siguiente mayor dentro de nums2
            
            # Caso donde nums1 y nums2 tienen elementos repetidos
            ([2,4], [4,3,2,1,4], [4, -1]),  # Se verifican duplicados de nums2 en el caso de 4 y 2
            
            # Caso con valores negativos
            ([-1, -2], [-2, -1, 0, 1], [-2, -1]), # Verificación con números negativos en ambos arrays
            
            # Caso con nums1 que es más largo que nums2
            ([4,1,2,3], [1,2], [2, -1, -1, -1]),  # Test cuando nums1 contiene elementos que no están en nums2
            
            # Caso donde nums1 está vacío
            ([], [1, 2, 3, 4], []),  # Resultado vacío debido a que nums1 no tiene elementos
            
            # Caso donde nums2 tiene un único elemento
            ([1], [1], [-1])  # Sólo un elemento en nums2 y nums1 tiene ese único elemento
        ]
    )
    def test_next_greater_element(self, nums1, nums2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función nextGreaterElement.

        Args:
            nums1 (List[int]): Los elementos para los que necesitamos encontrar el siguiente mayor.
            nums2 (List[int]): La lista completa donde buscamos el siguiente mayor.
            expected_output (List[int]): El resultado esperado para cada conjunto de entradas.
        """
        assert self.solution.nextGreaterElement(nums1, nums2) == expected_output
