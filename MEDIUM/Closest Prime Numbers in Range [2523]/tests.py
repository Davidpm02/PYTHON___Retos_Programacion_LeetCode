import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "left, right, expected_output",
        [
            (10, 30, [11, 13]),   # Primos más cercanos entre 10 y 30.
            (2, 10, [2, 3]),      # Primos más cercanos en el rango inicial.
            (14, 28, [17, 19]),   # Primos más cercanos en un rango sin primos consecutivos.
            (1, 2, [-1, -1]),     # No hay dos primos en el rango.
            (29, 41, [29, 31]),   # Primos consecutivos en el rango superior.
            (90, 100, [97, -1]),  # Solo un primo en el rango, sin pareja.
            (100, 200, [101, 103]), # Primos más cercanos en un rango mayor.
            (300, 400, [307, 311]), # Rango con primos dispersos.
        ]
    )
    def test_closest_primes(self, left, right, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función closestPrimes.

        Args:
            left (int): Límite inferior del rango de búsqueda.
            right (int): Límite superior del rango de búsqueda.
            expected_output (List[int]): Par de primos más cercanos o [-1, -1] si no existen.
        """
        assert self.solution.closestPrimes(left, right) == expected_output