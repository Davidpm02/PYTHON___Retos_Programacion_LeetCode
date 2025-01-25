# Map of Highest Peak

## Descripción

El ejercicio "Map of Highest Peak" consiste en asignar alturas a las celdas de una matriz que representa un mapa de terreno con agua y tierra, respetando las siguientes reglas:

- Las celdas con agua (`isWater[i][j] == 1`) deben tener una altura de `0`.
- Las alturas asignadas a las celdas deben ser números enteros no negativos.
- La diferencia absoluta de altura entre celdas adyacentes no puede ser mayor a `1`.

El objetivo es maximizar la altura más alta en la matriz, garantizando que se cumplan todas las reglas descritas.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `highestPeak`. Este método sigue los siguientes pasos:

1. **Inicialización de la matriz de alturas:** Se crea una matriz de las mismas dimensiones que `isWater`, inicializada con `-1` para indicar que las celdas aún no han sido procesadas.
2. **Preparación de una cola para BFS:** Todas las celdas de agua (altura `0`) se añaden inicialmente a una cola, ya que estas servirán como puntos de partida para calcular las alturas del resto del mapa.
3. **Propagación con BFS:** Se utiliza un algoritmo de búsqueda en anchura (BFS) para recorrer las celdas adyacentes y asignar sus alturas de manera incremental.
4. **Direcciones adyacentes:** Se manejan las direcciones norte, este, sur y oeste para calcular las alturas de celdas vecinas.
5. **Retorno de la matriz de alturas:** Una vez procesada toda la matriz, se devuelve la matriz resultante con las alturas asignadas.

## Uso

Para utilizar el código, se define la matriz de entrada `isWater` que representa las celdas de agua y tierra. Luego, se crea una instancia de la clase `Solution` y se llama al método `highestPeak`. Este método retorna una nueva matriz con las alturas asignadas.

```python
if __name__ == "__main__":
    isWater = [[0, 1], [0, 0]]

    sol = Solution()
    height = sol.highestPeak(isWater)
    print(height)  # Output: [[1, 0], [2, 1]]
```

## Conclusión

El ejercicio "Map of Highest Peak" utiliza técnicas de búsqueda en anchura (BFS) para resolver un problema de asignación óptima en matrices bidimensionales. La solución es eficiente, ya que cada celda se procesa una sola vez, lo que resulta en un tiempo lineal respecto al número total de celdas. Este enfoque destaca por su simplicidad y efectividad en problemas de propagación y mapeo en estructuras matriciales.
