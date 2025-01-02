import pytest
import pandas as pd
from challenge import swap_salary  # Asegúrate de importar correctamente la función desde tu reto

class TestSwapSalary:
    
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            # Caso con DataFrame donde se intercambian correctamente los sexos
            (
                pd.DataFrame({"sex": ["m", "f", "m", "f"]}), 
                pd.DataFrame({"sex": ["f", "m", "f", "m"]})
            ),
            # Caso con una sola fila, debe invertirse el valor 'm' a 'f'
            (
                pd.DataFrame({"sex": ["m"]}), 
                pd.DataFrame({"sex": ["f"]})
            ),
            # Caso con una sola fila, debe invertirse el valor 'f' a 'm'
            (
                pd.DataFrame({"sex": ["f"]}), 
                pd.DataFrame({"sex": ["m"]})
            ),
            # Caso con todas las filas siendo 'm', todas deben invertirse a 'f'
            (
                pd.DataFrame({"sex": ["m", "m", "m"]}), 
                pd.DataFrame({"sex": ["f", "f", "f"]})
            ),
            # Caso con todas las filas siendo 'f', todas deben invertirse a 'm'
            (
                pd.DataFrame({"sex": ["f", "f", "f"]}), 
                pd.DataFrame({"sex": ["m", "m", "m"]})
            ),
            # Caso con un DataFrame vacío, no debe cambiar nada
            (
                pd.DataFrame({"sex": []}),
                pd.DataFrame({"sex": []})
            ),
        ]
    )
    def test_swap_salary(self, input_data, expected_output):
        """
        Prueba parametrizada para validar la función swap_salary.
        
        Args:
            input_data (pd.DataFrame): El DataFrame de entrada con la columna 'sex'.
            expected_output (pd.DataFrame): El DataFrame esperado luego de aplicar la inversión de sexos.
        """
        result = swap_salary(input_data)
        pd.testing.assert_frame_equal(result, expected_output)
