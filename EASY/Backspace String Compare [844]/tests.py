import pytest
from challenge import Solution  # Asegúrate de que el archivo de la solución sea challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, t, expected_output",
        [
            ("ab#c", "ad#c", True),                  # Ambos se reducen a "ac", por lo que son iguales
            ("ab##", "c#d#", True),                  # Ambos se reducen a "", por lo que son iguales
            ("a#c", "b", False),                    # "a#c" se reduce a "c", pero "b" no es igual
            ("a##c", "#a#c", True),                  # Ambos se reducen a "c", por lo que son iguales
            ("xy#z", "xzz#", False),                # "xy#z" se reduce a "xz", y "xzz#" se reduce a "xz", lo que los hace diferentes
            ("##", "y#", False),                    # "##" se reduce a "" y "y#" se reduce a "y", diferentes
            ("abc#d", "abc#d", True),                # Ambos son exactamente iguales
            ("a###b", "b", True),                   # "a###b" se reduce a "b", que es igual a "b"
            ("p#q##", "q", True),                    # "p#q##" se reduce a "", y "q" se queda como "q", que es lo mismo
            ("#", "", True),                        # La cadena solo contiene un "#" por lo que se reduce a "", igual que ""
            ("xyz###", "", False),                  # "xyz###" se reduce a "", pero no coincide con "", pues no están vacías al mismo tiempo
        ]
    )
    def test_backspace_compare(self, s, t, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función backspaceCompare.

        Args:
            s (str): La primera cadena de texto que se comparará.
            t (str): La segunda cadena de texto que se comparará.
            expected_output (bool): El resultado esperado de la comparación.
        """
        assert self.solution.backspaceCompare(s, t) == expected_output
