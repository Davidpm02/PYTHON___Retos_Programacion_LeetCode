import pytest
from challenge import Solution  # Se importa la clase Solution desde challenge.py

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "tiles, expected_output",
        [
            ("AAB", 8),  # Ejemplo con repeticiones que generan menos combinaciones únicas
            ("ABC", 15), # Caso con letras distintas
            ("AA", 3),   # Solo tres posibilidades: "A", "AA", "A" (pero una sola vez)
            ("A", 1),    # Un único carácter solo puede generar una posibilidad
            ("AB", 4),   # "A", "B", "AB", "BA"
            ("AAA", 4),  # "A", "AA", "AAA"
            ("ABCD", 64), # Máximo número de combinaciones sin repetición
        ]
    )
    def test_num_tile_possibilities(self, tiles, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función numTilePossibilities.

        Args:
            tiles (str): La cadena de baldosas que se probará.
            expected_output (int): El número esperado de combinaciones únicas.
        """
        assert self.solution.numTilePossibilities(tiles) == expected_output