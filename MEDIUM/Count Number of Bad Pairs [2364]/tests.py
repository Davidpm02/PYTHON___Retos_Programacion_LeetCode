import pytest
from challenge import Solution  
from typing import List

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_nums, expected_output",
        [
            ([1,2,3,4,5], 0),    # Todos los pares son buenos
            ([4,1,3,3], 2),      # Dos pares malos
            ([1,1,1,1], 6),      # Todos los pares son malos
            ([0,0,0,0], 0),      # Todos los pares son buenos
            ([5,5,5,5,5], 10),   # Máximo número de pares malos
            ([10,20,30,40], 0),  # Progresión aritmética, todos buenos
            ([3,2,1,0], 6),      # Orden inverso, todos malos
            ([1,3,1,3,1,3], 9),  # Alternancia de valores
            ([100,200,300,400], 0),  # Secuencia creciente sin pares malos
            ([9,7,5,3,1], 10)    # Todos los pares son malos
        ]
    )
    def test_count_bad_pairs(self, input_nums: List[int], expected_output: int):
        """
        Prueba parametrizada para validar diferentes casos de la función countBadPairs.

        Args:
            input_nums (List[int]): Lista de números de entrada.
            expected_output (int): El número esperado de 'Bad Pairs'.
        """
        assert self.solution.countBadPairs(input_nums) == expected_output