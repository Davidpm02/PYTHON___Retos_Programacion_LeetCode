import pytest
from challenge import Solution  # Ajusta el nombre del archivo o módulo según corresponda

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "widths, s, expected_output",
        [
            # Caso básico: cadena pequeña que cabe en una sola línea.
            ([10]*26, "abc", [1, 30]), # Todos los caracteres tienen el mismo ancho (10 px), cadena "abc" totaliza 30 px.

            # Caso donde una línea está llena justo a su capacidad (100 px).
            ([10]*25 + [5], "abcdefghijklmnopqrstuvwxyz", [2, 50]), # Primeros 25 caracteres llenan una línea, el último ocupa solo 5 px.

            # Caso donde la longitud de la cadena es menor a 100 px.
            ([10]*26, "abcdef", [1, 60]), # La cadena "abcdef" tiene 60 px (6*10) y cabría en una línea.

            # Caso donde varias líneas están involucradas.
            ([20]*26, "abcdefghijklmnopqrstuvwxyz", [5, 0]), # 5 líneas necesarias, cada línea tiene exactamente 20 px.

            # Caso con una cadena vacía, debería devolver [1, 0], ya que no se necesita más que una línea vacía.
            ([1]*26, "", [1, 0]),

            # Caso donde la cadena no cabe en una línea y requiere más de una.
            ([50]*26, "abcdefghijklmnopqrstuvwxyz", [3, 30]), # Solo 50 px por letra, "abcdefghij" se queda en 100 px (2 líneas), los demás llevan 1 línea adicional.

            # Caso con caracteres cuya suma exacta da justo 100 px.
            ([20]*5 + [10]*21, "abcdefghij"*2, [3, 100]), # Cadena repetida y ajustada a líneas de 100 px.

            # Caso con caracteres con la máxima amplitud posible (por ejemplo, cadenas que exceden con solo 1 carácter adicional).
            ([40]*5 + [30]*21, "abcdefghij"*2, [3, 60]), # Aumento del tamaño de cada letra en el ejemplo anterior (línea 3 tiene 60 px restantes).
        ]
    )
    def test_numberOfLines(self, widths, s, expected_output):
        """
        Prueba parametrizada para validar la función numberOfLines.
        
        Args:
            widths (List[int]): El ancho en píxeles para cada letra.
            s (str): La cadena que se va a procesar.
            expected_output (List[int]): El resultado esperado con [número de líneas, ancho de última línea].
        """
        result = self.solution.numberOfLines(widths, s)
        assert result == expected_output
