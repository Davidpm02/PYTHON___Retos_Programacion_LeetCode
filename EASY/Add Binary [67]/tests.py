import pytest
from challenge import Solution  # Asegúrate de que el archivo de la solución sea challenge.py

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "a, b, expected_output",
        [
            ("11", "1", "100"),              # 3 (11) + 1 = 4 (100)
            ("1010", "1011", "10101"),       # 10 (1010) + 11 (1011) = 21 (10101)
            ("0", "0", "0"),                 # Suma de 0 + 0, debe devolver 0
            ("1101", "1011", "11000"),       # 13 (1101) + 11 (1011) = 24 (11000)
            ("1", "1", "10"),                # 1 + 1 = 2 (10)
            ("111", "1", "1000"),            # 7 (111) + 1 = 8 (1000)
            ("111111", "1", "1000000"),      # 63 (111111) + 1 = 64 (1000000)
            ("1001", "1100", "11001"),       # 9 (1001) + 12 (1100) = 21 (11001)
            ("101", "101", "1010"),          # 5 (101) + 5 (101) = 10 (1010)
            ("0", "101", "101"),             # 0 + 5 (101) = 5 (101)
        ]
    )
    def test_add_binary(self, a, b, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función addBinary.

        Args:
            a (str): La primera cadena binaria.
            b (str): La segunda cadena binaria.
            expected_output (str): El resultado esperado de la suma binaria.
        """
        assert self.solution.addBinary(a, b) == expected_output
