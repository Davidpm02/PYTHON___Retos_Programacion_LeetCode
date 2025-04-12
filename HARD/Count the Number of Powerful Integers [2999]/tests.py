import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "start, finish, limit, s, expected_output",
        [
            (1, 100, 9, "123", 2),                  # Casos con un patrón pequeño y límite grande
            (1, 100, 9, "2", 10),                   # Casos con un solo dígito en el patrón
            (50, 100, 9, "5", 5),                   # Caso con un patrón de un solo dígito, limitado a números mayores
            (100, 200, 9, "99", 1),                 # Patrón de dígitos repetidos con límites en el rango
            (1, 1000, 9, "999", 1),                 # Casos con patrón repetido de 3 dígitos
            (10, 1000, 9, "555", 0),                # Sin resultados en el rango debido al patrón
            (1, 500, 5, "35", 3),                   # Rango medio, con dígitos limitados
            (1, 2000, 5, "100", 2),                 # Caso con patrón más grande
            (1, 1000, 9, "7", 100),                 # Casos donde el patrón es un solo dígito, y debe ser muy frecuente
            (1, 500, 9, "543", 0),                  # Caso con patrón poco frecuente
            (1, 1000, 5, "13", 10),                 # Otro patrón con números más pequeños
            (1, 100, 9, "12345", 0),                # Caso con un patrón más largo sin resultados en el rango
            (10, 300, 9, "3", 30),                  # Caso con un patrón muy frecuente de un solo dígito
        ]
    )
    def test_number_of_powerful_int(self, start, finish, limit, s, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función numberOfPowerfulInt.

        Args:
            start (int): El valor de inicio del rango.
            finish (int): El valor final del rango.
            limit (int): El límite máximo de los dígitos permitidos.
            s (str): El patrón de dígitos que debe terminar el número.
            expected_output (int): El número esperado de enteros poderosos en el rango.
        """
        assert self.solution.numberOfPowerfulInt(start, finish, limit, s) == expected_output
