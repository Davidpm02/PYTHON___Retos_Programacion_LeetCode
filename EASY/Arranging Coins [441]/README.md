# Arranging Coins

## Descripción

El ejercicio "Arranging Coins" trata de organizar un número determinado de monedas, `n`, en una estructura de escalera en la que cada fila contiene exactamente el número de monedas equivalente a su número de fila (por ejemplo, la primera fila contiene 1 moneda, la segunda fila contiene 2 monedas, y así sucesivamente). El objetivo es determinar cuántas filas completas se pueden formar utilizando todas o parte de las monedas disponibles.

Este ejercicio es útil en situaciones que implican distribuciones escalonadas o en la solución de problemas de series aritméticas donde el número total de elementos es limitado.

## Implementación

La implementación se realiza en Python mediante una clase `Solution`, que contiene el método `arrangeCoins`. Este método calcula cuántas filas completas de la escalera se pueden construir con el número de monedas `n` dado. El algoritmo utilizado aquí se basa en un bucle `while` que distribuye las monedas por filas en orden creciente hasta que las monedas disponibles se agotan o no se puede completar una nueva fila.

### Detalles de la Implementación

- **Inicialización**: Se inicializan `completed_rows` en 0 para contar las filas completas, y `coins_in_stairs` como una lista que almacena el número de monedas por fila.
- **Distribución de monedas**: En cada iteración del bucle, el programa verifica si `n` contiene suficientes monedas para completar una nueva fila. Si es posible, el número de monedas requeridas para esa fila se añade a `coins_in_stairs`, y `completed_rows` se incrementa.
- **Condición de parada**: Si `n` ya no contiene suficientes monedas para completar la siguiente fila, el bucle termina, y se devuelve el número total de filas completas.

## Uso

Para ejecutar el código, se crea una instancia de la clase `Solution` y se llama al método `arrangeCoins`, pasando como argumento el número de monedas `n`. El método devolverá el número de filas completas de la escalera que se pueden construir con `n` monedas.

```python
if __name__ == "__main__":
    n = 8

    sol = Solution()
    rows_completed = sol.arrangeCoins(n)
    print(rows_completed)  # Output: 3
```

## Conclusión

El ejercicio "Arranging Coins" ilustra un problema común en la programación y la teoría de números, relacionado con la organización en secuencias numéricas crecientes. La solución implementada es directa y eficiente para el propósito del problema, y utiliza una estructura iterativa para distribuir las monedas fila por fila. Este enfoque ofrece un equilibrio entre claridad y rendimiento, especialmente adecuado para el manejo de estructuras escalonadas en programación.
