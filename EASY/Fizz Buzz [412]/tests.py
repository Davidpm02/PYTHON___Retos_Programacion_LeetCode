import pytest
from challenge import Solution  # Asumo que el código original está en el archivo challenge.py


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (1, ["1"]),                                 # Caso más pequeño posible
            (3, ["1", "2", "Fizz"]),                    # Caso donde aparece "Fizz"
            (5, ["1", "2", "Fizz", "4", "Buzz"]),       # Caso donde aparece "Buzz"
            (15, ["1", "2", "Fizz", "4", "Buzz",        # Caso donde aparece "FizzBuzz"
                  "Fizz", "7", "8", "Fizz", "Buzz", 
                  "11", "Fizz", "13", "14", "FizzBuzz"]),
            (0, []),                                    # Caso borde: n = 0 no genera elementos
        ]
    )
    def test_fizz_buzz(self, n, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función fizzBuzz.

        Args:
            n (int): El número de elementos a generar.
            expected_output (List[str]): El array esperado.
        """
        assert self.solution.fizzBuzz(n) == expected_output
