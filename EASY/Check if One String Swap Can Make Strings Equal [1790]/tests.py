import pytest
from challenge import Solution  # Importo la clase Solution desde el fichero del reto


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s1, s2, expected_output",
        [
            ("bank", "kanb", True),  # Se pueden intercambiar dos caracteres para ser iguales
            ("attack", "defend", False),  # No se pueden hacer iguales con un solo intercambio
            ("kelb", "kelb", True),  # Las cadenas ya son iguales
            ("abcd", "abdc", True),  # Intercambio válido de caracteres
            ("abcd", "abcd", True),  # Cadenas iguales
            ("abcd", "badc", False),  # Se requieren más de un intercambio
            ("aa", "aa", True),  # Cadenas idénticas
            ("abcd", "abce", False),  # Un solo cambio no es suficiente
            ("a", "a", True),  # Un solo carácter igual
            ("abc", "acb", True),  # Se intercambian dos caracteres
        ]
    )
    def test_are_almost_equal(self, s1, s2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función areAlmostEqual.

        Args:
            s1 (str): Primera cadena de entrada.
            s2 (str): Segunda cadena de entrada.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.areAlmostEqual(s1, s2) == expected_output
