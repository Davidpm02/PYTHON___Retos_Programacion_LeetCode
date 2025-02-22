import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            (["0"], "1"),  # Caso con un solo elemento "0"
            (["1"], "0"),  # Caso con un solo elemento "1"
            (["00", "01", "10"], "11"),  # Caso con todas las combinaciones excepto "11"
            (["11", "10", "00"], "01"),  # Caso con todas las combinaciones excepto "01"
            (["000", "001", "010", "011", "100", "101", "110"], "111"),  # Todos menos "111"
        ]
    )
    def test_find_different_binary_string(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findDifferentBinaryString.

        Args:
            nums (List[str]): Lista de cadenas binarias.
            expected_output (str): El resultado esperado que no está en nums.
        """
        assert self.solution.findDifferentBinaryString(nums) == expected_output
