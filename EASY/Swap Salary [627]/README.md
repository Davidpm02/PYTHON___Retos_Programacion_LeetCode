# Swap Salaries

## Descripción

El ejercicio "Swap Salaries" consiste en realizar un intercambio de los valores de la columna 'sex' de una tabla de empleados, cambiando todos los valores 'f' por 'm' y viceversa. La tarea se debe realizar con una única sentencia de actualización, sin utilizar tablas temporales intermedias. Esta operación es útil en situaciones donde se necesita invertir rápidamente los valores de una columna categórica, sin la intervención de estructuras adicionales como variables auxiliares.

La tabla de entrada llamada `Salary` tiene la siguiente estructura:

| Column Name | Type     |
|-------------|----------|
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |

El objetivo es crear una solución que modifique la columna `sex`, cambiando todas las instancias de 'f' por 'm' y todas las de 'm' por 'f'.

## Implementación

La solución se implementa utilizando Python y la biblioteca Pandas, con la creación de la función `swap_salary`. Este método recibe un DataFrame que representa la tabla `Salary` y cambia los valores de la columna `sex` según sea necesario.

### Detalles de la implementación

- **Iteración sobre el DataFrame:** La función utiliza un ciclo `for` para recorrer las filas del DataFrame, verificando el valor de la columna `sex` en cada fila.
- **Condicional para realizar el intercambio:** Si el valor es 'f', se reemplaza por 'm'. Si el valor es 'm', se reemplaza por 'f'.
- **Modificación directa del DataFrame:** El valor de la columna 'sex' de cada fila se actualiza directamente utilizando el método `at`, que permite modificar el valor de una celda en particular en el DataFrame.

## Uso

Para utilizar este código, se debe proporcionar un DataFrame `salary` que contenga la información de los empleados, y luego invocar la función `swap_salary`.

```python
import pandas as pd

# Crear el DataFrame de ejemplo
salary_data = {
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'sex': ['m', 'f', 'm', 'f'],
    'salary': [2500, 1500, 5500, 500]
}
salary = pd.DataFrame(salary_data)

# Llamar a la función
swapped_salary = swap_salary(salary)

# Mostrar el DataFrame resultante
print(swapped_salary)
```

Este código creará un DataFrame con la información inicial, intercambiará los valores de la columna sex, y mostrará el resultado con los valores modificados.

## Conclusión

El ejercicio "Swap Salaries" proporciona una manera eficiente de intercambiar los valores de una columna categórica en un DataFrame sin necesidad de crear estructuras adicionales ni realizar operaciones complejas. Este tipo de manipulación de datos es fundamental en tareas de transformación de bases de datos, y la solución presentada utiliza las herramientas integradas de Pandas para realizarlo de manera sencilla. La implementación refuerza el concepto de manipulación de datos y provee una base útil para modificaciones rápidas de información dentro de tablas.
