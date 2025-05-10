import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "moveTime, expected_output",
        [
            (
                [
                    [0, 0],
                    [0, 0]
                ],
                3
            ),  # Camino óptimo: coste alternante (1 + 2)
            (
                [
                    [0, 10],
                    [0, 0]
                ],
                5
            ),  # Debe evitar (0,1) debido a su tiempo mínimo 10
            (
                [
                    [0, 0, 0],
                    [100, 100, 100],
                    [0, 0, 0]
                ],
                7
            ),  # Tiene que esperar en la fila intermedia por restricciones altas
            (
                [
                    [0]
                ],
                0
            ),  # Ya está en la posición objetivo
            (
                [
                    [0, 0],
                    [100, 100]
                ],
                104
            ),  # El movimiento forzado implica esperar mucho tiempo
            (
                [
                    [0, 5],
                    [1, 0]
                ],
                5
            ),  # Camino alternante con restricciones intermedias
        ]
    )
    def test_min_time_to_reach(self, moveTime, expected_output):
        """
        Prueba parametrizada para validar diferentes configuraciones de la cuadrícula de mazmorras
        con restricciones de entrada y coste de movimiento alternante.

        Args:
            moveTime (List[List[int]]): Matriz que indica el tiempo mínimo permitido para entrar a cada celda.
            expected_output (int): Tiempo mínimo esperado para llegar a la celda destino.
        """
        assert self.solution.minTimeToReach(moveTime) == expected_output
