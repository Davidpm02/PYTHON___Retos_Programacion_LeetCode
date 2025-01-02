import pytest
from challenge import Solution  # Asegúrate de que tu archivo esté correctamente importado como challenge.py y la clase Solution esté definida allí.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, goal, expected_output",
        [
            ("abcde", "cdeab", True),               # Caso en el que una rotación convierte s en goal
            ("abcde", "abced", False),              # Caso en el que s no puede convertirse en goal
            ("", "", True),                         # Caso especial en el que ambas cadenas son vacías
            ("a", "a", True),                       # Caso en el que la cadena s es una sola letra y es igual a goal
            ("a", "b", False),                      # Caso en el que una sola letra no coincide
            ("abcdef", "defabc", True),             # Caso con una cadena más larga, con rotaciones válidas
            ("abcdef", "abcdef", True),             # Caso en el que s ya es igual a goal sin hacer ninguna rotación
            ("abcde", "edcba", False),              # Caso donde s no puede rotar para ser igual a goal (sin palindromos aquí)
            ("aabbcc", "bccaab", True),             # Caso de rotación con cadenas con caracteres repetidos
        ]
    )
    def test_rotateString(self, s, goal, expected_output):
        """
        Prueba parametrizada para verificar si la cadena 's' puede convertirse en 'goal'
        mediante rotaciones.

        Args:
            s (str): La cadena inicial.
            goal (str): La cadena objetivo después de un número de rotaciones.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.rotateString(s, goal) == expected_output
