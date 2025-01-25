import pytest
from challenge import Solution  # Importamos la clase Solution desde el archivo challenge

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected_output",
        [
            # Caso 1: Matriz 2xN simple
            ([[[2, 5, 4], [1, 5, 2]]], 4),

            # Caso 2: Matriz con una única columna
            ([[[3], [1]]], 0),

            # Caso 3: Matriz con valores altos
            ([[[10, 20, 30], [30, 20, 10]]], 20),

            # Caso 4: Matriz donde ambos caminos tienen la misma suma final
            ([[[1, 3, 1], [3, 1, 3]]], 3),

            # Caso 5: Matriz optimizada para el primer robot
            ([[[1, 2, 3, 4], [4, 3, 2, 1]]], 4),

            # Caso 6: Matriz con valores grandes y mixtos
            ([[[5, 10, 15, 20], [20, 15, 10, 5]]], 25),

            # Caso 7: Todos los valores son iguales
            ([[[1, 1, 1, 1], [1, 1, 1, 1]]], 1),
        ]
    )
    def test_grid_game(self, grid, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función gridGame.

        Args:
            grid (List[List[int]]): Matriz 2xN representando los puntos en cada posición.
            expected_output (int): Resultado esperado para el puntaje mínimo que puede obtener el segundo robot.
        """
        assert self.solution.gridGame(grid) == expected_output
