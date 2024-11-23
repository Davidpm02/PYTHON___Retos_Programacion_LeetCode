import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "word, expected_output",
        [
            ("USA", True),               # Todas las letras son mayúsculas (válido)
            ("leetcode", True),          # Todas las letras son minúsculas (válido)
            ("Google", True),            # Solo la primera letra es mayúscula (válido)
            ("FlaG", False),             # Uso incorrecto de mayúsculas
            ("Python", True),            # Primera letra mayúscula, resto minúsculas (válido)
            ("PYTHON", True),            # Todas mayúsculas (válido)
            ("python", True),            # Todas minúsculas (válido)
            ("PyThoN", False),           # Uso incorrecto de mayúsculas
            ("", True),                  # Cadena vacía (válida por defecto)
            ("a", True),                 # Una sola letra minúscula (válida)
            ("A", True),                 # Una sola letra mayúscula (válida)
        ]
    )
    def test_detect_capital_use(self, word, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función detectCapitalUse.

        Args:
            word (str): Palabra que se probará para validar el uso correcto de mayúsculas.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.detectCapitalUse(word) == expected_output
