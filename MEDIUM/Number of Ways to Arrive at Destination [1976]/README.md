# Number of Ways to Arrive at Destination

## Descripción

El ejercicio "Number of Ways to Arrive at Destination" consiste en determinar el número de formas en que se puede viajar desde la intersección 0 hasta la intersección n - 1 en la menor cantidad de tiempo posible. Para ello, se cuenta con una ciudad representada como un grafo no dirigido, donde los nodos son intersecciones y las aristas son carreteras con un tiempo de viaje asociado.

El objetivo es calcular cuántos caminos distintos permiten llegar a la intersección final en el menor tiempo posible. Dado que el resultado puede ser grande, se devuelve el resultado módulo 10^9 + 7.

## Implementación

La solución se implementa en Python utilizando un enfoque basado en el algoritmo de Dijkstra para encontrar la ruta más corta en grafos ponderados. Se emplea una estructura de cola de prioridad (heap) para gestionar la exploración eficiente de los caminos más óptimos.

### Detalles de la implementación

- **Construcción del grafo:** Se utiliza una lista de adyacencia para almacenar las conexiones entre intersecciones.
- **Inicialización de Dijkstra:** Se emplea una lista para registrar el tiempo mínimo necesario para llegar a cada nodo y otra para contar las formas de llegar a dicho nodo con dicho tiempo mínimo.
- **Exploración con heap:** Se procesa cada nodo expandiendo sus vecinos, actualizando el tiempo mínimo si se encuentra una mejor ruta y acumulando las formas de llegar en el menor tiempo posible.

## Uso

Para ejecutar el código, se debe proporcionar un número de intersecciones `n` y una lista de carreteras `roads`, donde cada elemento es una lista de tres valores `[ui, vi, timei]`, indicando una carretera bidireccional entre las intersecciones `ui` y `vi` con un tiempo de viaje `timei`.

```python
if __name__ == "__main__":
    n = 7
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    
    sol = Solution()
    result = sol.countPaths(n, roads)
    print(result)  # Output: 4
```

## Conclusión

El ejercicio "Number of Ways to Arrive at Destination" presenta una interesante aplicación de algoritmos de teoría de grafos en la búsqueda de caminos más cortos y la optimización de rutas. La solución implementada con Dijkstra y una cola de prioridad permite encontrar eficientemente la cantidad de formas en las que se puede alcanzar la meta en el menor tiempo posible. Esta técnica es ampliamente utilizada en problemas de navegación, redes y planificación de rutas óptimas en diversos dominios de la computación.
