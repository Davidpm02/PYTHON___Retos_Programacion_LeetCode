# Trapping Rain Water II

## Descripción

El ejercicio "Trapping Rain Water II" consiste en determinar la cantidad de agua que puede acumularse en un mapa de elevaciones bidimensional después de una lluvia. Cada celda de la matriz representa la altura del terreno en esa posición. El agua puede quedar atrapada en depresiones rodeadas por terrenos más altos, y la tarea es calcular el volumen total de agua acumulada.

Este problema es una extensión tridimensional del clásico problema de "Trapping Rain Water", donde en lugar de una sola dimensión, el agua se acumula en un área bidimensional con barreras en sus bordes.

## Implementación

La solución se implementa en Python utilizando una estructura de datos de cola de prioridad (min-heap) para procesar las celdas de menor altura primero y propagar la acumulación de agua de manera eficiente.

### Detalles de la implementación

- **Cola de prioridad (Min-Heap):** Se utiliza para procesar primero las celdas con menor altura, lo que permite calcular correctamente el nivel máximo de agua en cada punto.
- **Estructura de visitados:** Se emplea una matriz `visited` para asegurarse de que cada celda se procesa solo una vez y evitar cálculos innecesarios.
- **Bordes del mapa:** Se añaden todas las celdas de los bordes a la cola de prioridad, ya que estas establecen los límites del agua acumulada.
- **Procesamiento mediante BFS (Búsqueda en Anchura):** Se extrae la celda con menor altura de la cola, y se revisan sus vecinos. Si un vecino tiene una altura menor, el agua que puede acumularse allí es la diferencia entre la altura actual y la altura del vecino.
- **Actualización de la cola:** Se agregan los vecinos procesados a la cola con la altura máxima entre la celda actual y la nueva celda, garantizando que el agua fluya correctamente en el mapa.

## Uso

Para utilizar este código, se debe definir un `heightMap`, que es una matriz bidimensional que representa el terreno. Luego, se crea una instancia de la clase `Solution` y se llama al método `trapRainWater` con el `heightMap` como entrada.

```python
if __name__ == "__main__":
    heightMap = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    
    sol = Solution()
    trapped_water = sol.trapRainWater(heightMap)
    print(trapped_water)  # Output: 4
```

## Conclusión

El ejercicio "Trapping Rain Water II" proporciona una solución eficiente para calcular la cantidad de agua atrapada en un mapa de elevaciones bidimensional. La estrategia basada en una cola de prioridad permite procesar las celdas en orden óptimo, asegurando que el cálculo del volumen de agua sea preciso. Este enfoque es útil en aplicaciones relacionadas con modelado geográfico, simulaciones de inundaciones y problemas de optimización en gráficos. Además, refuerza conceptos clave de estructuras de datos avanzadas como heaps y algoritmos de búsqueda en anchura (BFS).
