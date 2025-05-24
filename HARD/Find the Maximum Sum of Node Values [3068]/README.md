# Find the Maximum Sum of Node Values

## Descripción

El ejercicio **"Find the Maximum Sum of Node Values"** plantea el desafío de encontrar la suma máxima posible de los valores de los nodos de un árbol no dirigido después de realizar operaciones XOR sobre sus aristas.

Se parte de un árbol con `n` nodos numerados del `0` al `n - 1`, donde cada nodo tiene un valor inicial representado en la lista `nums`. Además, se proporciona un valor entero `k`, y se permite realizar la operación XOR entre pares de nodos conectados directamente por una arista. Cada vez que se aplica la operación a una arista `[u, v]`, se actualizan ambos nodos con `nums[u] = nums[u] ^ k` y `nums[v] = nums[v] ^ k`.

El objetivo es determinar la máxima suma total posible de los valores de los nodos tras aplicar cualquier número (incluyendo cero) de estas operaciones.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `maximumValueSum`. Este método emplea programación dinámica sobre árboles (Tree DP) y se apoya en una búsqueda en profundidad (`DFS`) para recorrer y evaluar de manera eficiente el árbol completo.

## Detalles de la implementación

- **Construcción del grafo:** Se utiliza un diccionario de listas (`defaultdict`) para representar la estructura del árbol a partir de las aristas.
- **Cálculo de beneficios:** Para cada nodo, se calcula cuánto aumentaría su valor si se aplicara la operación XOR con `k`. Esta diferencia se denomina *beneficio*.
- **DP en árbol:** Se define una estructura `dp[node][parity]` donde:
  - `dp[node][0]` representa la suma máxima en el subárbol del nodo actual con un número **par** de operaciones XOR aplicadas.
  - `dp[node][1]` representa la suma máxima con un número **impar** de operaciones XOR.
- **DFS:** Se aplica un recorrido en profundidad desde la raíz del árbol (nodo 0), acumulando de forma óptima los resultados de cada subárbol, teniendo en cuenta las combinaciones de paridad de operaciones.

## Uso

Para utilizar este código, se deben definir las listas `nums`, `edges` y el entero `k`. Luego, se crea una instancia de la clase `Solution`, y se invoca el método `maximumValueSum` con los datos de entrada.

```python
if __name__ == "__main__":
    nums = [1, 2, 1]
    k = 3
    edges = [[0, 1], [0, 2]]

    sol = Solution()
    result = sol.maximumValueSum(nums, k, edges)
    print(result)  # Output: 6
```

## Conclusión

El ejercicio "Find the Maximum Sum of Node Values" explora una estrategia avanzada de optimización mediante operaciones XOR en árboles, lo cual es particularmente relevante en problemas donde se requiere transformar valores bajo ciertas reglas combinatorias.

La implementación propuesta destaca por aplicar técnicas de programación dinámica sobre grafos, que permiten calcular de forma eficiente el resultado óptimo sin necesidad de evaluar todas las posibles combinaciones de operaciones. Esto demuestra una aplicación práctica del Tree DP en contextos reales y optimización estructurada, siendo un ejemplo enriquecedor para el estudio de algoritmos avanzados en árboles y estructuras jerárquicas.
