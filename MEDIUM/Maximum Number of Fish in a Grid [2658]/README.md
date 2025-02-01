# Maximum Number of Fish in a Grid

## Descripción

El ejercicio "Maximum Number of Fish in a Grid" consiste en encontrar el máximo número de peces que un pescador puede capturar comenzando desde cualquier celda de agua en una cuadrícula 2D. La cuadrícula está representada por una matriz en la que las celdas de agua contienen un número de peces, y las celdas de tierra están representadas por ceros. El pescador puede moverse de una celda de agua a una celda adyacente y capturar los peces que contiene.

El objetivo es determinar la cantidad máxima de peces que se pueden capturar desde una celda inicial, donde las celdas adyacentes son aquellas que están en las posiciones arriba, abajo, izquierda y derecha.

## Implementación

La implementación se realiza en Python utilizando una clase llamada `Solution` que contiene el método `findMaxFish`. Este método recorre toda la cuadrícula y, para cada celda de agua, realiza una búsqueda en amplitud (BFS) para calcular el número total de peces en la región conectada de agua. Después de evaluar todas las celdas de agua, se devuelve el número máximo de peces que se pueden capturar.

### Detalles de la implementación

- **Búsqueda en amplitud (BFS):** Se utiliza una cola para recorrer todas las celdas conectadas de agua desde un punto de inicio y contar los peces presentes en esas celdas.
- **Marcado de celdas visitadas:** Las celdas de agua visitadas se marcan para evitar contar los peces más de una vez.
- **Direcciones de movimiento:** Las direcciones de movimiento se restringen a las celdas adyacentes (arriba, abajo, izquierda, derecha).

## Uso

Para utilizar este código, se debe proporcionar una matriz `grid` que represente la cuadrícula, luego crear una instancia de la clase `Solution` y llamar al método `findMaxFish` para obtener el resultado.

```python
if __name__ == "__main__":
    grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]

    sol = Solution()
    max_fish = sol.findMaxFish(grid)
    print(max_fish)  # Output: 7
```

## Conclusión

El ejercicio "Maximum Number of Fish in a Grid" presenta un desafío interesante que combina la búsqueda en amplitud con la manipulación de una cuadrícula 2D. La implementación es eficiente para el tamaño de la cuadrícula dado en las restricciones del problema (con un máximo de 10x10 celdas). El método findMaxFish resuelve el problema de manera óptima y aprovecha las propiedades de la BFS para explorar las regiones de agua de manera efectiva. Este tipo de problemas son útiles en escenarios de simulación de redes o exploración de espacios, y este enfoque proporciona una solución clara y concisa utilizando Python.
