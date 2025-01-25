import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "arr, mat, expected_output",
        [
            # Caso base: arr con un solo elemento
            ([1], [[1]], 0),

            # Matriz de 2x2 donde la primera fila se completa primero
            ([1, 2, 3, 4], [[1, 2], [3, 4]], 1),

            # Matriz de 2x2 donde la primera columna se completa primero
            ([1, 3, 2, 4], [[1, 2], [3, 4]], 1),

            # Caso donde la última celda completa una fila
            ([4, 2, 1, 3], [[1, 2], [3, 4]], 3),

            # Matriz de 3x3 con fila completa en medio del proceso
            ([9, 3, 5, 7, 1, 4, 2, 8, 6], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], 4),

            # Matriz más grande con columnas completadas primero
            ([10, 6, 15, 5, 8, 12, 14, 2, 11, 7, 13, 9, 1, 4, 3], 
             [[10, 11, 12, 13, 14], [15, 1, 2, 3, 4], [5, 6, 7, 8, 9]], 8),

            # Caso donde nunca se completa una fila/columna
            ([1, 2, 3, 4, 5, 6], [[1, 2, 3], [4, 5, 6]], -1),

            # Matriz con un único elemento repetido (se completa en el primer paso)
            ([7, 7, 7], [[7, 7], [7, 7]], 0),
        ]
    )
    def test_first_complete_index(self, arr, mat, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función firstCompleteIndex.

        Args:
            arr (List[int]): Lista de números a pintar.
            mat (List[List[int]]): Matriz de números.
            expected_output (int): Índice esperado del primer completo.
        """
        result = self.solution.firstCompleteIndex(arr, mat)
        assert result == expected_output
