import pytest
from collections import Counter
from typing import List
from challenge import Solution  # Importar la clase Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 2, 2, 3, 1], 2),                        # Caso común: [2, 2] tiene el mayor grado (2 veces), sublista más corta de mayor grado tiene tamaño 2
            ([1, 2, 2, 3, 1, 4, 2], 6),                  # Caso en el que el grado máximo de 2 ocurre entre indices [1, 4], longitud 6
            ([1, 1, 1, 1], 4),                          # Todos los elementos tienen el mismo grado (4 veces), la sublista mínima es toda la lista
            ([1, 2, 3, 4, 5], 1),                       # Caso sin repeticiones, el subarray de menor grado es de tamaño 1
            ([5, 5, 5, 5], 4),                          # Todos los elementos son iguales, por lo que el subarray mínimo es todo
            ([1, 2, 3, 3, 4, 5, 6, 7], 2),              # Subarray con la mayor repetición 3 ocurrencias, subarray [3, 3]
            ([4, 4, 2, 2, 1, 1, 1], 3),                  # El 1 tiene el mayor grado de 3, el subarray más pequeño es [1, 1, 1]
            ([4, 2, 2, 2, 5], 3),                       # El 2 tiene el mayor grado de 3, subarray [2, 2, 2] de tamaño 3
            ([7], 1),                                    # Caso de lista con solo un elemento, el subarray más corto es de tamaño 1
            ([10, 10, 2, 3, 3, 3, 2], 3),                # El número 3 ocurre 3 veces, subarray mínimo [3, 3, 3]
        ]
    )
    def test_find_shortest_subarray(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findShortestSubArray.

        Args:
            nums (List[int]): La lista de números en la que se busca el subarray.
            expected_output (int): El tamaño esperado de la sublista de mayor grado.
        """
        assert self.solution.findShortestSubArray(nums) == expected_output
