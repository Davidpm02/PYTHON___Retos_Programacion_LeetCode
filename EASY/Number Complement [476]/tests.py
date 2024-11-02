import pytest
from challenge import Solution  # Importa la clase Solution desde el módulo correspondiente

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            (5, 2),        # Ejemplo básico: 5 en binario es '101', su complemento es '010' -> 2
            (1, 0),        # El complemento de 1 ('1' en binario) es '0'
            (0, 1),        # Caso especial: el complemento de 0 ('0' en binario) es '1'
            (10, 5),       # 10 en binario es '1010', su complemento es '0101' -> 5
            (7, 0),        # 7 en binario es '111', su complemento es '000' -> 0
            (15, 0),       # 15 en binario es '1111', su complemento es '0000' -> 0
            (8, 7),        # 8 en binario es '1000', su complemento es '0111' -> 7
            (50, 13),      # 50 en binario es '110010', su complemento es '001101' -> 13
            (100, 27),     # 100 en binario es '1100100', su complemento es '0011011' -> 27
            (255, 0),      # 255 en binario es '11111111', su complemento es '00000000' -> 0
        ]
    )
    def test_find_complement(self, num, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findComplement.

        Args:
            num (int): El número entero cuyo complemento se probará.
            expected_output (int): El complemento esperado.
        """
        assert self.solution.findComplement(num) == expected_output
