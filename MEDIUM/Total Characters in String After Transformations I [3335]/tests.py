import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_str, t, expected_output",
        [
            ("abc", 0, 3),              # Sin transformaciones, la longitud permanece igual
            ("z", 1, 2),                # 'z' -> 'ab'
            ("z", 2, 3),                # 'z' -> 'ab', luego 'a'->'b', 'b'->'c' → "bc" (longitud 2), total 3
            ("a", 1, 1),                # 'a' -> 'b'
            ("a", 2, 1),                # 'a' -> 'b' -> 'c'
            ("z", 3, 4),                # z -> ab -> bc -> cd
            ("xyz", 1, 3),              # 'x'->'y', 'y'->'z', 'z'->'ab' → "yza" + "b" → total 4
            ("zzz", 1, 6),              # Cada 'z' -> 'ab' → "ababab"
            ("abz", 2, 5),              # 'a'->'b'->'c', 'b'->'c'->'d', 'z'->'ab'->'bc' → total: 5
            ("", 10, 0),                # Cadena vacía permanece vacía sin importar las transformaciones
            ("z", 10, 89),              # Validación de crecimiento exponencial con transformaciones
        ]
    )
    def test_length_after_transformations(self, input_str, t, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método lengthAfterTransformations.

        Args:
            input_str (str): Cadena inicial.
            t (int): Número de transformaciones.
            expected_output (int): Longitud esperada tras aplicar las transformaciones.
        """
        assert self.solution.lengthAfterTransformations(input_str, t) == expected_output
