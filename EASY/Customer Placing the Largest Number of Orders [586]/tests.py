import pytest
import pandas as pd
from challenge import largest_orders  # Importamos la función largest_orders

class TestSolution:
    @pytest.mark.parametrize(
        "orders, expected_output",
        [
            (pd.DataFrame(columns=['customer_number']),
             pd.DataFrame(data=[], columns=['customer_number'])),  # Caso sin órdenes, debe devolver un DataFrame vacío

            (pd.DataFrame({'customer_number': [1, 2, 3]}),
             pd.DataFrame(data=[1], columns=['customer_number'])),  # Un cliente con una orden, resultado debe ser el cliente con ID 1

            (pd.DataFrame({'customer_number': [1, 1, 2, 3]}),
             pd.DataFrame(data=[1], columns=['customer_number'])),  # Cliente 1 tiene dos órdenes, es el cliente con más órdenes

            (pd.DataFrame({'customer_number': [1, 2, 3, 2, 3, 1]}),
             pd.DataFrame(data=[1], columns=['customer_number'])),  # Cliente 1 tiene el mismo número de órdenes que 2 y 3 (dos cada uno),
                                                                   # pero aparece primero, por lo que se elige el primero

            (pd.DataFrame({'customer_number': [4, 4, 5, 5]}),
             pd.DataFrame(data=[4], columns=['customer_number'])),  # Cliente 4 y 5 tienen el mismo número de órdenes, pero 4 es primero

            (pd.DataFrame({'customer_number': [6, 6, 7, 8, 7, 8, 7]}),
             pd.DataFrame(data=[7], columns=['customer_number']))   # Cliente 7 tiene 3 órdenes, más que cualquier otro cliente
        ]
    )
    def test_largest_orders(self, orders, expected_output):
        """
        Prueba parametrizada para validar la función largest_orders.

        Args:
            orders (pd.DataFrame): El DataFrame de órdenes con los datos de clientes.
            expected_output (pd.DataFrame): El DataFrame esperado con el número de cliente con más órdenes.
        """
        assert largest_orders(orders).equals(expected_output)  # Comprobamos que la función retorna el DataFrame correcto
