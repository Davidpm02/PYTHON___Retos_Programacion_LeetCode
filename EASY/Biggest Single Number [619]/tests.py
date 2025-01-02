import pytest
import pandas as pd
from challenge import biggest_single_number  # Importamos la función del reto

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar el DataFrame antes de cada prueba."""
        # Inicializamos un DataFrame de ejemplo con números para las pruebas.
        self.numbers_data = pd.DataFrame({
            "num": [1, 2, 2, 3, 4, 4, 5, 6, 6]
        })

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                pd.DataFrame({"num": [1, 2, 3, 4, 5]}),  # Todos los números con una sola aparición
                pd.DataFrame({"num": [5]})  # El número más grande con una sola aparición es 5
            ),
            (
                pd.DataFrame({"num": [2, 2, 3, 3, 4, 4]}),  # Números repetidos
                pd.DataFrame({"num": [None]})  # No hay números con una sola aparición
            ),
            (
                pd.DataFrame({"num": [5, 7, 9, 7, 6, 6]}),  # Números 5, 9, 7 y 6, 7 y 6 se repiten
                pd.DataFrame({"num": [9]})  # 9 es el único número con una sola aparición
            ),
            (
                pd.DataFrame({"num": [3, 3, 2, 2, 8]}),  # El 8 solo aparece una vez
                pd.DataFrame({"num": [8]})  # El número con una sola aparición es 8
            ),
            (
                pd.DataFrame({"num": [10, 10, 10, 10]}),  # Todos los números son iguales
                pd.DataFrame({"num": [None]})  # No hay ningún número con una sola aparición
            ),
        ]
    )
    def test_biggest_single_number(self, input_data, expected_output):
        """
        Prueba parametrizada para validar el funcionamiento de la función biggest_single_number.

        Args:
            input_data (pd.DataFrame): DataFrame con una columna de números.
            expected_output (pd.DataFrame): DataFrame esperado con el número de única aparición.
        """
        assert biggest_single_number(input_data).equals(expected_output)

