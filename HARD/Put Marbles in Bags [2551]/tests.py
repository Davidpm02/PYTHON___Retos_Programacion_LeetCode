import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "weights, k, expected_output",
        [
            ([1, 3, 5, 1], 2, 4),          # Caso simple con 2 mochilas, donde la diferencia entre el puntaje máximo y mínimo es 4
            ([1, 3, 5, 1], 3, 2),          # Con 3 mochilas, la diferencia se reduce
            ([1, 1, 1, 1, 1], 3, 0),      # Todos los pesos son iguales, la diferencia entre puntajes es 0
            ([10, 20, 30, 40, 50], 2, 40), # Caso con mármoles de valores diferentes, y con 2 mochilas
            ([10, 20, 30, 40, 50], 5, 0),  # Con el número de mochilas igual al número de mármoles, la diferencia es 0
            ([1, 2, 3, 4], 2, 4),         # Con pocos valores, la diferencia entre el máximo y el mínimo es 4
            ([5, 7, 3, 9, 2], 3, 6),      # Diferentes valores, con 3 mochilas
            ([1, 1, 1, 1], 2, 0),         # Caso con varios 1s, la diferencia es 0
            ([5, 8, 7, 4, 3, 2], 4, 8),   # Otro ejemplo donde la diferencia es mayor
        ]
    )
    def test_put_marbles(self, weights, k, expected_output):
        """
        Prueba parametrizada para validar el método putMarbles.

        Args:
            weights (List[int]): La lista de pesos de los mármoles.
            k (int): El número de mochilas.
            expected_output (int): La diferencia esperada entre el puntaje máximo y mínimo.
        """
        assert self.solution.putMarbles(weights, k) == expected_output
