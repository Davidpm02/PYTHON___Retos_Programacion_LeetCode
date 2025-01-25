import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "isWater, expected_output",
        [
            # Caso básico: celda de agua rodeada por tierra
            (
                [
                    [0, 1, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                ],
                [
                    [1, 0, 1],
                    [2, 1, 2],
                    [3, 2, 3],
                ],
            ),
            # Caso donde toda la matriz es agua
            (
                [
                    [1, 1],
                    [1, 1],
                ],
                [
                    [0, 0],
                    [0, 0],
                ],
            ),
            # Caso donde toda la matriz es tierra
            (
                [
                    [0, 0],
                    [0, 0],
                ],
                [
                    [1, 2],
                    [2, 3],
                ],
            ),
            # Caso con agua en esquinas opuestas
            (
                [
                    [1, 0, 0],
                    [0, 0, 0],
                    [0, 0, 1],
                ],
                [
                    [0, 1, 2],
                    [1, 2, 1],
                    [2, 1, 0],
                ],
            ),
        ]
    )
    def test_highest_peak(self, isWater, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método highestPeak.

        Args:
            isWater (List[List[int]]): Matriz binaria de entrada indicando agua (1) y tierra (0).
            expected_output (List[List[int]]): Matriz de alturas esperada.
        """
        assert self.solution.highestPeak(isWater) == expected_output
