"""
DESCRIPTION:

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.

 

Table: Bonus

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.

 

Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.
Return the result table in any order.
The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+


Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+


Output: 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+

"""

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
    """
    Se encarga de verificar todos los empleados que reciben un bonus inferior a 
    1000 o no reciben bonus, y retorna un DataFrame con los resultados.

    params:
        - employee (pd.DataFrame)
        - bonus (pd.DataFrame)
    
    returns:
        pd.DataFrame -- Dataframe obtenido como resultado.
    """

    # Filtrar empleados con bonus menor a 1000
    empId_less_than_1000 = bonus.loc[bonus["bonus"] < 1000, "empId"].values

    # Empleados que no tienen bonus registrados
    empId_without_bonus = employee.loc[~employee["empId"].isin(bonus["empId"]), "empId"].values

    # Combinar los IDs de empleados sin bonus y con bonus < 1000
    empId_less_1000_bonus = empId_less_than_1000.tolist()
    empId_less_1000_bonus.extend(empId_without_bonus)

    # Obtener nombres de empleados con bonus < 1000 o sin bonus
    names_employees_with_less_1000_bonus = employee.loc[employee["empId"].isin(empId_less_1000_bonus), "name"].values
    
    employees_and_bonus = []
    for empId in empId_less_1000_bonus:
        if empId in bonus["empId"].values:
            employee_name = employee.loc[employee["empId"] == empId, "name"].values
            employee_bonus = bonus.loc[bonus["empId"] == empId, "bonus"].values
        else:
            employee_name = employee.loc[employee["empId"] == empId, "name"].values
            employee_bonus = None
        
        employee_info = (employee_name[0], employee_bonus[0] if (employee_bonus is not None) else None)
        employees_and_bonus.append(employee_info)

    return pd.DataFrame(data=employees_and_bonus,
                        columns=["name", "bonus"])