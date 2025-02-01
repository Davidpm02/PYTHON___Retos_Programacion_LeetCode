# Divide Nodes Into the Maximum Number of Groups

## Descripción

El ejercicio "Divide Nodes Into the Maximum Number of Groups" consiste en dividir los nodos de un grafo no dirigido en el máximo número posible de grupos de manera que se cumplan las siguientes condiciones:

- Cada nodo pertenece a exactamente un grupo.
- Si dos nodos están conectados por una arista, entonces la diferencia entre sus índices de grupo debe ser exactamente 1.

Si no es posible realizar la agrupación cumpliendo estas condiciones, la función debe devolver `-1`.

## Implementación

La solución está implementada en Python dentro de la clase `Solution`, que contiene el método `magnificentSets`. Este método sigue los siguientes pasos:

- Construcción del grafo utilizando listas de adyacencia.
- Uso de BFS (Búsqueda en Anchura) para determinar si el grafo es bipartito y calcular la máxima profundidad de los grupos.
- Identificación de los componentes conexos del grafo.
- Cálculo del número máximo de grupos en los que se pueden dividir los nodos.
- Retorno del número total de grupos, o `-1` si no es posible agrupar los nodos según las reglas establecidas.

## Uso

Para ejecutar este código, simplemente se deben definir los valores de `n` y `edges`, y luego crear una instancia de la clase `Solution`. Se debe llamar al método `magnificentSets` con estos valores para obtener el resultado.

```python
if __name__ == "__main__":
    n = 6
    edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
    
    sol = Solution()
    max_groups = sol.magnificentSets(n, edges)
    print(max_groups)  # Output esperado: 4
```

## Conclusión

El ejercicio "Divide Nodes Into the Maximum Number of Groups" plantea un problema interesante de teoría de grafos, específicamente sobre particionamiento y bipartición. La implementación emplea BFS para evaluar la viabilidad de la división de nodos y calcular la máxima cantidad de grupos posibles.

El enfoque utilizado es eficiente para el rango de restricciones del problema y permite resolverlo en tiempo razonable. Sin embargo, en casos donde el grafo contiene ciclos impares, la solución devuelve `-1`, ya que no es posible cumplir con la condición de diferencias de grupo de exactamente 1.
