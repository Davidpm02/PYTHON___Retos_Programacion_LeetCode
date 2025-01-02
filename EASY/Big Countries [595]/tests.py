import pytest
import pandas as pd
from challenge import big_countries  # Importamos la función del reto


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar el DataFrame antes de cada prueba."""
        # Creamos un DataFrame de ejemplo para las pruebas.
        self.world_data = pd.DataFrame({
            "name": ["Country A", "Country B", "Country C", "Country D", "Country E"],
            "population": [50000000, 30000000, 4000000, 10000000, 150000000],
            "area": [2000000, 3000000, 10000000, 700000, 1800000]
        })

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                pd.DataFrame({
                    "name": ["Country A", "Country B", "Country C"],
                    "population": [50000000, 30000000, 4000000],
                    "area": [2000000, 3000000, 10000000]
                }),
                pd.DataFrame({
                    "name": ["Country A", "Country B", "Country C"],
                    "population": [50000000, 30000000, 4000000],
                    "area": [2000000, 3000000, 10000000]
                })[["name", "population", "area"]]  # Esperamos los tres países
            ),
            (
                pd.DataFrame({
                    "name": ["Country D", "Country E"],
                    "population": [10000000, 150000000],
                    "area": [700000, 1800000]
                }),
                pd.DataFrame({
                    "name": ["Country E"],
                    "population": [150000000],
                    "area": [1800000]
                })[["name", "population", "area"]]  # Solo Country E tiene una población grande
            ),
            (
                pd.DataFrame({
                    "name": ["Country F", "Country G"],
                    "population": [25000000, 10000000],
                    "area": [3500000, 4000000]
                }),
                pd.DataFrame({
                    "name": ["Country F", "Country G"],
                    "population": [25000000, 10000000],
                    "area": [3500000, 4000000]
                })[["name", "population", "area"]]  # Ambos países son grandes por su área
            ),
        ]
    )
    def test_big_countries(self, input_data, expected_output):
        """
        Prueba parametrizada para validar el funcionamiento de la función big_countries.

        Args:
            input_data (pd.DataFrame): Un DataFrame con los datos de varios países.
            expected_output (pd.DataFrame): El DataFrame esperado con los países grandes.
        """
        assert big_countries(input_data).equals(expected_output)

