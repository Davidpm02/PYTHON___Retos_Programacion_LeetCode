import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "blocks, k, expected_output",
        [
            ("WBBWWBBWBW", 7, 3),  # Caso donde hay que cambiar 3 'W' para obtener 7 'B' consecutivos
            ("BBBBB", 5, 0),       # Todos los bloques ya son negros, no se requieren cambios
            ("WWWWW", 3, 3),       # Solo hay 'W', se deben cambiar 3 para formar 'BBB'
            ("BWBWBWB", 2, 1),     # Caso donde hay alternancia, mínimo 1 cambio para formar 2 'B' consecutivos
            ("WWBWWBWWBWW", 4, 2), # Se deben cambiar 2 'W' en la mejor sección
            ("BWBBWBB", 3, 0),     # Ya hay una secuencia de 3 'B' consecutivos
            ("WBWBWBW", 4, 2),     # Alternancia donde mínimo 2 cambios son necesarios
        ]
    )
    def test_minimum_recolors(self, blocks, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minimumRecolors.

        Args:
            blocks (str): Cadena con los bloques 'B' y 'W'.
            k (int): Número de bloques negros consecutivos requeridos.
            expected_output (int): Resultado esperado.
        """
        assert self.solution.minimumRecolors(blocks, k) == expected_output
