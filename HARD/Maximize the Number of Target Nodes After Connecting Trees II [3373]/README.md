# Maximize the Number of Target Nodes After Connecting Trees II

## Descripción

El ejercicio **"Maximize the Number of Target Nodes After Connecting Trees II"** consiste en analizar la estructura de dos árboles no dirigidos y calcular, para cada nodo del primer árbol, la máxima cantidad de nodos que podrían considerarse "target" tras conectar dicho nodo con cualquier nodo del segundo árbol.

Un nodo `u` es "target" de un nodo `v` si la distancia (número de aristas en el camino) entre `u` y `v` es **par**. Se incluye también el propio nodo, ya que la distancia de un nodo a sí mismo es 0 (par).

Dado que cada conexión entre un nodo del primer árbol y otro del segundo es independiente, se trata de un análisis que se repite para cada nodo del primer árbol de forma separada, evaluando la mejor posible conexión con el segundo árbol.

## Implementación

La implementación está desarrollada en Python, utilizando una clase `Solution` con el método principal `maxTargetNodes`. La solución sigue una lógica estructurada basada en teoría de grafos y se apoya en BFS para colorear los árboles de manera alterna (colores 0 y 1), como si se tratase de grafos bipartitos.

### Detalles de la implementación

- **Construcción de árboles:** A partir de las listas de aristas `edges1` y `edges2`, se generan listas de adyacencia para representar ambos árboles.
  
- **Coloreado y conteo bipartito:** Se realiza un recorrido BFS sobre cada árbol, asignando colores alternos a los nodos (0 o 1) según su profundidad. Esta coloración permite distinguir entre nodos que están a distancia par o impar entre sí. Durante este proceso, también se cuentan los nodos de cada color.

- **Optimización de conexión:** Se determina cuál color del segundo árbol aporta mayor cantidad de nodos "target" al conectar con un nodo del primer árbol. Esto se calcula en función del color del nodo del primer árbol que se analiza.

- **Resultado final:** Para cada nodo del primer árbol, se calcula cuántos nodos en total serían "target" al conectarse con un nodo óptimo del segundo árbol. Se suman los nodos "target" del primer árbol (de su mismo color) con el mejor grupo posible del segundo árbol (de color opuesto).

## Uso

Para utilizar este código, simplemente se deben definir las listas `edges1` y `edges2`, que representan las aristas de los dos árboles. Luego, se crea una instancia de la clase `Solution` y se llama al método `maxTargetNodes`.

```python
if __name__ == "__main__":
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

    sol = Solution()
    result = sol.maxTargetNodes(edges1, edges2)
    print(result)  # Output: [8,7,7,8,8]
```

## Conclusión

Este ejercicio destaca la importancia de los recorridos por grafos y el análisis de estructuras bipartitas para maximizar objetivos combinatorios. La clave está en entender que las distancias pares en un árbol están relacionadas con la paridad de las profundidades de los nodos.

La solución aprovecha que los árboles son inherentemente bipartitos para colorear nodos según su profundidad y utilizar esta coloración como herramienta para identificar eficientemente los "target nodes". El método propuesto es eficiente incluso para árboles de gran tamaño, gracias al uso de estructuras óptimas y BFS para la exploración de nodos.
