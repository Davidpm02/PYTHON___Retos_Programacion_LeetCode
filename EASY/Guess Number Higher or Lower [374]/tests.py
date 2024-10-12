import pytest
from challenge import Solution
from unittest.mock import patch

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, picked_number, expected_output",
        [
            (10, 6, 6),     # Número seleccionado es 6, el rango es 1-10
            (1, 1, 1),      # El único número posible es 1
            (100, 75, 75),  # El número seleccionado es 75, el rango es 1-100
            (50, 25, 25),   # El número seleccionado es 25, el rango es 1-50
            (10, 1, 1),     # El número seleccionado es 1, rango pequeño
        ]
    )
    @patch('challenge.guess')
    def test_guess_number(self, mock_guess, n, picked_number, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método guessNumber.

        Se utiliza un mock para la función guess().

        Args:
            n (int): El número máximo en el rango.
            picked_number (int): El número que se seleccionará como respuesta.
            expected_output (int): El número esperado como resultado.
        """
        def guess_mock(num):
            """Simula la función guess()"""
            if num < picked_number:
                return 1  # El número seleccionado es mayor
            elif num > picked_number:
                return -1  # El número seleccionado es menor
            else:
                return 0  # Número correcto
        
        # Mockear el comportamiento de guess() según el número seleccionado
        mock_guess.side_effect = guess_mock

        # Ejecutar la función a probar
        assert self.solution.guessNumber(n) == expected_output
