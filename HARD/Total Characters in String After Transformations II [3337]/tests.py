import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, t, nums, expected_output",
        [
            # Sin transformaciones, la longitud permanece igual
            ("abc", 0, [1]*26, 3),

            # Cada letra avanza 1 posición (nums[i] = 1), una transformación
            # a -> b, b -> c, c -> d → sigue siendo longitud 3
            ("abc", 1, [1]*26, 3),

            # Con wrap-around: 'z' + nums[z] = 1 -> a
            ("z", 1, [1]*26, 1),

            # Cada letra genera 2 nuevas letras por transformación (nums = 2)
            # Una transformación sobre 'a' → 'b','c'
            ("a", 1, [2]*26, 2),

            # Dos transformaciones sobre 'a' con nums=2 debería generar 4 letras
            ("a", 2, [2]*26, 4),

            # Con t=3 y nums todos a 2, la cantidad de letras crece exponencialmente
            ("a", 3, [2]*26, 8),

            # Casos con combinaciones más específicas de nums
            ("a", 2, [1 if i == 0 else 0 for i in range(26)], 1),  # Solo avanza 1 → 'a'->'b'->'c'

            # Cadena vacía debe seguir dando longitud 0
            ("", 5, [2]*26, 0),

            # Validación con múltiples caracteres y configuraciones variadas de nums
            ("abc", 2, [1]*26, 3),  # Simple avance de letras

            # Transformación sin expansión (nums = 0 para todo) → no cambia nada
            ("abc", 2, [0]*26, 0),
        ]
    )
    def test_length_after_transformations(self, s, t, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método lengthAfterTransformations.

        Args:
            s (str): Cadena inicial.
            t (int): Número de transformaciones.
            nums (List[int]): Reglas de transformación por carácter.
            expected_output (int): Longitud esperada tras aplicar las transformaciones.
        """
        assert self.solution.lengthAfterTransformations(s, t, nums) == expected_output
