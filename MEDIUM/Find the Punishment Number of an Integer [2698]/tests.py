import pytest
from challenge import Solution  # Importamos la clase Solution desde el archivo challenge.py

class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_n, expected_output",
        [
            (1, 1),   # Caso base más simple
            (2, 5),   # 1^2 + 2^2 = 1 + 4 = 5
            (10, 182), # Cálculo esperado con varios valores
            (20, 1256), # Prueba con más valores
            (30, 16630), # Caso con mayor n
            (50, 291941), # Número más grande para verificar estabilidad
        ]
    )
    def test_punishmentNumber(self, input_n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función punishmentNumber.

        Args:
            input_n (int): Número límite para calcular el punishment number.
            expected_output (int): El resultado esperado.
        """
        assert self.solution.punishmentNumber(input_n) == expected_output