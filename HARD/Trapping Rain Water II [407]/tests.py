import pytest
from challenge import Solution  

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "heightMap, expected_output",
        [
            ([[1,1,1],[1,0,1],[1,1,1]], 1),  # Caso básico con un solo hueco central
            ([[3,3,3,3],[3,1,1,3],[3,1,1,3],[3,3,3,3]], 4),  # Pequeña piscina cerrada
            ([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]], 4),  # Mapa más grande con variaciones
            ([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12]], 14),  # Ejemplo con mayor profundidad
            ([[5,5,5,5],[5,1,1,5],[5,1,1,5],[5,5,5,5]], 16),  # Gran volumen de agua atrapada
            ([[5,5,5,5],[5,0,5,5],[5,5,5,5]], 5),  # Una única celda atrapando agua
            ([[3,3,3,3],[3,3,3,3],[3,3,3,3]], 0),  # Sin espacios para agua atrapada
            ([[1,2,3],[4,5,6],[7,8,9]], 0),  # Sin posibilidad de atrapamiento
        ]
    )
    def test_trap_rain_water(self, heightMap, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función trapRainWater.

        Args:
            heightMap (List[List[int]]): Matriz de alturas del terreno.
            expected_output (int): Cantidad esperada de agua atrapada.
        """
        assert self.solution.trapRainWater(heightMap) == expected_output
