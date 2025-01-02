import pytest
from challenge import Solution  # Ajusta el import según el nombre de tu archivo.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, k, expected_output",
        [
            ("2-4A0r7-4k", 4, "24A0-R74K"),    # Caso típico con formato y letras
            ("2-4A0r7-4k", 3, "24-A0R-74K"),    # Caso con k igual a 3
            ("-A-", 1, "A"),                    # Caso con solo un guion y letras
            ("2-4a0r7-4k", 5, "24A0R-74K"),     # Con mezcla de letras mayúsculas y minúsculas
            ("abc-def-gh", 2, "AB-CD-EF-GH"),   # Separando por grupos de 2 caracteres
            ("abcd-efgh", 1, "A-B-C-D-E-F-G-H"),  # Caso con grupos de longitud 1
            ("aaaaaaaaaaa", 2, "AA-AA-AA-AA-AA"), # Sin guiones, solo caracteres
            ("", 3, ""),                        # Caso de cadena vacía
        ]
    )
    def test_license_key_formatting(self, input_str, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función licenseKeyFormatting.

        Args:
            input_str (str): La clave de licencia de entrada.
            k (int): La longitud máxima de los grupos.
            expected_output (str): La clave de licencia formateada esperada.
        """
        assert self.solution.lice
