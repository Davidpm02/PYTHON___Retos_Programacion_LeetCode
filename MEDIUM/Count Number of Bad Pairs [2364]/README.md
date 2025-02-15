# Count Number of Bad Pairs

## Descripción

El ejercicio "Count Number of Bad Pairs" consiste en encontrar el número total de "Bad Pairs" en un array de enteros dado. Se define una "Bad Pair" como un par de índices \((i, j)\) tal que \(i < j\) y \(j - i \neq nums[j] - nums[i]\). El objetivo es contar cuántos pares en el array cumplen esta condición.

## Implementación

La solución implementada en Python utiliza un enfoque basado en el cálculo de diferencias y el uso de una estructura de datos de tipo diccionario para optimizar la búsqueda de "Good Pairs". A continuación, se describen los pasos clave de la implementación:

- **Cálculo del total de pares:** Se obtiene el número total de pares posibles en el array mediante la fórmula combinatoria \( n(n-1)/2 \), donde \( n \) es el tamaño del array.
- **Uso de un diccionario para contar "Good Pairs"**: Se usa un `defaultdict` para llevar el seguimiento de las ocurrencias de la expresión \( i - nums[i] \). Si un valor se ha visto antes, entonces contribuye al número de "Good Pairs".
- **Cálculo de "Bad Pairs"**: Se obtiene restando el número de "Good Pairs" del total de pares posibles.

Este método permite reducir la complejidad del problema a \( O(n) \), lo que lo hace eficiente para grandes valores de \( n \).

## Uso

Para utilizar este código, se debe definir un array de números enteros y luego llamar al método `countBadPairs` de la clase `Solution`.

```python
if __name__ == "__main__":
    nums = [4,1,3,3]
    sol = Solution()
    result = sol.countBadPairs(nums)
    print(result)  # Output: 5
```

## Conclusión

El ejercicio "Count Number of Bad Pairs" permite explorar técnicas eficientes de conteo mediante estructuras de datos como `defaultdict`. En lugar de comparar todos los pares de manera ingenua \( O(n^2) \), se emplea una optimización basada en diferencias y frecuencia para reducir la complejidad a \( O(n) \). Esta solución no solo mejora el rendimiento, sino que también demuestra la utilidad de los diccionarios en problemas de conteo de patrones en estructuras de datos secuenciales.
