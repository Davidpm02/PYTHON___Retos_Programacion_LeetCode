import pytest
from challenge import Solution  # Ajusta el import si el nombre del archivo es diferente.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "jewels, stones, expected_output",
        [
            ("aA", "aAAbbbb", 3),         # Joyas son 'aA' y las piedras son 'aAAbbbb' (2 'a' + 1 'A')
            ("z", "ZZ", 0),               # Joyas 'z' no están en las piedras 'ZZ'
            ("", "abc", 0),               # No hay joyas en el inventario de piedras
            ("abc", "aabbcc", 6),         # Las piedras contienen todas las joyas y deben ser contadas
            ("xYz", "xxXYyyyZZ", 5),      # Piedra contiene 2 'x', 2 'Y', y 1 'z' de las joyas dadas
            ("a", "abcabcabc", 3),        # Una joya 'a' en un inventario con 3 'a's
            ("ab", "babbab", 5),          # Las piedras contienen 2 'a' y 3 'b', todas las joyas son contabilizadas
        ]
    )
    def test_numJewelsInStones(self, jewels, stones, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función numJewelsInStones.

        Args:
            jewels (str): Las joyas que estamos buscando.
            stones (str): El inventario de piedras disponible.
            expected_output (int): El número esperado de joyas en las piedras.
        """
        assert self.solution.numJewelsInStones(jewels, stones) == expected_output
