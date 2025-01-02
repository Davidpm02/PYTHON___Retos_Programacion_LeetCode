import pytest
import pandas as pd
from challenge import employee_bonus  # Importa la función desde el módulo correspondiente


class TestEmployeeBonus:
    def setup_method(self):
        """Método de configuración para crear los DataFrames antes de cada prueba."""
        
        # DataFrame de empleados
        self.employee = pd.DataFrame({
            'empId': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        })
        
        # DataFrame de bonos
        self.bonus = pd.DataFrame({
            'empId': [1, 2, 5],
            'bonus': [800, 1200, 950]
        })

    def test_employee_bonus_under_1000(self):
        """Prueba que verifica empleados con un bono menor a 1000 o sin bono."""
        
        expected_result = pd.DataFrame({
            'name': ['Alice', 'Charlie', 'David', 'Eve'],
            'bonus': [800, None, None, 950]
        })
        
        # Llamar a la función employee_bonus con los DataFrames de prueba
        result = employee_bonus(self.employee, self.bonus)
        
        # Verificar que el resultado es igual al esperado
        pd.testing.assert_frame_equal(result, expected_result)
    
    def test_no_employees_with_bonus(self):
        """Prueba que no haya empleados sin datos en el DataFrame de empleados ni de bonos."""
        
        # Modificar el DataFrame de empleados para que no haya datos
        empty_employee = pd.DataFrame(columns=['empId', 'name'])
        empty_bonus = pd.DataFrame(columns=['empId', 'bonus'])

        expected_result = pd.DataFrame(columns=['name', 'bonus'])

        # Llamar a la función con DataFrames vacíos
        result = employee_bonus(empty_employee, empty_bonus)
        
        # Verificar que el resultado es un DataFrame vacío
        pd.testing.assert_frame_equal(result, expected_result)
        
    def test_employees_with_no_bonus(self):
        """Prueba que verifica empleados que no tienen bono registrado."""
        
        # DataFrame de empleados (solo el nombre y el id)
        employees = pd.DataFrame({
            'empId': [1, 2, 3, 4, 6],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Frank']
        })
        
        # DataFrame de bonos
        bonuses = pd.DataFrame({
            'empId': [1, 2, 5],
            'bonus': [800, 1500, 950]
        })

        expected_result = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Frank'],
            'bonus': [800, 1500, None, None, None]
        })
        
        # Llamar a la función employee_bonus con los nuevos DataFrames
        result = employee_bonus(employees, bonuses)
        
        # Verificar que el resultado es igual al esperado
        pd.testing.assert_frame_equal(result, expected_result)
        
    def test_all_employees_get_bonus(self):
        """Prueba que verifica todos los empleados reciban su bono si es menor que 1000 o tienen un bono registrado."""
        
        # DataFrame con empleados
        all_employees = pd.DataFrame({
            'empId': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie']
        })
        
        # DataFrame con bonos
        all_bonuses = pd.DataFrame({
            'empId': [1, 2, 3],
            'bonus': [900, 1000, 1100]
        })

        expected_result = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie'],
            'bonus': [900, 1000, 1100]
        })
        
        # Llamar a la función employee_bonus con los nuevos DataFrames
        result = employee_bonus(all_employees, all_bonuses)
        
        # Verificar que el resultado es igual al esperado
        pd.testing.assert_frame_equal(result, expected_result)
