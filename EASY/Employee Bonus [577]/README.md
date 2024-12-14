# Employee Bonus

## Descripción

El ejercicio **"Employee Bonus"** tiene como objetivo identificar empleados cuyo bono sea menor a 1000 o que no tengan asignado un bono en absoluto. Este problema utiliza dos tablas: `Employee` y `Bonus`. La tabla `Employee` almacena información sobre los empleados, incluyendo su salario y su supervisor, mientras que la tabla `Bonus` detalla el monto del bono para ciertos empleados, utilizando la columna `empId` como clave primaria y referencia.

El resultado final es un reporte con el nombre y el bono de estos empleados, ordenados de cualquier manera.

### Ejemplo de entrada y salida:

#### Entrada
**Tabla Employee:**

| empId | name   | supervisor | salary |
|-------|--------|------------|--------|
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |

**Tabla Bonus:**

| empId | bonus |
|-------|-------|
| 2     | 500   |
| 4     | 2000  |

#### Salida

| name   | bonus |
|--------|-------|
| Brad   | null  |
| John   | null  |
| Dan    | 500   |

---

## Implementación

La solución a este problema se implementó utilizando **Python** y la biblioteca **pandas** para el procesamiento de las tablas `Employee` y `Bonus`.

### Pasos clave de la implementación:

1. **Filtrar empleados con bonos menores a 1000:**
   Utilizamos pandas para seleccionar los `empId` cuyos valores en la columna `bonus` sean inferiores a 1000.

2. **Identificar empleados sin bono:**
   Con el método `~isin()` de pandas, determinamos los empleados cuyo `empId` no aparece en la tabla `Bonus`.

3. **Combinar resultados:**
   Los `empId` obtenidos de los pasos anteriores se combinan en una lista única.

4. **Crear el resultado final:**
   Para cada `empId`, se recuperan el `name` y el `bonus` (o `null` si no tiene bono) y se formatea en un nuevo DataFrame.

### Código

```python
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """
    Verifica empleados con bonos menores a 1000 o sin bonos y retorna un DataFrame con los resultados.

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

    # Combinar IDs de empleados sin bonus y con bonus < 1000
    empId_less_1000_bonus = list(empId_less_than_1000) + list(empId_without_bonus)

    # Crear resultados finales
    employees_and_bonus = []
    for empId in empId_less_1000_bonus:
        employee_name = employee.loc[employee["empId"] == empId, "name"].values[0]
        employee_bonus = (bonus.loc[bonus["empId"] == empId, "bonus"].values[0]
                          if empId in bonus["empId"].values else None)
        employees_and_bonus.append((employee_name, employee_bonus))

    return pd.DataFrame(data=employees_and_bonus, columns=["name", "bonus"])
```

---

## Uso

Para utilizar esta solución, simplemente cargue las tablas `Employee` y `Bonus` en DataFrames de pandas y llame a la función `employee_bonus`.

### Ejemplo de uso

```python
import pandas as pd

# Crear DataFrame Employee
employee_data = {
    "empId": [3, 1, 2, 4],
    "name": ["Brad", "John", "Dan", "Thomas"],
    "supervisor": [None, 3, 3, 3],
    "salary": [4000, 1000, 2000, 4000]
}

employee = pd.DataFrame(employee_data)

# Crear DataFrame Bonus
bonus_data = {
    "empId": [2, 4],
    "bonus": [500, 2000]
}

bonus = pd.DataFrame(bonus_data)

# Llamar a la función
result = employee_bonus(employee, bonus)
print(result)
```

Salida esperada:

```bash
    name  bonus
0   Brad   None
1   John   None
2    Dan   500
```

---

## Conclusión

El ejercicio **"Employee Bonus"** es un excelente ejemplo de cómo aplicar transformaciones de datos con pandas para filtrar, combinar y analizar tablas relacionales. La implementación permite generar un reporte conciso de empleados que cumplen criterios específicos, mostrando la potencia de pandas para resolver problemas comunes en la manipulación de datos.
