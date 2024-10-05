import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (0, [0]),                 # Caso con n=0, solo tiene un valor en la lista que es 0
            (1, [0, 1]),              # Caso con n=1, contiene los bits de 0 y 1
            (2, [0, 1, 1]),           # Caso con n=2, la representación binaria de 2 tiene un 1
            (3, [0, 1, 1, 2]),        # Caso con n=3, la representación binaria de 3 tiene dos 1s
            (5, [0, 1, 1, 2, 1, 2]),  # Caso con n=5, se incluyen los resultados para números entre 0 y 5
            (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),  # Caso con n=10, resultado para varios valores
            (15, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]), # Caso con n=15, hasta valores binarios con 4 bits
        ]
    )
    def test_count_bits(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countBits.

        Args:
            n (int): Entero que representa el límite superior para generar la lista de bits.
            expected_output (List[int]): El resultado esperado.
        """
        assert self.solution.countBits(n) == expected_output
