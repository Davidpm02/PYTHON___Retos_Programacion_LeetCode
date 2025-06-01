import pytest
from challenge import Solution  # Importo la clase Solution del fichero challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "label, n, expected_coords",
        [
            (1, 6, (5, 0)),      # Primera casilla en tablero 6x6
            (6, 6, (5, 5)),      # Última casilla fila inferior, dirección izquierda a derecha
            (7, 6, (4, 5)),      # Inicio fila superior siguiente (boustrophedon)
            (12, 6, (4, 0)),     # Cambio de dirección en fila 4
            (36, 6, (0, 0)),     # Última casilla del tablero 6x6
            (1, 3, (2, 0)),      # Tablero 3x3, primera casilla
            (9, 3, (0, 0)),      # Última casilla en 3x3
        ]
    )
    def test_label_to_coords(self, label, n, expected_coords):
        """
        Valida la conversión de etiqueta a coordenadas en la matriz.
        """
        assert self.solution._label_to_coords(label, n) == expected_coords

    @pytest.mark.parametrize(
        "board, expected_moves",
        [
            # Caso trivial 1x1
            ([[-1]], 0),

            # Tablero 2x2 sin serpientes ni escaleras
            ([[-1, -1],
              [-1, -1]], 1),

            # Tablero 3x3 con una escalera en casilla 2 que va a la 9
            ([[-1, -1, -1],
              [-1, -1, -1],
              [-1, 9, -1]], 1),

            # Tablero 6x6 con serpiente que baja de 14 a 4, escalera que sube de 2 a 15
            ([[-1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1],
              [-1, 14, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1],
              [-1, 15, -1, -1, -1, -1]], 4),

            # Tablero 3x3 sin solución posible (serpientes que retroceden siempre)
            ([[-1, -1, -1],
              [-1, 1, -1],
              [-1, -1, -1]], -1),
        ]
    )
    def test_snakes_and_ladders(self, board, expected_moves):
        """
        Valida el cálculo mínimo de tiradas para llegar a la última casilla.
        """
        assert self.solution.snakesAndLadders(board) == expected_moves
