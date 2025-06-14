import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "status, candies, keys, containedBoxes, initialBoxes, expected_output",
        [
            # Caso base: una caja abierta con dulces, sin llaves ni cajas contenidas
            ([1], [10], [[]], [[]], [0], 10),
            
            # Caja cerrada, sin llave, no se puede abrir => 0 dulces
            ([0], [10], [[]], [[]], [0], 0),

            # Caja cerrada, llave en caja inicial para abrirla
            ([0, 0], [10, 20], [[1], []], [[], []], [0], 20),

            # Caja abierta con llave para caja cerrada contenida, se abren ambas
            (
                [1, 0], 
                [5, 10], 
                [[1], []], 
                [[1], []], 
                [0], 
                15
            ),

            # Varias cajas, llaves y cajas contenidas anidadas
            (
                [1, 0, 0, 0], 
                [5, 10, 15, 20], 
                [[1], [2], [], []], 
                [[1], [3], [], []], 
                [0], 
                50
            ),

            # Cajas abiertas inicialmente con dulces y sin llaves ni cajas
            ([1, 1], [10, 15], [[], []], [[], []], [0, 1], 25),

            # Llaves para cajas no encontradas inicialmente (no pueden abrir)
            (
                [0, 0], 
                [10, 20], 
                [[1], []], 
                [[], []], 
                [0], 
                0
            ),

            # Caja con llave para sí misma (no debería generar ciclo infinito)
            (
                [1], 
                [10], 
                [[0]], 
                [[]], 
                [0], 
                10
            ),

            # Caja abierta inicial con caja contenida cerrada y llave para abrirla
            (
                [1, 0], 
                [5, 15], 
                [[], [1]], 
                [[1], []], 
                [0], 
                20
            ),

            # Caso sin cajas iniciales
            ([], [], [], [], [], 0),
        ]
    )
    def test_max_candies(self, status, candies, keys, containedBoxes, initialBoxes, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método maxCandies.

        Args:
            status (List[int]): Estado de cada caja (1 abierta, 0 cerrada).
            candies (List[int]): Cantidad de dulces en cada caja.
            keys (List[List[int]]): Llaves contenidas en cada caja.
            containedBoxes (List[List[int]]): Cajas contenidas en cada caja.
            initialBoxes (List[int]): Cajas iniciales disponibles.
            expected_output (int): Número máximo esperado de dulces recolectados.
        """
        assert self.solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes) == expected_output
