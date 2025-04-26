import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, 1),        # Caso mínimo, solo el número 1
            (5, 2),        # Grupos con la mayor cantidad de números (1, 2, 3, 4, 5)
            (10, 2),       # 10 números, varios grupos con la misma cantidad
            (20, 3),       # Rango más grande, múltiples grupos
            (100, 4),      # Rango aún más grande
            (50, 4),       # Con 50 números, verificamos cuántos grupos tienen la mayor cantidad
            (15, 2),       # 15 números, cómo se agrupan en base a la suma de dígitos
            (99, 4),       # Caso con 99 números
        ]
    )
    def test_count_largest_group(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countLargestGroup.

        Args:
            n (int): El número hasta el cual se agruparán los números en base a la suma de sus dígitos.
            expected_output (int): El número esperado de grupos con la mayor longitud.
        """
        assert self.solution.countLargestGroup(n) == expected_output
