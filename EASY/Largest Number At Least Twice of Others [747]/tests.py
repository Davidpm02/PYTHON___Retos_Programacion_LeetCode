import pytest
from challenge import Solution  # Ajusta el import si el nombre del archivo es diferente.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([3, 6, 1, 0], 1),           # El mayor número es 6 y es al menos el doble de los demás.
            ([1, 2, 3, 4], -1),          # 4 no es el doble de 3, así que debería retornar -1.
            ([1, 0], 0),                 # 1 es el doble de 0, así que el índice de 1 es 0.
            ([10, 2, 5, 7], 0),          # El 10 es mayor que el doble de todos los demás.
            ([0, 0, 0, 1], 3),           # El único número no cero es 1, y es el doble de 0.
            ([100, 20, 30, 40], 0),      # El 100 es al menos el doble de los demás números.
            ([5, 8, 10, 1], -1),         # Ningún número es al menos el doble de los demás.
            ([50, 25, 10, 5, 0], 0),     # 50 es el doble de los otros números en la lista.
            ([2, 5, 1, 4], -1),          # El 5 no es el doble de todos los otros números.
        ]
    )
    def test_dominantIndex(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función dominantIndex.

        Args:
            nums (List[int]): La lista de números a evaluar.
            expected_output (int): El índice esperado del número dominante o -1 si no aplica.
        """
        assert self.solution.dominantIndex(nums) == expected_output
