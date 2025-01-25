# Find Eventual Safe States

## Descripción

El ejercicio "Find Eventual Safe States" consiste en determinar todos los nodos seguros de un grafo dirigido. Un nodo es considerado seguro si cualquier camino que inicie desde él conduce únicamente a nodos terminales o a otros nodos seguros. Un nodo es terminal si no tiene aristas salientes.

El objetivo del ejercicio es devolver una lista ordenada de nodos seguros.

## Implementación

La implementación utiliza un enfoque basado en la inversión del grafo original para facilitar la identificación de los nodos seguros:

1. **Construcción del grafo invertido:** Se invierten las direcciones de las aristas para facilitar el recorrido desde nodos terminales hacia sus predecesores.
2. **Identificación de nodos terminales:** Los nodos sin conexiones salientes se consideran terminales y se añaden a una cola para su procesamiento.
3. **Propagación hacia nodos seguros:** Mediante un recorrido en anchura (BFS), se procesan los nodos terminales y se actualizan los grados de salida de sus predecesores. Si un predecesor llega a tener un grado de salida de cero, se marca como seguro y se añade a la cola.
4. **Resultado:** Al finalizar, se devuelve una lista con todos los nodos seguros, ordenados de forma ascendente.

## Uso

Para utilizar este código, se debe definir el grafo como una lista de listas, donde cada nodo se encuentra asociado a un conjunto de nodos vecinos. Luego, se instancia la clase `Solution` y se llama al método `eventualSafeNodes`. Este método devuelve la lista de nodos seguros.

```python
if __name__ == "__main__":
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]

    sol = Solution()
    safe_nodes = sol.eventualSafeNodes(graph)
    print(safe_nodes)  # Output: [2, 4, 5, 6]
```

## Conclusión

El ejercicio "Find Eventual Safe States" presenta una solución eficiente para identificar nodos seguros en grafos dirigidos. Utiliza un enfoque de inversión de grafos combinado con BFS, lo que asegura que cada nodo se procese de manera lineal respecto al número total de nodos y aristas. Este enfoque es ideal para problemas relacionados con grafos dirigidos, ofreciendo una solución clara y eficiente que destaca en su aplicación práctica.
