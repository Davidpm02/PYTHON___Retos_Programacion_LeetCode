import pytest
import pandas as pd
from challenge import find_classes  # Importa la función find_classes desde el archivo principal


class TestFindClasses:
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                # Caso 1: Varias clases con asistentes suficientes
                pd.DataFrame({'class': ['Math', 'Math', 'Math', 'Math', 'Math', 
                                        'Science', 'Science', 'Science', 'Science', 
                                        'History', 'History']}),
                pd.DataFrame({'class': ['Math', 'Science']})  # Solo Math y Science tienen al menos 5 asistentes
            ),
            (
                # Caso 2: Ninguna clase tiene asistentes suficientes
                pd.DataFrame({'class': ['Math', 'Science', 'History']}),
                pd.DataFrame({'class': []})  # Resultado esperado es vacío
            ),
            (
                # Caso 3: Exactamente 5 asistentes en una clase
                pd.DataFrame({'class': ['Math', 'Math', 'Math', 'Math', 'Math', 
                                        'Science', 'Science', 'History']}),
                pd.DataFrame({'class': ['Math']})  # Solo Math cumple con el mínimo
            ),
            (
                # Caso 4: Todas las clases cumplen con el mínimo
                pd.DataFrame({'class': ['Math', 'Math', 'Math', 'Math', 'Math', 
                                        'Science', 'Science', 'Science', 'Science', 'Science']}),
                pd.DataFrame({'class': ['Math', 'Science']})  # Ambas clases tienen al menos 5 asistentes
            ),
            (
                # Caso 5: DataFrame vacío
                pd.DataFrame({'class': []}),
                pd.DataFrame({'class': []})  # Resultado esperado es vacío
            ),
        ]
    )
    def test_find_classes(self, input_data, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios de la función find_classes.

        Args:
            input_data (pd.DataFrame): DataFrame con la información de las clases.
            expected_output (pd.DataFrame): DataFrame esperado después del filtrado.
        """
        result = find_classes(input_data)
        # Compara DataFrames ignorando el índice
        pd.testing.assert_frame_equal(result.reset_index(drop=True), 
                                       expected_output.reset_index(drop=True))
