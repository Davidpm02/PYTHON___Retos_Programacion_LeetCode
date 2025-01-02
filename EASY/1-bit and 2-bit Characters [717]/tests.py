import pytest
from challenge import Solution  # Asegúrate de que el archivo de la solución sea challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "bits, expected_output",
        [
            ([1, 0], True),                 # Ejemplo básico, 1 seguido de 0 debe devolver True
            ([1, 0, 0], False),             # Ejemplo donde el segundo último bit es 1, lo cual no es válido
            ([0], True),                    # Solo un bit, debe ser un carácter de un único bit
            ([1, 0, 1, 0], True),           # Validación con una secuencia intercalada de bits
            ([1, 1, 0], False),             # La secuencia termina en 0 pero es precedida por un bit 1
            ([0, 0, 1, 0, 0], True),        # Secuencia válida con 0, 0, 1, 0, 0, último bit es 0
            ([1, 1, 1, 0], True),           # La secuencia termina en un 0
            ([1, 1, 0, 0], False),          # El último 0 es precedido por más de un 1
            ([0, 0], True),                 # Secuencia con bits de valor 0 solo
            ([1, 0, 1, 1, 0], False)        # Termina en un bit 0, pero tiene un bit 1 antes de ello
        ]
    )
    def test_is_one_bit_character(self, bits, expected_output):
        """
        Prueba parametrizada para validar si el último carácter de la secuencia
        es un carácter de un único bit.

        Args:
            bits (List[int]): La secuencia de bits a comprobar.
            expected_output (bool): El resultado esperado.
        """
        assert self.solution.isOneBitCharacter(bits) == expected_output
