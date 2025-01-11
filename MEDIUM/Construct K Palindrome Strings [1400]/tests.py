import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, k, expected_output",
        [
            ("annabelle", 2, True),   # Dos palíndromos posibles
            ("leetcode", 3, False),    # No es posible construir 3 palíndromos
            ("true", 4, True),         # Cada carácter en su propia subcadena
            ("aabbcc", 3, True),       # Se pueden crear 3 palíndromos
            ("abc", 3, False),         # Imposible crear 3 palíndromos con caracteres impares
            ("ab", 2, True),           # Dos palíndromos posibles ("a", "b")
            ("a", 1, True),            # Un solo carácter en una subcadena es siempre un palíndromo
            ("abcd", 2, False),        # No es posible dividir en 2 palíndromos
        ]
    )
    def test_can_construct(self, s, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función canConstruct.

        Args:
            s (str): La cadena que se utilizará para comprobar si es posible construir palíndromos.
            k (int): El número de palíndromos que se desea construir.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.canConstruct(s, k) == expected_output
