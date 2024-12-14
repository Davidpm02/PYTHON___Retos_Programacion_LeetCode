# Find Customer Referee

## Descripción

Este ejercicio trabaja con una tabla SQL llamada `Customer` que tiene las siguientes columnas: 

- `id`: Identificador único del cliente (clave primaria).
- `name`: Nombre del cliente.
- `referee_id`: Identificador del cliente que los refirió.

El objetivo es encontrar los nombres de los clientes que **no han sido referidos** por el cliente con `id = 2`.

### Ejemplo de Entrada

Tabla `Customer`:

| id | name  | referee_id |
|----|-------|------------|
| 1  | Will  | null       |
| 2  | Jane  | null       |
| 3  | Alex  | 2          |
| 4  | Bill  | null       |
| 5  | Zack  | 1          |
| 6  | Mark  | 2          |

### Ejemplo de Salida

| name  |
|-------|
| Will  |
| Jane  |
| Bill  |
| Zack  |

En este caso, solo los clientes `Alex` y `Mark` han sido referidos por el cliente con `id = 2`, por lo que no aparecen en la salida.

---

## Implementación

La solución se desarrolla en Python utilizando la biblioteca **pandas** para procesar la tabla `Customer` como un `DataFrame`.

El enfoque es simple:
1. Seleccionamos todas las filas donde el `referee_id` no sea `2`, utilizando la función `loc` de pandas con una máscara lógica.
2. Retornamos únicamente la columna `name` con los nombres de los clientes seleccionados, formateándola en un nuevo `DataFrame`.

---

## Uso

El método se puede utilizar para analizar la tabla Customer de forma directa. Aquí tienes un ejemplo práctico:

```python
if __name__ == "__main__":
    # Creamos el DataFrame con datos de ejemplo
    data = {
        'id': [1, 2, 3, 4, 5, 6],
        'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
        'referee_id': [None, None, 2, None, 1, 2]
    }
    customer_df = pd.DataFrame(data)
    
    # Llamamos al método
    result = find_customer_referee(customer_df)
    
    # Mostramos el resultado
    print(result)
```

**Salida esperada:**

```bash
    name
0   Will
1   Jane
2   Bill
3   Zack
```

---

## Conclusión

El ejercicio "Find Customer Referee" destaca cómo trabajar con relaciones en tablas de datos y filtros lógicos para obtener información específica. La implementación en Python con pandas es eficiente, clara y fácilmente adaptable a conjuntos de datos más grandes. Este enfoque ilustra el poder de las herramientas de análisis de datos modernas, especialmente en tareas de filtrado y extracción en bases de datos tabulares.
