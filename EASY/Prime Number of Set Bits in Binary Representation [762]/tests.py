import pytest
from challenge import Solution  # Asegúrate de que el archivo se llame challenge.py y la clase Solution esté definida allí.

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "left, right, expected_output",
        [
            # Ejemplo simple
            (6, 10, 4),  # Los números 6 (110), 7 (111), 9 (1001), 10 (1010) tienen 2, 3, 2, 2 bits en '1'
            
            # Caso de un solo número
            (8, 8, 1),   # Solo el número 8 (1000) tiene 1 bit en '1' (no es primo)

            # Rango más grande
            (10, 15, 5),  # Los números del 10 al 15 tienen los siguientes bits en 1: 2, 3, 3, 3, 4, 2, que son primos 2, 3, 3, 3, 2.

            # Casos sin números primos en los bits de '1'
            (0, 0, 0),    # Solo tiene 1 bit en '1' (no es primo)

            # Números con cantidades pequeñas de bits en '1'
            (1, 5, 3),    # Los números 1, 2, 3, 4 y 5 tienen los siguientes bits: 1, 1, 2, 1, 2. Solo 2 (10) tiene número de bits primo (1)
            (0, 10, 6),   # Los números 0 a 10 tienen los siguientes bits en 1: 0, 1, 1, 2, 1, 2, 2, 3, 2, 3, 2 (prime counts: 1, 1, 3)
        ]
    )
    def test_count_prime_set_bits(self, left, right, expected_output):
        """
        Prueba parametrizada para validar la función countPrimeSetBits.

        Args:
            left (int): El límite inferior del rango.
            right (int): El límite superior del rango.
            expected_output (int): La cantidad esperada de números con un número primo de bits en su representación binaria.
        """
        assert self.solution.countPrimeSetBits(left, right) == expected_output
