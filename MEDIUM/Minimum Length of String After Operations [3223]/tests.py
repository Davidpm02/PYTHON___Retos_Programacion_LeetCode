import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected_output",
        [
            ("abcabc", 6),  # La cadena no tiene caracteres repetidos, debe retornar el tamaño completo.
            ("aabbcc", 6),   # Los caracteres no se repiten 3 veces, tamaño completo también.
            ("aaabbbccc", 5), # Los caracteres que aparecen 3 veces son eliminados parcialmente, queda "aabbb"
            ("zzz", 2),      # El string está compuesto sólo por "zzz", queda "zz".
            ("zzzzzzz", 5),  # Después de eliminar "zzz", queda "zz" (tamaño 2 en total, porque se eliminan todas las "zzz").
            ("abcd", 4),     # Todos los caracteres son distintos, debe devolver la longitud total.
            ("xxxyyyzz", 3), # Si todos los caracteres se repiten 3 veces, la longitud obtenida debería ser 3.
            ("aaaaaabbbbbccccc", 10),  # Al eliminar de manera repetida los caracteres más frecuentes "a", "b", "c", la cadena reducirá su tamaño
            ("", 0),         # Cadena vacía, salida es 0.
            ("abccba", 6),   # No hay caracteres repetidos 3 veces, debe devolver tamaño completo.
        ]
    )
    def test_minimum_length(self, s, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minimumLength.

        Args:
            s (str): La cadena que será procesada.
            expected_output (int): La longitud esperada después de realizar los procedimientos de eliminación.
        """
        assert self.solution.minimumLength(s) == expected_output
