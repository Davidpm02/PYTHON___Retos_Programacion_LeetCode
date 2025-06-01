# Maximize the Number of Target Nodes After Connecting Trees I

## Descripción

El ejercicio **"Maximize the Number of Target Nodes After Connecting Trees I"** consiste en determinar, para cada nodo del primer árbol, cuántos nodos pueden ser alcanzados en total (incluyendo a sí mismo) si se conecta a un único nodo del segundo árbol mediante una arista adicional, bajo la condición de que la distancia entre dos nodos (en número de aristas) no supere un valor dado `k`.

Este problema se basa en conceptos fundamentales de teoría de grafos, como el recorrido por anchura (BFS), el cálculo de distancias y el análisis de componentes conexas. Es especialmente útil para afianzar conocimientos sobre árboles y optimización de búsqueda en estructuras no lineales.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método `maxTargetNodes`. Este método toma como entrada las aristas de dos árboles no dirigidos (`edges1` y `edges2`) y un entero `k` que define la distancia máxima para que un nodo sea considerado "target" de otro.

### Detalles de la implementación

- **Construcción de grafos:** A partir de las listas de aristas, se construyen listas de adyacencia para ambos árboles, representando sus respectivas conexiones.
- **Recorrido por BFS:** Para cada nodo, se ejecuta un recorrido en anchura (BFS) que permite contar cuántos nodos están a una distancia menor o igual a `k` (en el árbol 1) o `k - 1` (en el árbol 2, ya que una arista será usada para la conexión).
- **Optimización cruzada:** Se calcula, para cada nodo del primer árbol, la suma del número de nodos alcanzables desde sí mismo y el número máximo de nodos alcanzables desde cualquier nodo del segundo árbol, considerando que la nueva arista puede usarse estratégicamente.
- **Resultados individuales:** Se construye y devuelve una lista de enteros donde cada posición `i` representa el número máximo de nodos "target" para el nodo `i` del primer árbol.

## Uso

Para utilizar este código, simplemente se deben definir las listas de aristas `edges1` y `edges2`, junto con el valor de `k`. Luego, se crea una instancia de la clase `Solution` y se llama al método `maxTargetNodes` con los parámetros definidos.

```python
if __name__ == "__main__":
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    k = 2

    sol = Solution()
    result = sol.maxTargetNodes(edges1, edges2, k)
    print(result)  # Output: [9, 7, 9, 8, 8]
```

## Conclusión

El ejercicio "Maximize the Number of Target Nodes After Connecting Trees I" permite profundizar en el análisis de árboles y la propagación de información a través de conexiones estratégicas. La implementación propuesta utiliza técnicas clásicas como BFS y la manipulación de listas de adyacencia, demostrando cómo resolver problemas de propagación de estados o cobertura máxima en estructuras arborescentes.

Este enfoque tiene aplicaciones prácticas en diseño de redes, propagación de señales, y planificación de rutas óptimas, y es especialmente relevante en contextos donde una conexión extra puede marcar una diferencia significativa en la cobertura del sistema.
