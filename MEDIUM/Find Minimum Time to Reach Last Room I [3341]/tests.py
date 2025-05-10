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
                    [0, 1],
                    [1, 2]
                ],
                3
            ),  # Camino óptimo: (0,0) -> (1,0) -> (1,1), respetando tiempos
            (
                [
                    [0, 100],
                    [0, 0]
                ],
                3
            ),  # Debe evitar la celda (0,1) y tomar el camino por (1,0)
            (
                [
                    [0, 2, 4],
                    [2, 5, 6],
                    [3, 2, 1]
                ],
                7
            ),  # Múltiples caminos posibles; el algoritmo elige el de menor costo
            (
                [
                    [0, 1, 2],
                    [3, 8, 2],
                    [5, 3, 1]
                ],
                7
            ),  # Variante con restricciones de tiempo que obligan a esperar
            (
                [
                    [0]
                ],
                0
            ),  # Ya se encuentra en la posición destino
            (
                [
                    [0, 100000],
                    [100000, 0]
                ],
                100001
            ),  # Obligado a esperar largos periodos debido a restricciones
        ]
    )
    def test_min_time_to_reach(self, moveTime, expected_output):
        """
        Prueba parametrizada para validar distintos mapas de tiempo de movimiento
        en la dungeon.

        Args:
            moveTime (List[List[int]]): Matriz de tiempos mínimos para moverse a cada celda.
            expected_output (int): Tiempo mínimo total esperado para alcanzar la celda destino.
        """
        assert self.solution.minTimeToReach(moveTime) == expected_output
