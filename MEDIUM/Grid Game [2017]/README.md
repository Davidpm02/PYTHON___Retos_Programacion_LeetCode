# Grid Game

## Descripción

El ejercicio **Grid Game** involucra a dos robots que deben atravesar una matriz 2D de tamaño `2 x n`. Esta matriz representa puntos que pueden recolectar en cada celda. Ambos robots comienzan en `(0, 0)` y deben llegar a `(1, n-1)`, pero con objetivos distintos:

- El primer robot intenta minimizar los puntos que el segundo robot pueda recolectar.
- El segundo robot intenta maximizar su puntaje.

Ambos robots se desplazan de manera óptima, y los caminos permitidos incluyen movimientos hacia la derecha `(r, c) → (r, c+1)` o hacia abajo `(r, c) → (r+1, c)`. El reto consiste en calcular cuántos puntos puede recolectar el segundo robot, suponiendo que ambos juegan de forma óptima.

## Implementación

La solución se implementa en Python en la clase `Solution`, que contiene el método `gridGame`. Este método sigue el siguiente enfoque:

1. **Sumas acumulativas:** Se calculan las sumas acumuladas de ambas filas de la matriz para evaluar rápidamente las elecciones de caminos.
2. **Análisis de cortes:** Se simula un corte en cada columna, evaluando los puntos que quedarían disponibles para el segundo robot si el primer robot escogió cortar en esa columna.
3. **Minimizar el máximo:** Se determina el mínimo de los puntos máximos disponibles para el segundo robot a través de todos los cortes posibles.

El método está diseñado para manejar matrices de tamaño grande de manera eficiente, cumpliendo con las restricciones del problema.

## Uso

Para utilizar el código, basta con inicializar una instancia de la clase `Solution` y llamar al método `gridGame` con una matriz `grid` de tamaño `2 x n` como entrada.

```python
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        """
        Calcula los puntos recolectados por el segundo robot dado un grid 2xN.
        Ambos robots juegan de manera óptima.
        
        params:
            grid List[List[int]] - matriz de puntos de tamaño 2xN
        
        returns:
            int
        """
        
        n = len(grid[0])
        
        # Crear acumulados para cada fila (filas 0 y 1)
        top_prefix_sum = [0] * n
        bottom_prefix_sum = [0] * n
        
        # Llenar los acumulados de la fila superior (0) y la inferior (1)
        for i in range(n):
            top_prefix_sum[i] = top_prefix_sum[i - 1] + grid[0][i] if i > 0 else grid[0][i]
            bottom_prefix_sum[i] = bottom_prefix_sum[i - 1] + grid[1][i] if i > 0 else grid[1][i]

        # Inicializar el mínimo del máximo de puntos que el segundo robot puede tomar
        min_points = float('inf')

        for i in range(n):
            # Puntos disponibles si el primer robot corta en la columna i
            points_top = top_prefix_sum[n - 1] - top_prefix_sum[i]
            points_bottom = bottom_prefix_sum[i - 1] if i > 0 else 0
            
            # El segundo robot tomará el máximo de los dos caminos disponibles
            second_robot_points = max(points_top, points_bottom)
            
            # Actualizar el mínimo
            min_points = min(min_points, second_robot_points)

        return min_points
```

## Conclusión

El ejercicio **Grid Game** representa un problema interesante de optimización con restricciones, donde dos agentes interactúan en un entorno competitivo. La solución propuesta utiliza sumas acumulativas para evaluar de manera eficiente todas las posibles estrategias. Este enfoque garantiza una ejecución óptima incluso para los tamaños máximos permitidos por las restricciones del problema. Esta implementación también enfatiza conceptos clave como la evaluación de estrategias competitivas y el uso de estructuras de datos simples pero efectivas para optimizar el tiempo de cálculo.
