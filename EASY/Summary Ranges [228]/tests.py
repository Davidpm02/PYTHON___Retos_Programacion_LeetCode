import pytest
from challenge import Solution  # Asegúrate de que el archivo donde resides la clase Solution sea "solution.py"

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),       # Ejemplo con múltiples rangos
            ([1, 2, 3], ["1->3"]),                               # Rango completo
            ([1], ["1"]),                                       # Solo un elemento
            ([], []),                                           # Lista vacía
            ([2, 3, 4], ["2->4"]),                             # Todos los elementos consecutivos
            ([5, 6, 8, 9, 10], ["5->6", "8->10"]),             # Rangos separados
            ([10, 11, 12, 15, 16, 20], ["10->12", "15->16", "20"]),  # Rango con interrupciones
            ([100, 101], ["100->101"]),                         # Dos elementos consecutivos
            ([100], ["100"]),                                   # Un solo número
            ([1, 3, 5, 7], ["1", "3", "5", "7"]),             # Sin rangos, solo elementos
        ]
    )
    def test_summary_ranges(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función summaryRanges.

        Args:
            nums (List[int]): La lista de enteros a ser procesada.
            expected_output (List[str]): La lista de rangos esperados.
        """
        assert self.solution.summaryRanges(nums) == expected_output
