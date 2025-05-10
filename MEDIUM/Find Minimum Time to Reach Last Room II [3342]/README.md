# Find Minimum Time to Reach Last Room II

## Descripción

El ejercicio **"Find Minimum Time to Reach Last Room II"** consiste en encontrar el tiempo mínimo requerido para moverse desde la esquina superior izquierda `(0, 0)` hasta la esquina inferior derecha `(n-1, m-1)` de una cuadrícula bidimensional que representa un calabozo. Cada celda en esta cuadrícula contiene una restricción temporal `moveTime[i][j]` que indica el tiempo más temprano en el que se puede comenzar a entrar en dicha celda.

Los movimientos permitidos son hacia celdas adyacentes en las direcciones cardinales (arriba, abajo, izquierda, derecha). El coste temporal de los movimientos se alterna: el primer movimiento cuesta 1 segundo, el siguiente 2 segundos, luego 1 segundo, y así sucesivamente. El objetivo es calcular el tiempo mínimo total necesario para llegar a la última celda cumpliendo con todas las restricciones temporales y de movimiento.

Este problema pone a prueba conceptos avanzados de algoritmos de grafos, planificación temporal, estructuras de datos como colas de prioridad, y la adaptación de algoritmos clásicos como Dijkstra a contextos con restricciones adicionales.

## Implementación

La implementación está escrita en Python utilizando programación orientada a objetos. Se define una clase `Solution` que contiene el método `minTimeToReach`. Este método aplica una variante del algoritmo de Dijkstra con un estado adicional: la **paridad del movimiento actual** (si el siguiente movimiento costará 1 o 2 segundos).

### Detalles de la implementación

- **Estructura de estado extendido:** Se mantiene una matriz tridimensional `dist[i][j][p]` para registrar el tiempo mínimo necesario para llegar a la celda `(i, j)` con paridad `p`, donde `p = 0` representa que el siguiente paso costará 1 segundo y `p = 1` que costará 2 segundos.
  
- **Cola de prioridad (`heapq`):** Se usa para explorar las celdas con menor tiempo acumulado primero, garantizando una expansión eficiente.

- **Restricción de tiempo mínima:** Para cada celda destino `(nx, ny)`, el algoritmo espera hasta que `moveTime[nx][ny]` sea alcanzable antes de moverse hacia ella.

- **Direcciones adyacentes:** El algoritmo considera movimientos hacia arriba, abajo, izquierda y derecha, siempre que se mantengan dentro de los límites de la cuadrícula.

- **Alternancia del coste de movimiento:** El tiempo del paso se determina por la paridad del paso actual y se alterna al avanzar en la ruta.

Este enfoque asegura que se consideren correctamente tanto las restricciones temporales como el patrón de coste alternante de los movimientos.

## Uso

Para utilizar este código, simplemente se debe instanciar la clase `Solution` y llamar al método `minTimeToReach`, pasando la matriz `moveTime` como argumento.

```python
if __name__ == "__main__":
    moveTime = [[0,4],[4,4]]
    
    sol = Solution()
    result = sol.minTimeToReach(moveTime)
    print(result)  # Output: 7
```

## Conclusión

El ejercicio "Find Minimum Time to Reach Last Room II" representa una interesante variación del algoritmo de caminos mínimos con restricciones temporales y patrones alternantes de coste. La solución propuesta se adapta eficazmente mediante el uso de un algoritmo de búsqueda con prioridad, manteniendo estados extendidos para capturar la dinámica del coste variable. Este enfoque no solo resuelve el problema de manera óptima, sino que también sirve como ejemplo práctico de cómo extender algoritmos clásicos para abordar desafíos más complejos en programación y teoría de grafos.
