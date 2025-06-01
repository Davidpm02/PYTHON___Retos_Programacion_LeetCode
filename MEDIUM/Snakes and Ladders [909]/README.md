# Snakes and Ladders

## Descripción

El ejercicio "Snakes and Ladders" plantea una simulación del clásico juego de mesa donde se debe llegar desde la primera casilla hasta la última del tablero, minimizando el número de tiradas de dado necesarias. El tablero está representado por una matriz cuadrada de tamaño `n x n`, en la que las casillas están numeradas de forma Boustrophedon, es decir, alternando el sentido de las filas de izquierda a derecha y de derecha a izquierda desde abajo hacia arriba.

Cada tirada de dado puede resultar en un avance de entre 1 y 6 posiciones. Si al llegar a una casilla esta contiene una serpiente o escalera (es decir, su valor no es `-1`), el jugador es trasladado inmediatamente a otra casilla. El objetivo es determinar el mínimo número de movimientos necesarios para alcanzar la última casilla del tablero. Si no es posible alcanzarla, se debe devolver `-1`.

## Implementación

La implementación está desarrollada en Python y consiste en una clase `Solution` con dos métodos principales:

- `_label_to_coords`: Método auxiliar que traduce una etiqueta numérica de casilla (1-indexed) a coordenadas `(fila, columna)` dentro de la matriz `board`. Esta conversión respeta el patrón Boustrophedon de numeración del tablero.
  
- `snakesAndLadders`: Método principal que utiliza una búsqueda en anchura (BFS) para explorar todos los posibles caminos desde la casilla inicial hasta la final, garantizando que se encuentra la solución óptima (es decir, el menor número de movimientos).

### Detalles de la implementación

- **Conversión de casilla a coordenadas:** A través del método `_label_to_coords`, se mapea una casilla numerada a su posición en la matriz considerando la alternancia de dirección en cada fila.
- **Búsqueda BFS:** Se utiliza una cola `deque` para explorar todas las posibles casillas accesibles desde la actual, en función de las tiradas de dado. Se mantiene un conjunto `visited` para evitar revisitar casillas y así prevenir bucles.
- **Manejo de serpientes y escaleras:** Si la casilla resultante de un movimiento contiene un valor distinto de `-1`, el jugador es redirigido automáticamente a dicha casilla destino, respetando la regla de que no se encadenan varias serpientes/escaleras.

## Uso

Para utilizar este código, se debe definir una matriz `board` representando el tablero de juego, y luego crear una instancia de la clase `Solution`. Se llama al método `snakesAndLadders` con esta matriz para obtener el número mínimo de movimientos necesarios para completar el juego.

```python
if __name__ == "__main__":
    board = [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]

    sol = Solution()
    result = sol.snakesAndLadders(board)
    print(result)  # Output: 4
```

## Conclusión

El ejercicio "Snakes and Ladders" combina conceptos clave de programación como el uso de estructuras de datos eficientes (colas, conjuntos) con técnicas de búsqueda (BFS) para resolver un problema de optimización sobre grafos implícitos. La implementación aprovecha la naturaleza estructurada del tablero para realizar una búsqueda sistemática y evitar caminos redundantes, garantizando la obtención de la solución más corta. Este tipo de ejercicios es ideal para afianzar habilidades en manipulación de matrices, simulación de escenarios y resolución de problemas mediante algoritmos clásicos.
