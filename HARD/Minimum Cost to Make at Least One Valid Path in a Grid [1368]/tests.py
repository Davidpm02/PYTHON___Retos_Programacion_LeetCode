import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "grid, expected_output",
        [
            # Caso básico donde el costo es 0 porque el camino es válido tal cual
            ([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]], 3), 
            
            # Caso donde la cuadrícula tiene un camino inicial válido sin modificar
            ([[1, 1, 3], [3, 2, 2], [1, 1, 4]], 0), 
            
            # Caso donde se necesita al menos un cambio para formar un camino válido
            ([[1, 2], [4, 3]], 1),
            
            # Caso de una cuadrícula mínima 1x1
            ([[1]], 0), 
            
            # Caso con un costo no trivial, donde varias señales necesitan modificación
            ([[1, 1, 1], [3, 2, 2], [3, 3, 4]], 2), 
            
            # Caso donde todas las señales inicialmente apuntan fuera y deben cambiarse
            ([[4, 4, 4], [4, 4, 4], [4, 4, 4]], 4), 
            
            # Caso de cuadrícula 5x5 con caminos complejos
            ([[1, 2, 1, 2, 1], [3, 4, 3, 4, 3], [2, 1, 2, 1, 2], [4, 3, 4, 3, 4], [1, 2, 1, 2, 1]], 7)
        ]
    )
    def test_min_cost(self, grid, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios de la función minCost.

        Args:
            grid (List[List[int]]): La cuadrícula de direcciones.
            expected_output (int): El resultado esperado del costo mínimo.
        """
        assert self.solution.minCost(grid) == expected_output
