import pytest
import pandas as pd
from challenge import find_customer_referee  # Asegúrate de ajustar el nombre del archivo que contiene la función


class TestFindCustomerReferee:
    def setup_method(self):
        """Método de configuración para crear el DataFrame de clientes antes de cada prueba."""
        
        # DataFrame de ejemplo de clientes
        self.customer = pd.DataFrame({
            'customer_id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'referee_id': [3, 2, 1, 1, 2]  # Las referencias son por customer_id
        })

    def test_find_customers_not_referred_by_id_2(self):
        """Prueba que verifica que se encuentren los clientes que no han sido referidos por el cliente con ID = 2."""
        
        # Se espera que Bob (ID = 2) y Eve (referido por ID = 2) sean excluidos.
        expected_result = pd.DataFrame({
            'name': ['Alice', 'Charlie', 'David']
        })
        
        # Llamamos a la función find_customer_referee con el DataFrame de clientes
        result = find_customer_referee(self.customer)
        
        # Verificamos que el resultado es igual al esperado
        pd.testing.assert_frame_equal(result, expected_result)

    def test_no_customers_in_df(self):
        """Prueba que verifica el comportamiento con un DataFrame de clientes vacío."""
        
        # DataFrame vacío de clientes
        empty_df = pd.DataFrame(columns=['customer_id', 'name', 'referee_id'])
        
        expected_result = pd.DataFrame(columns=['name'])  # Debe ser un DataFrame vacío
        result = find_customer_referee(empty_df)
        
        # Verificamos que el resultado es un DataFrame vacío
        pd.testing.assert_frame_equal(result, expected_result)

    def test_only_customers_referred_by_id_2(self):
        """Prueba que verifica que solo se excluyan los clientes referidos por el ID = 2."""
        
        # Todos los clientes son referidos por ID = 2, por lo que no se espera ningún cliente en el resultado.
        only_referred_by_2 = pd.DataFrame({
            'customer_id': [6, 7],
            'name': ['John', 'Jane'],
            'referee_id': [2, 2]
        })

        expected_result = pd.DataFrame(columns=['name'])  # Sin clientes en el resultado
        result = find_customer_referee(only_referred_by_2)

        # Verificamos que el resultado sea vacío
        pd.testing.assert_frame_equal(result, expected_result)

    def test_all_customers_are_excluded(self):
        """Prueba que verifica que no se devuelvan clientes si todos los clientes son referidos por ID = 2."""
        
        # Todos los clientes son referidos por ID = 2
        customers_all_referred_by_2 = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'referee_id': [2, 2, 2]
        })
        
        expected_result = pd.DataFrame(columns=['name'])  # No se espera ningún cliente
        result = find_customer_referee(customers_all_referred_by_2)
        
        # Verificamos que el resultado sea vacío
        pd.testing.assert_frame_equal(result, expected_result)

    def test_single_customer_not_referred_by_id_2(self):
        """Prueba que verifica que solo se devuelvan clientes no referidos por ID = 2."""
        
        # En este caso solo Alice no fue referida por ID = 2
        single_customer_df = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'referee_id': [3, 2, 1]
        })
        
        expected_result = pd.DataFrame({
            'name': ['Alice']
        })

        result = find_customer_referee(single_customer_df)
        
        # Verificamos que el resultado sea el esperado
        pd.testing.assert_frame_equal(result, expected_result)
