import pytest
from challenge import Solution  # Asegúrate de que el archivo con la clase Solution se llame "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_list, expected_output",
        [
            ([1, 2, 3, 4], False),          # No hay duplicados
            ([1, 2, 3, 1], True),           # 1 está duplicado
            ([5, 5, 5, 5], True),           # Todos los elementos son duplicados
            ([0, 0, 0, 0], True),           # Duplicados de 0
            ([], False),                    # Lista vacía, no hay duplicados
            ([10, 20, 30, 40], False),      # Lista con valores únicos
            ([100, 200, 300, 100], True),   # 100 está duplicado
        ]
    )
    def test_contains_duplicate(self, input_list, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función containsDuplicate.

        Args:
            input_list (List[int]): La lista de enteros que se probará si contiene duplicados.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.containsDuplicate(input_list) == expected_output
