import pytest
from challenge import Solution  # Se asume que el código del reto está en challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, roads, expected_output",
        [
            (7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]], 4),
            (2, [[1,0,10]], 1),
            (4, [[0,1,1],[1,2,1],[2,3,1],[0,2,2],[1,3,2]], 2),
            (5, [[0,1,2],[1,2,2],[2,3,2],[3,4,2],[0,4,8]], 1),
            (3, [[0,1,5],[1,2,5],[0,2,10]], 1),
        ]
    )
    def test_countPaths(self, n, roads, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countPaths.
        
        Args:
            n (int): Número de intersecciones en la ciudad.
            roads (List[List[int]]): Lista de carreteras con sus tiempos de viaje.
            expected_output (int): El número esperado de formas de llegar al destino en el menor tiempo.
        """
        assert self.solution.countPaths(n, roads) == expected_output
