import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected_output",
        [
            # Caso base con solo un servidor, no comunicado
            ([[1, 0], [0, 0]], 0),

            # Todos los servidores están comunicados por fila
            ([[1, 1], [0, 0]], 2),

            # Todos los servidores están comunicados por columna
            ([[1, 0], [1, 0]], 2),

            # Combinación de servidores comunicados por filas y columnas
            ([[1, 1], [1, 0]], 3),

            # Matriz sin servidores
            ([[0, 0], [0, 0]], 0),

            # Servidores no comunicados
            ([[1, 0], [0, 1]], 0),

            # Todos los servidores comunicados en una matriz grande
            ([  
                [1, 0, 1], 
                [0, 1, 0], 
                [1, 0, 1]
            ], 8),

            # Caso donde algunos servidores están aislados
            ([  
                [1, 1, 0], 
                [0, 1, 0], 
                [0, 0, 1]
            ], 3),

            # Servidores conectados en la misma fila y columna
            ([  
                [1, 1, 1], 
                [1, 0, 1], 
                [1, 1, 1]
            ], 12),
        ]
    )
    def test_count_servers(self, grid, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countServers.

        Args:
            grid (List[List[int]]): Matriz binaria representando los servidores.
            expected_output (int): Número esperado de servidores comunicados.
        """
        assert self.solution.countServers(grid) == expected_output
