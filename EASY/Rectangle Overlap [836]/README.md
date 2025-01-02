# Rectangle Overlap

## Descripción

El ejercicio "Rectangle Overlap" verifica si dos rectángulos, definidos por sus esquinas inferior izquierda y superior derecha en un plano cartesiano, se solapan. Este problema es fundamental en el ámbito de la geometría computacional y encuentra aplicaciones en áreas como gráficos por computadora y detección de colisiones.

### Definición del problema

Un rectángulo está definido como una lista `[x1, y1, x2, y2]`, donde:

- `(x1, y1)` es la coordenada de su esquina inferior izquierda.
- `(x2, y2)` es la coordenada de su esquina superior derecha.

Dos rectángulos se consideran solapados si el área de su intersección es positiva, es decir:

- No deben simplemente tocarse por los bordes o las esquinas.

La función devuelve `True` si los rectángulos se solapan, de lo contrario, retorna `False`.

## Implementación

El problema se resuelve mediante la clase `Solution`, que implementa el método `isRectangleOverlap`. Este método evalúa las condiciones geométricas necesarias para determinar si existe un solapamiento entre los dos rectángulos.

### Detalles de la implementación

- **Condiciones clave para solapamiento:**
  - El lado derecho del primer rectángulo (`rec1[2]`) debe estar a la derecha del lado izquierdo del segundo rectángulo (`rec2[0]`).
  - El lado superior del primer rectángulo (`rec1[3]`) debe estar por encima del lado inferior del segundo rectángulo (`rec2[1]`).
  - Las condiciones inversas deben cumplirse también para el segundo rectángulo.

- **Lógica del método:**
  - Se utiliza un conjunto de comprobaciones lógicas combinadas mediante operadores de comparación para evaluar si las áreas de los rectángulos se superponen.
  - Un bloque de manejo de errores (`try-except`) asegura robustez contra inconsistencias en los datos de entrada.

## Conclusión

El ejercicio "Rectangle Overlap" presenta una solución eficiente para detectar el solapamiento entre dos rectángulos mediante evaluaciones geométricas directas. Este enfoque es claro y utiliza condiciones lógicas bien definidas, lo que lo hace práctico para aplicaciones en geometría computacional. Resolver este problema fortalece habilidades esenciales en el manejo de estructuras de datos y razonamiento lógico.
