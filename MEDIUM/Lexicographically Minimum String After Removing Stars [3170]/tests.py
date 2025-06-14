import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, expected_output",
        [
            ("ab*c", "ac"),                 # Elimina la 'b' más pequeña antes de '*'
            ("a*b*c", ""),                  # Cada '*' elimina el carácter más pequeño disponible
            ("abc**", "c"),                 # Dos '*' eliminan las dos letras más pequeñas
            ("", ""),                      # Cadena vacía, salida vacía
            ("****", ""),                  # Sólo '*', sin letras a eliminar
            ("abcd", "abcd"),              # Sin '*', no se elimina nada
            ("a*bc*def*", "df"),           # Eliminación progresiva de caracteres más pequeños
            ("zz*zz*zz*", "zzz"),          # Letras iguales, elimina las últimas añadidas
            ("a*b*c*d*e*f*g*", ""),        # Eliminación múltiple de letras simples
            ("ab*z*c*", "z"),              # Combinación con letras y '*' en posiciones mixtas
        ]
    )
    def test_clear_stars(self, input_str, expected_output):
        """
        Prueba parametrizada para validar distintos casos de la función clearStars.

        Args:
            input_str (str): Cadena de entrada con letras y posibles '*'.
            expected_output (str): Resultado esperado tras eliminar según reglas.
        """
        assert self.solution.clearStars(input_str) == expected_output
