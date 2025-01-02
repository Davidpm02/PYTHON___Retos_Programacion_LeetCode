import pytest
import pandas as pd
from challenge import sales_person  # Asegúrate de que tu archivo esté correctamente importado como challenge.py y la función sales_person esté definida allí.


class TestSalesPerson:
    @pytest.mark.parametrize(
        "sales_person_data, company_data, orders_data, expected_output_data",
        [
            (
                # Datos de ventas, compañías y pedidos
                pd.DataFrame({
                    'sales_id': [1, 2, 3],
                    'name': ['Alice', 'Bob', 'Charlie']
                }),
                pd.DataFrame({
                    'com_id': [1, 2],
                    'name': ['RED', 'BLUE']
                }),
                pd.DataFrame({
                    'order_id': [101, 102, 103],
                    'sales_id': [1, 2, 3],
                    'com_id': [1, 2, 2]
                }),
                # Esperado, nombre de todos los vendedores ajenos a la compañía RED
                pd.DataFrame({
                    'name': ['Bob', 'Charlie']
                })
            ),
            (
                # Caso en que todos los vendedores son de RED
                pd.DataFrame({
                    'sales_id': [1, 2],
                    'name': ['Alice', 'Bob']
                }),
                pd.DataFrame({
                    'com_id': [1],
                    'name': ['RED']
                }),
                pd.DataFrame({
                    'order_id': [101, 102],
                    'sales_id': [1, 2],
                    'com_id': [1, 1]
                }),
                # Esperado, no hay vendedores ajenos a RED
                pd.DataFrame({
                    'name': []
                })
            ),
            (
                # Caso en el que no existen pedidos a RED
                pd.DataFrame({
                    'sales_id': [1, 2, 3],
                    'name': ['Alice', 'Bob', 'Charlie']
                }),
                pd.DataFrame({
                    'com_id': [1, 2],
                    'name': ['RED', 'BLUE']
                }),
                pd.DataFrame({
                    'order_id': [101, 102, 103],
                    'sales_id': [1, 2, 3],
                    'com_id': [3, 4, 5]  # No hay pedidos a la compañía RED
                }),
                # Esperado, todos los vendedores porque no hubo pedidos a 'RED'
                pd.DataFrame({
                    'name': ['Alice', 'Bob', 'Charlie']
                })
            ),
            (
                # Caso sin registros de compañías
                pd.DataFrame({
                    'sales_id': [1, 2],
                    'name': ['Alice', 'Bob']
                }),
                pd.DataFrame({
                    'com_id': [],
                    'name': []
                }),
                pd.DataFrame({
                    'order_id': [101, 102],
                    'sales_id': [1, 2],
                    'com_id': [1, 1]
                }),
                # Esperado, todos los vendedores ya que no hay compañías registradas
                pd.DataFrame({
                    'name': ['Alice', 'Bob']
                })
            )
        ]
    )
    def test_sales_person(self, sales_person_data, company_data, orders_data, expected_output_data):
        """
        Prueba parametrizada para validar la función sales_person.

        Args:
            sales_person_data (pd.DataFrame): DataFrame con los datos de los vendedores.
            company_data (pd.DataFrame): DataFrame con los datos de las compañías.
            orders_data (pd.DataFrame): DataFrame con los datos de los pedidos.
            expected_output_data (pd.DataFrame): DataFrame con el resultado esperado.
        """
        result = sales_person(sales_person_data, company_data, orders_data)
        pd.testing.assert_frame_equal(result, expected_output_data)  # Compara los DataFrames generados
