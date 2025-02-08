import pytest
from challenge import Solution  # Importo la clase Solution desde el fichero del reto


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([3, 4, 5, 1, 2], True),  # Caso típico de rotación válida
            ([1, 2, 3, 4, 5], True),  # Lista ya ordenada
            ([2, 1, 3, 4, 5], False),  # No es una rotación válida
            ([1, 1, 1, 1, 1], True),  # Todos los elementos iguales
            ([5, 6, 7, 8, 9, 1, 2, 3, 4], True),  # Lista más grande con rotación válida
            ([6, 7, 8, 9, 10, 5], True),  # Rotación mínima
            ([4, 5, 6, 7, 1, 2, 3], True),  # Otro caso de rotación válida
            ([10, 1, 2, 3, 4, 5], True),  # Rotación en el primer elemento
            ([1, 3, 2, 4, 5], False),  # No sigue el patrón de rotación
            ([3, 2, 1], False),  # Descendente sin rotación válida
        ]
    )
    def test_check(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función check.

        Args:
            nums (List[int]): La lista de números a evaluar.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.check(nums) == expected_output
