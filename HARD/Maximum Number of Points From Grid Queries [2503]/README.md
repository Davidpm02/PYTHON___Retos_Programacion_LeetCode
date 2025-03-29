# Maximum Number of Points From Grid Queries

## Descripción

El ejercicio "Maximum Number of Points From Grid Queries" consiste en recorrer una matriz numérica siguiendo ciertas reglas y determinar el número máximo de puntos obtenidos para cada consulta en un array dado. Para cada consulta, partimos desde la celda superior izquierda de la matriz y seguimos estas reglas:

- Si el valor de la consulta es estrictamente mayor que el valor de la celda actual, obtenemos un punto (si es la primera vez que visitamos esa celda) y podemos movernos a cualquier celda adyacente en las direcciones arriba, abajo, izquierda o derecha.
- Si el valor de la consulta es menor o igual al valor de la celda actual, el proceso finaliza para esa consulta.

El objetivo es calcular cuántos puntos se pueden obtener para cada consulta en la lista de consultas proporcionada.

## Implementación

La implementación se realiza en Python utilizando una estrategia basada en un **Min-Heap** (cola de prioridad mínima) para expandir el recorrido de la matriz en orden creciente de valores. Se utiliza un conjunto para marcar las celdas visitadas y evitar procesarlas más de una vez.

### Detalles de la implementación

1. **Inicialización**:
   - Se almacena la matriz y la lista de consultas.
   - Se inicializa un Min-Heap con la celda superior izquierda de la matriz.
   - Se mantiene un conjunto de celdas visitadas.

2. **Procesamiento de consultas**:
   - Se ordenan las consultas en orden ascendente.
   - Se expande el recorrido de la matriz hasta que el valor mínimo en el heap sea mayor o igual al valor de la consulta actual.
   - Se cuentan los puntos obtenidos y se almacenan en la respuesta.

3. **Manejo del recorrido de la matriz**:
   - Se extraen celdas del heap y se expanden a sus vecinas si no han sido visitadas.
   - Se agregan al heap las nuevas celdas encontradas.
   - Se continúa hasta que no se pueda avanzar más.

## Uso

Para utilizar este código, se debe definir una matriz `grid` y una lista de consultas `queries`, y luego crear una instancia de la clase `Solution`. Se llama al método `maxPoints` con estos valores y se obtiene la lista de respuestas correspondiente.

```python
if __name__ == "__main__":
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]

    sol = Solution()
    result = sol.maxPoints(grid, queries)
    print(result)  # Output: [5, 8, 1]
```

## Conclusión

El ejercicio "Maximum Number of Points From Grid Queries" presenta un desafío interesante relacionado con la exploración de matrices y el uso eficiente de estructuras de datos como **colas de prioridad (Min-Heap)** para optimizar la búsqueda de celdas accesibles. La solución implementada aprovecha estas estructuras para garantizar una ejecución eficiente incluso con restricciones grandes. Este enfoque es especialmente útil en problemas que requieren un procesamiento ordenado y eficiente de datos en una estructura matricial.
