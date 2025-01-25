# Count Servers that Communicate

## Descripción

El ejercicio "Count Servers that Communicate" consiste en determinar la cantidad de servidores que pueden comunicarse entre sí dentro de un centro de servidores. Este centro se representa mediante una matriz binaria donde:

- Un valor `1` en una celda indica la presencia de un servidor.
- Un valor `0` indica que no hay servidor.

Dos servidores pueden comunicarse si están en la misma fila o en la misma columna. Este problema es fundamental en la optimización de redes y comunicaciones dentro de centros de datos.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que incluye el método `countServers`. Este método:

- Mapea la cantidad de servidores por fila y por columna utilizando listas de suma.
- Recorre cada celda de la matriz y determina si el servidor actual puede comunicarse con otros, verificando las filas y columnas asociadas.

### Detalles de la implementación

- **Contar servidores por fila y columna:**
  Utiliza la suma de valores en cada fila y columna para obtener el total de servidores en esas áreas.

- **Verificación de comunicación:**
  Un servidor se considera comunicado si hay más de un servidor en su fila o columna.

- **Complejidad del algoritmo:**
  La solución tiene una complejidad de tiempo O(m * n), siendo m y n las dimensiones de la matriz.

## Uso

Para utilizar este código, solo necesitas definir la matriz binaria que representa el centro de servidores y llamar al método `countServers` de la clase `Solution`. El código devuelve el número de servidores que pueden comunicarse.

```python
from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        """
        Se encarga de contabilizar todos los servidores que se encuentran
        comunicados dentro de una matriz binaria.

        Un 1 en una posición de la matriz indica la presencia de un servidor,
        mientras que un 0 representa la ausencia del mismo.

        params:
            grid (List[List[int]])
        
        returns:
            int
        """

        # Filas y columnas dentro de la matriz
        n, m = len(grid), len(grid[0])

        # Mapeo el número de servidores por fila y columna
        servers_in_rows = [sum(row) for row in grid]
        servers_in_columns = [sum([grid[r][i] for r in range(n)]) for i in range(m)]    

        communicated_servers = 0
        for r in range(n):
            for c in range(m):
                if ((grid[r][c] == 1) and ((servers_in_rows[r] > 1) or (servers_in_columns[c] > 1))):
                    communicated_servers += 1
        return communicated_servers
```

## Conclusión

El ejercicio "Count Servers that Communicate" aborda un problema fundamental en redes y comunicación dentro de infraestructuras tecnológicas. La solución presentada es eficiente y clara, permitiendo determinar de manera óptima cuántos servidores están conectados entre sí mediante la matriz dada. Este tipo de problema refuerza conceptos clave como el procesamiento matricial y el diseño eficiente de algoritmos.
