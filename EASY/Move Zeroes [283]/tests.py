import pytest
from challenge import Solution  # Se asume que el archivo del reto se llama challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),        # Caso típico, se mueven los ceros al final
            ([0, 0, 1], [1, 0, 0]),                      # Dos ceros al inicio, se mueven al final
            ([1, 2, 3], [1, 2, 3]),                      # Sin ceros, el array se mantiene igual
            ([0, 0, 0], [0, 0, 0]),                      # Solo ceros, no hay cambios
            ([4, 0, 5, 0, 6], [4, 5, 6, 0, 0]),          # Mezcla de enteros y ceros
            ([1], [1]),                                  # Un solo elemento, sin ceros
            ([0], [0]),                                  # Un solo elemento que es cero
        ]
    )
    def test_move_zeroes(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función moveZeroes.

        Args:
            nums (List[int]): Lista de números que será procesada para mover ceros al final.
            expected_output (List[int]): Lista esperada después de mover los ceros.
        """
        self.solution.moveZeroes(nums)
        assert nums == expected_output
