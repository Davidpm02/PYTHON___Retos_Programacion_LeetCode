# Maximum Count of Positive Integer and Negative Integer

## Descripción

El ejercicio "Maximum Count of Positive Integer and Negative Integer" consiste en determinar cuál es el mayor número entre los enteros positivos y los enteros negativos dentro de un array ordenado en orden no decreciente. En otras palabras, si el número de enteros positivos en `nums` es `pos` y el número de enteros negativos es `neg`, el objetivo es devolver el valor máximo entre `pos` y `neg`.

Cabe destacar que el valor `0` no es considerado ni positivo ni negativo y, por lo tanto, no se cuenta en ninguna de las dos categorías.

## Implementación

La implementación se realiza en Python mediante una clase `Solution`, que contiene el método `maximumCount`. Este método recorre el array `nums`, cuenta la cantidad de enteros positivos y negativos, y devuelve el mayor de estos dos valores.

### Detalles de la implementación

- **Inicialización de contadores**: Se crean dos variables para contar los números positivos y negativos.
- **Recorrido del array**: Se itera sobre `nums` y se actualizan los contadores según el signo de cada número.
- **Cálculo del máximo**: Se retorna el valor máximo entre los contadores de enteros positivos y negativos.

El algoritmo tiene una complejidad de **O(n)**, donde `n` es el tamaño del array `nums`, ya que se realiza un único recorrido sobre la lista.

## Uso

Para utilizar este código, se debe definir una lista de enteros ordenados en orden no decreciente y luego crear una instancia de la clase `Solution`. Se llama al método `maximumCount` con esta lista para obtener el resultado.

```python
if __name__ == "__main__":
    nums = [-2, -1, -1, 1, 2, 3]
    
    sol = Solution()
    max_count = sol.maximumCount(nums)
    print(max_count)  # Output: 3
```

## Conclusión

El ejercicio "Maximum Count of Positive Integer and Negative Integer" es una forma eficiente de contar y comparar la cantidad de enteros positivos y negativos en un array ordenado. Su implementación en Python es directa y aprovecha la simplicidad de un recorrido lineal para obtener el resultado de manera óptima. Esta solución es útil en análisis de datos y problemas de conteo donde la distinción entre valores positivos y negativos es relevante.
