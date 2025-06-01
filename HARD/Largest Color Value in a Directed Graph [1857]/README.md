# Largest Color Value in a Directed Graph

## Descripción

El ejercicio "Largest Color Value in a Directed Graph" consiste en analizar un grafo dirigido cuyos nodos están coloreados, con el objetivo de encontrar el valor de color más alto entre todos los caminos válidos posibles. El valor de color de un camino se define como el número de veces que el color más frecuente aparece en dicho camino.

Una ruta válida en el grafo es una secuencia de nodos conectados por aristas dirigidas. Si el grafo contiene ciclos, no es posible calcular un valor válido, por lo que el resultado debe ser -1. Este tipo de problema es representativo de algoritmos que combinan teoría de grafos, detección de ciclos y programación dinámica.

## Implementación

La solución se implementa en Python mediante una clase `Solution`, que contiene el método `largestPathValue`. Este método aplica una combinación de técnicas de recorrido topológico, programación dinámica y manipulación de estructuras de datos para encontrar el valor de color más alto posible.

## Detalles de la implementación

- **Construcción del grafo:** Se utiliza una lista de adyacencia (`adj`) para representar las conexiones entre nodos y una lista `indegree` para contar las aristas entrantes a cada nodo.
- **Inicialización del DP:** Se crea una matriz `dp` de dimensiones `n x 26`, donde `n` es el número de nodos y `26` representa las letras del alfabeto. Cada celda `dp[i][c]` guarda la cantidad máxima del color `c` que puede obtenerse en un camino hasta el nodo `i`.
- **Recorrido topológico:** Se emplea una cola (`deque`) para realizar un recorrido topológico sobre los nodos con `indegree` cero, evitando así ciclos.
- **Propagación del DP:** A medida que se procesan los nodos, se actualizan los valores del DP para sus vecinos, considerando si el color del nodo actual coincide con el color del vecino.
- **Ciclo detectado:** Si el número de nodos procesados es menor al total, significa que existe un ciclo, y se devuelve -1.
- **Resultado final:** El valor máximo del DP a lo largo de todos los nodos representa la mayor cantidad de repeticiones de un color a lo largo de un camino válido.

## Uso

Para utilizar este código, se debe definir la cadena de colores de los nodos (`colors`) y la lista de aristas dirigidas (`edges`). Luego se crea una instancia de la clase `Solution` y se llama al método `largestPathValue`.

```python
if __name__ == "__main__":
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]

    sol = Solution()
    max_color_value = sol.largestPathValue(colors, edges)
    print(max_color_value)  # Output: 3
```

## Conclusión

El ejercicio "Largest Color Value in a Directed Graph" es un excelente ejemplo de cómo combinar técnicas de análisis de grafos con programación dinámica para resolver un problema complejo en estructuras dirigidas. Al tener en cuenta la frecuencia de colores en caminos y la detección de ciclos, se construye una solución eficiente y escalable incluso para grafos de gran tamaño. Este enfoque refuerza el entendimiento de recorridos topológicos, actualización de estados en DP y el manejo de estructuras de grafos en problemas del mundo real.
