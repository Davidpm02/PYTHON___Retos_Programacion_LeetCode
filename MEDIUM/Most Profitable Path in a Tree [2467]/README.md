# Most Profitable Path in a Tree

## Descripcion

El ejercicio "Most Profitable Path in a Tree" consiste en encontrar el camino hacia una hoja del árbol que maximice la ganancia neta de Alice. Se nos proporciona un árbol no dirigido con `n` nodos, donde cada nodo tiene una puerta con un costo o recompensa asociado. Alice comienza en la raíz del árbol (nodo 0) y se mueve hacia una hoja, mientras que Bob comienza en un nodo dado y se mueve hacia la raíz. Cuando ambos llegan simultáneamente a un nodo, comparten el costo o recompensa de su puerta. El objetivo es determinar la mayor ganancia neta que Alice puede obtener eligiendo su camino de manera óptima.

## Implementacion

La solución se implementa en Python utilizando una representación del árbol con listas de adyacencia y una combinación de DFS (búsqueda en profundidad) y BFS (búsqueda en anchura) para calcular los tiempos de llegada de Alice y Bob a cada nodo. Se emplean las siguientes estrategias:

- **Construcción del grafo:** Se usa un diccionario de listas para representar el árbol.
- **Cálculo de profundidad y padres:** Se usa un recorrido en profundidad (DFS) para determinar el padre y la profundidad de cada nodo.
- **Determinación del tiempo de llegada de Bob:** Se rastrea el camino de Bob desde su nodo inicial hasta la raíz.
- **Exploración de caminos y cálculo de ganancia:** Se usa un DFS desde la raíz para recorrer todos los caminos posibles y calcular la ganancia neta de Alice.

## Uso

Para utilizar este código, se debe definir la estructura del árbol, el nodo inicial de Bob y los valores de las puertas de cada nodo. Luego, se crea una instancia de la clase `Solution` y se llama al método `mostProfitablePath` con los parámetros correspondientes.

```python
if __name__ == "__main__":
    edges = [[0,1],[1,2],[1,3],[3,4]]
    bob = 3
    amount = [-2,4,2,-4,6]
    
    sol = Solution()
    max_profit = sol.mostProfitablePath(edges, bob, amount)
    print(max_profit)  # Salida esperada: 6
```

## Conclusion

El ejercicio "Most Profitable Path in a Tree" plantea un problema interesante de optimización en grafos, combinando aspectos de árboles, programación dinámica y recorridos DFS/BFS. La solución desarrollada aprovecha la eficiencia del DFS para explorar los caminos y determinar la ganancia máxima que Alice puede obtener, considerando el impacto del movimiento simultáneo de Bob. Este tipo de problema es relevante en la teoría de grafos y tiene aplicaciones en modelado de juegos y optimización de recursos.
