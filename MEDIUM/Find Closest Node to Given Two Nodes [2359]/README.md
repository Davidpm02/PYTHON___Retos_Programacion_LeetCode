# First Closest Node to Given Two Nodes

## Descripción

El ejercicio **"First Closest Node to Given Two Nodes"** plantea un problema sobre grafos dirigidos en los que cada nodo tiene a lo sumo una arista saliente. Dados dos nodos de inicio (`node1` y `node2`), el objetivo es encontrar el índice del primer nodo que sea alcanzable desde ambos, minimizando el mayor de los caminos entre cada nodo de inicio y dicho nodo común.

Este tipo de problema es relevante en áreas como análisis de redes, planificación de rutas y propagación de información, donde resulta útil identificar puntos de encuentro óptimos a partir de múltiples orígenes.

## Implementación

La solución está implementada en Python mediante una clase `Solution`, que contiene el método `closestMeetingNode`. La lógica principal consiste en calcular las distancias desde ambos nodos iniciales a todos los demás, y luego seleccionar aquel nodo alcanzable por ambos cuya distancia máxima respecto a los nodos de origen sea la mínima posible.

### Detalles de la implementación

- **Cálculo de distancias:** Se realiza un recorrido a lo largo de los nodos a partir de cada nodo inicial usando un enfoque iterativo que detiene el recorrido al encontrar un nodo previamente visitado o una arista inexistente (`-1`). Las distancias se almacenan en listas separadas.
  
- **Selección del nodo óptimo:** Una vez conocidas las distancias desde ambos nodos, se analiza cada posición del grafo. Se considera únicamente aquel nodo que sea alcanzable desde los dos orígenes. Para cada uno de estos nodos, se calcula el máximo de las dos distancias. Se guarda aquel nodo que minimice este valor y, en caso de empate, el de menor índice.

- **Complejidad temporal:** La solución es eficiente y escala linealmente respecto al número de nodos del grafo (O(n)), lo cual es adecuado para las restricciones del problema (hasta 10⁵ nodos).

## Uso

Para utilizar este código, es necesario definir una lista `edges` que represente las aristas del grafo, junto con los enteros `node1` y `node2` como nodos de partida. Se debe crear una instancia de la clase `Solution` y llamar al método `closestMeetingNode`.

```python
if __name__ == "__main__":
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1

    sol = Solution()
    resultado = sol.closestMeetingNode(edges, node1, node2)
    print(resultado)  # Output: 2
```

## Conclusión

El ejercicio "First Closest Node to Given Two Nodes" permite explorar estrategias de búsqueda en grafos unidireccionales con restricciones, enfocándose en la eficiencia y el manejo de ciclos. Esta solución demuestra cómo, incluso en grafos con conexiones limitadas, es posible identificar nodos óptimos de convergencia entre múltiples caminos mediante un análisis dual de distancias. Se trata de un ejercicio valioso para reforzar conceptos como recorridos en grafos, control de ciclos y optimización de condiciones múltiples en estructuras de datos complejas.
