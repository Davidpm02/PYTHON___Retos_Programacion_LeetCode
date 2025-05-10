# Find Minimum Time to Reach Last Room I

## Descripción

El ejercicio "Find Minimum Time to Reach Last Room I" consiste en calcular el tiempo mínimo necesario para atravesar una mazmorra representada como una cuadrícula bidimensional, desde la sala (0, 0) hasta la sala situada en la esquina inferior derecha (n - 1, m - 1). Cada celda de la cuadrícula tiene un tiempo mínimo `moveTime[i][j]` que indica cuándo se puede empezar a moverse hacia esa sala. El movimiento entre salas adyacentes (vertical u horizontalmente) toma exactamente un segundo. El objetivo es respetar estas restricciones temporales y determinar la ruta más rápida posible bajo dichas condiciones.

## Implementación

La solución se implementa en Python dentro de una clase llamada `Solution`, que contiene el método `minTimeToReach`. Este método utiliza una estrategia basada en búsqueda de caminos mínimos con una cola de prioridad (min-heap), lo que permite explorar las rutas de forma eficiente respetando las restricciones de tiempo.

## Detalles de la implementación

- **Inicialización:** Se determinan las dimensiones de la cuadrícula, y se crea una matriz `dist` para almacenar los tiempos mínimos conocidos hasta cada sala.
- **Direcciones válidas:** Se definen los movimientos permitidos (arriba, abajo, izquierda, derecha).
- **Cola de prioridad:** Se emplea una estructura `heap` para procesar las salas en orden de menor tiempo acumulado.
- **Lógica de movimiento:** Para cada movimiento posible, se calcula el tiempo más temprano en el que se puede iniciar el desplazamiento a la sala vecina, y se actualiza el tiempo de llegada si este resulta menor al registrado previamente.
- **Criterio de finalización:** El proceso se detiene en cuanto se alcanza la sala objetivo, devolviendo el tiempo mínimo registrado.

## Uso

Para utilizar este código, se debe definir una matriz `moveTime` con los tiempos mínimos de acceso a cada celda. Luego, se crea una instancia de la clase `Solution` y se invoca el método `minTimeToReach`, el cual devuelve el tiempo mínimo necesario para llegar a la última sala.

```python
if __name__ == "__main__":
    moveTime = [[0,4],[4,4]]

    sol = Solution()
    min_time = sol.minTimeToReach(moveTime)
    print(min_time)  # Output: 6
```

## Conclusión

El ejercicio "Find Minimum Time to Reach Last Room I" representa un problema típico de rutas mínimas con restricciones, muy común en entornos de planificación y navegación en grafos. La solución presentada hace uso de algoritmos clásicos como Dijkstra adaptado al contexto de restricciones temporales, utilizando una cola de prioridad para optimizar la búsqueda. Esta implementación permite resolver de forma eficiente cuadrículas de tamaño moderado respetando las condiciones impuestas en cada celda, y refuerza el entendimiento de técnicas avanzadas de recorrido y optimización en grafos.
