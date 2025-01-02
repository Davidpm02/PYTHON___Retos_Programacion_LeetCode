import pytest
from challenge import Solution  # Asegúrate de ajustar el nombre del archivo si es necesario.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "image, expected_output",
        [
            ([[1, 1, 0], [0, 1, 1], [1, 0, 1]], [[1, 0, 0], [0, 0, 1], [0, 1, 1]]),  # Caso general
            ([[1, 0], [0, 1]], [[1, 0], [1, 0]]),                                        # Caso con imagen pequeña de 2x2
            ([[0, 0], [1, 1]], [[1, 1], [0, 0]]),                                        # Caso con todos ceros o unos
            ([[1]], [[0]]),                                                              # Caso con una sola celda de 1
            ([[0]], [[1]]),                                                              # Caso con una sola celda de 0
            ([[1, 0, 1]], [[0, 1, 0]]),                                                  # Caso con una fila de longitud 3
            ([[0, 1, 0], [1, 0, 1]], [[1, 0, 1], [0, 1, 0]]),                          # Caso con dos filas de longitud 3
            ([[1, 0, 1, 1, 0], [0, 1, 0, 1, 1]], [[1, 1, 0, 1, 0], [0, 1, 0, 1, 1]]),  # Caso con imagen más larga
        ]
    )
    def test_flipAndInvertImage(self, image, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función flipAndInvertImage.

        Args:
            image (List[List[int]]): La imagen que se va a voltear e invertir.
            expected_output (List[List[int]]): La imagen procesada esperada.
        """
        assert self.solution.flipAndInvertImage(image) == expected_output
