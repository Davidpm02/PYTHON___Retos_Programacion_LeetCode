# Sales Person

## Descripción

El ejercicio "Sales Person" consiste en encontrar los nombres de todos los vendedores que no han tenido ningún pedido relacionado con la empresa llamada "RED". Utilizando tres tablas de bases de datos: `SalesPerson`, `Company`, y `Orders`, se realiza una consulta para obtener los resultados deseados. Este tipo de problema es común en aplicaciones que gestionan ventas o pedidos y requieren filtrar los vendedores según el cliente al que vendieron.

La tabla `SalesPerson` contiene información sobre los vendedores, la tabla `Company` proporciona detalles sobre las empresas, y la tabla `Orders` recoge la información de los pedidos realizados. El objetivo es seleccionar aquellos vendedores que no han tenido interacciones comerciales con la empresa "RED".

## Implementación

La solución se implementa utilizando el framework Pandas en Python. La función `sales_person` toma como entrada tres `DataFrames` (uno para cada una de las tablas mencionadas) y realiza los siguientes pasos:

1. Filtra la compañía "RED" para obtener su `com_id`.
2. Obtiene todos los `sales_id` asociados a la compañía "RED" en la tabla de pedidos (`Orders`).
3. Filtra los vendedores cuyos `sales_id` no están asociados a la compañía "RED".
4. Retorna un nuevo `DataFrame` con los nombres de los vendedores seleccionados.

Este enfoque es eficiente y fácil de seguir, y muestra el poder de Pandas para manipular y consultar bases de datos con datos tabulares.

## Uso

Para utilizar este código, es necesario tener los `DataFrames` que representen las tres tablas (`SalesPerson`, `Company`, `Orders`). La función `sales_person` se ejecuta pasando estos `DataFrames` como parámetros y devuelve un `DataFrame` con los nombres de los vendedores que no tienen pedidos asociados con "RED".

```python
import pandas as pd

# Cargar las tablas como DataFrames de Pandas
sales_person_df = pd.DataFrame({
    'sales_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
    'salary': [100000, 12000, 65000, 25000, 5000],
    'commission_rate': [6, 5, 12, 25, 10],
    'hire_date': ['2006-04-01', '2010-05-01', '2008-12-25', '2005-01-01', '2007-02-03']
})

company_df = pd.DataFrame({
    'com_id': [1, 2, 3, 4],
    'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
    'city': ['Boston', 'New York', 'Boston', 'Austin']
})

orders_df = pd.DataFrame({
    'order_id': [1, 2, 3, 4],
    'order_date': ['2014-01-01', '2014-02-01', '2014-03-01', '2014-04-01'],
    'com_id': [3, 4, 1, 1],
    'sales_id': [4, 5, 1, 4],
    'amount': [10000, 5000, 50000, 25000]
})

# Llamar a la función sales_person
result = sales_person(sales_person_df, company_df, orders_df)

# Mostrar el resultado
print(result)
```

## Conclusión

El ejercicio "Sales Person" es una excelente forma de entender cómo utilizar Pandas para realizar consultas y manipulaciones sobre datos tabulares. Al combinar varias tablas y aplicar filtros, es posible extraer resultados precisos según ciertos criterios, como en este caso, identificar a los vendedores que no han tenido ventas para la compañía "RED". Este tipo de consultas es común en sistemas de gestión de ventas y análisis de datos en el mundo real.

La solución proporciona una manera eficiente de filtrar grandes volúmenes de datos y obtener resultados valiosos para análisis posteriores. Además, refuerza los conocimientos sobre manipulación de datos en Pandas, una de las bibliotecas más importantes y potentes para el análisis de datos en Python.
