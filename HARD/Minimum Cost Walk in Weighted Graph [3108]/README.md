# Minimum Cost Walk in Weighted Graph

## Descripción

El ejercicio "Minimum Cost Walk in Weighted Graph" consiste en encontrar el costo mínimo de un recorrido en un grafo no dirigido y ponderado. El costo de un recorrido entre dos nodos se define como la operación AND bit a bit de los pesos de las aristas atravesadas en dicho recorrido.

Se proporciona un grafo con `n` vértices etiquetados de `0` a `n - 1` y una lista de aristas que conectan estos vértices con pesos asociados. Además, se da una lista de consultas donde cada consulta indica un par de vértices entre los cuales se desea conocer el costo mínimo de un recorrido.

Si existe un camino entre los dos vértices de la consulta, se devuelve el costo mínimo según la operación AND bit a bit de los pesos del recorrido; en caso contrario, se devuelve `-1`.

## Implementación

La solución se implementa en Python utilizando la estructura de datos **Disjoint Set Union (DSU)** o **Union-Find**, la cual permite agrupar vértices en componentes conexas y verificar si dos vértices pertenecen al mismo conjunto.

### Detalles de la implementación

- **Estructura DSU:** Se emplea un **Union-Find con compresión de caminos** y **uniones por rango** para optimizar las operaciones de agrupación y búsqueda de componentes.
- **Construcción del grafo:** Se procesan las aristas y se usa la estructura DSU para agrupar los vértices conectados en componentes conexas.
- **Cálculo del costo AND:** Para cada componente conexa, se calcula el AND bit a bit de los pesos de sus aristas.
- **Resolución de consultas:** Se verifica si los dos vértices de la consulta pertenecen al mismo componente conexo y, de ser así, se devuelve el costo AND calculado; en caso contrario, se devuelve `-1`.

## Uso

Para utilizar este código, se deben definir el número de vértices `n`, la lista de aristas `edges` y la lista de consultas `query`. Luego, se crea una instancia de la clase `Solution` y se llama al método `minimumCost` con estos valores.

```python
if __name__ == "__main__":
    n = 5
    edges = [[0,1,7],[1,3,7],[1,2,1]]
    query = [[0,3],[3,4]]
    
    sol = Solution()
    result = sol.minimumCost(n, edges, query)
    print(result)  # Output: [1, -1]
```

## Conclusión

El ejercicio "Minimum Cost Walk in Weighted Graph" presenta un problema clásico de análisis de grafos con una definición de costo basada en la operación AND bit a bit. La solución emplea la estructura **Disjoint Set Union (DSU)** para segmentar los vértices en componentes conexas, permitiendo una resolución eficiente de consultas.

Este enfoque es altamente eficiente en grafos grandes, ya que las operaciones de **find** y **union** están optimizadas mediante compresión de caminos y uniones por rango. Adicionalmente, el uso de estructuras de datos como diccionarios facilita el almacenamiento y acceso a la información relevante para cada componente.
