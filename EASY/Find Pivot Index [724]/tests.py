import pytest
from challenge import Solution  # Ajusta el nombre del archivo si es necesario.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 7, 3, 6, 5, 6], 3),         # Índice 3 es el pivote, ya que las sumas son iguales (6+5+6) = (1+7+3)
            ([1, 2, 3], -1),                 # No existe un índice pivote donde las sumas son iguales
            ([2, 1, -1, 1, 1], 2),           # Índice 2 es el pivote
            ([1, 2, 3, 4, 5], -1),           # No hay índice pivote
            ([1, 1, 1, 1, 1], 2),            # Índice 2 es el pivote, ya que las sumas son iguales (1+1) = (1+1+1)
            ([], -1),                        # Lista vacía, no existe índice pivote
            ([1], 0),                        # Solo un elemento, el índice pivote es 0
            ([0, 0, 0, 0], 1),               # Índice 1 es el pivote, ya que las sumas son iguales (0) = (0+0)
        ]
    )
    def test_pivotIndex(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función pivotIndex.

        Args:
            nums (List[int]): La lista de números que se probará.
            expected_output (int): El resultado esperado del índice pivote.
        """
        assert self.solution.pivotIndex(nums) == expected_output
