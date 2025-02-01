# Course Schedule IV

## Descripción

El ejercicio "Course Schedule IV" consiste en determinar si un curso es un prerrequisito directo o indirecto de otro, dado un número total de cursos y una lista de prerrequisitos.

Se proporciona un número `numCourses` que representa la cantidad total de cursos etiquetados del `0` al `numCourses - 1`. También se proporciona una lista `prerequisites`, donde cada par `[ai, bi]` indica que el curso `ai` debe completarse antes que el curso `bi`. Además, se recibe una lista `queries`, en la que cada par `[uj, vj]` representa una consulta sobre si el curso `uj` es un prerrequisito de `vj`.

El objetivo es responder cada consulta con `true` si `uj` es un prerrequisito directo o indirecto de `vj`, y `false` en caso contrario.

## Implementación

La solución se implementa en Python utilizando el **algoritmo de Floyd-Warshall**, que permite calcular el cierre transitivo de un grafo dirigido.

### Detalles de la implementación

1. **Inicialización de la matriz de alcance transitivo:** Se crea una matriz `reachable` de tamaño `numCourses x numCourses`, donde cada celda `reachable[i][j]` es `True` si el curso `i` es un prerrequisito de `j`.
2. **Marcado de relaciones directas:** Se marcan los prerrequisitos directos proporcionados en la lista `prerequisites` dentro de la matriz.
3. **Aplicación del algoritmo de Floyd-Warshall:** Se analiza la transitividad de los prerrequisitos para determinar las relaciones indirectas.
4. **Procesamiento de consultas:** Se verifica la matriz `reachable` para cada consulta de la lista `queries` y se devuelve un resultado booleano.

## Uso

Para utilizar este código, simplemente se deben definir los valores de `numCourses`, `prerequisites` y `queries`. Luego, se crea una instancia de la clase `Solution` y se llama al método `checkIfPrerequisite` para obtener los resultados.

```python
if __name__ == "__main__":
    numCourses = 3
    prerequisites = [[1, 2], [1, 0], [2, 0]]
    queries = [[1, 0], [1, 2]]
    
    sol = Solution()
    result = sol.checkIfPrerequisite(numCourses, prerequisites, queries)
    print(result)  # Output: [True, True]
```

## Conclusión

El ejercicio "Course Schedule IV" permite modelar problemas de dependencias entre cursos y resolver consultas de prerrequisitos de manera eficiente. La solución implementada utiliza el algoritmo de Floyd-Warshall para calcular el cierre transitivo del grafo de prerrequisitos, asegurando que todas las relaciones directas e indirectas se consideren correctamente. Este enfoque es eficiente para conjuntos de datos moderados y proporciona una forma clara de resolver problemas de dependencias en estructuras dirigidas.
