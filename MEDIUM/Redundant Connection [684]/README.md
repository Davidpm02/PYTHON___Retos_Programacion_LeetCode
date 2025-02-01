# Redundant Connection

## Descripción

El ejercicio "Redundant Connection" consiste en identificar una arista redundante en un grafo que originalmente era un árbol, pero al que se le ha agregado una arista adicional que forma un ciclo. Dado un conjunto de aristas que representan un grafo con `n` nodos, donde cada arista conecta dos nodos, el objetivo es encontrar la arista adicional que, al eliminarla, el grafo se convierta nuevamente en un árbol.

Un árbol es un grafo no dirigido y conexo que no tiene ciclos, mientras que la adición de una arista puede generar un ciclo. El reto es identificar cuál de las aristas adicionales puede ser eliminada para restaurar la propiedad de árbol en el grafo.

## Implementación

La implementación se realiza en Python utilizando un enfoque basado en el "Disjoint Set Union" (DSU), también conocido como "Union-Find". Este enfoque permite manejar eficientemente los conjuntos disjuntos de nodos para detectar si agregar una arista forma un ciclo en el grafo.

### Detalles de la implementación

- **DSU (Disjoint Set Union):** Se utiliza para representar los conjuntos disjuntos de nodos, facilitando la verificación de si dos nodos están en el mismo conjunto o no.
- **Compresión de ruta y unión por rango:** Para optimizar el rendimiento, se emplea compresión de ruta (para encontrar el líder de un conjunto rápidamente) y unión por rango (para mantener los árboles equilibrados).
- **Procesamiento de las aristas:** Se recorre cada arista y se intenta unir los nodos correspondientes. Si los nodos ya están conectados, significa que la arista actual forma un ciclo, y esta es la arista redundante.

## Uso

Para utilizar este código, se debe proporcionar una lista de aristas `edges` que representan el grafo con una arista adicional. Luego, se crea una instancia de la clase `Solution` y se llama al método `findRedundantConnection` para obtener la arista redundante.

```python
if __name__ == "__main__":
    edges = [[1,2],[1,3],[2,3]]

    sol = Solution()
    redundant_edge = sol.findRedundantConnection(edges)
    print(redundant_edge)  # Output: [2, 3]
```

## Conclusión

El ejercicio "Redundant Connection" presenta una excelente oportunidad para aplicar estructuras de datos eficientes, como el "Disjoint Set Union", en la resolución de problemas relacionados con grafos. El enfoque implementado permite identificar rápidamente la arista redundante utilizando técnicas como la compresión de ruta y la unión por rango, lo que hace que la solución sea tanto eficiente como escalable para grafos grandes. Este tipo de problemas es común en la teoría de grafos y la detección de ciclos en grafos no dirigidos, y el método propuesto proporciona una forma clara y eficiente de abordar el problema.
