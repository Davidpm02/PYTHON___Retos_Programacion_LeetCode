import pytest
from challenge import Solution  # Asegúrate de que el nombre del archivo donde resides la clase Solution sea "challenge.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("abc", 2),           # Ejemplo básico: |b - a| + |c - b| = 1 + 1 = 2
            ("a", 0),             # Cadena de un solo carácter, el score es 0
            ("", 0),              # Cadena vacía, el score es 0
            ("abcd", 6),          # Ejemplo más largo: |b - a| + |c - b| + |d - c| = 1 + 1 + 1 = 3
            ("aabbcc", 2),       # Cadena con caracteres repetidos: |a - a| + |b - b| + |c - c| = 0 + 0 + 0 = 0
            ("abcdef", 5),       # Ejemplo con una cadena en orden alfabético: |b - a| + |c - b| + |d - c| + |e - d| + |f - e| = 1 + 1 + 1 + 1 + 1 = 5
            ("zyx", 50),         # Cadena en orden inverso: |y - z| + |x - y| = 25 + 25 = 50
            ("aBc", 33)          # Ejemplo con caracteres en diferentes casos: |B - a| + |c - B| = 1 + 32 = 33
        ]
    )
    def test_score_of_string(self, input_str, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método scoreOfString.

        Args:
            input_str (str): La cadena de caracteres cuya puntuación se evaluará.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.scoreOfString(input_str) == expected_output
