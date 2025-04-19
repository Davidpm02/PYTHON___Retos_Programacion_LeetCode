# Count the Number of Fair Pairs

## Descripción

El ejercicio **"Count the Number of Fair Pairs"** tiene como objetivo encontrar cuántas parejas de índices (i, j) en un array de enteros `nums` cumplen con una condición específica. Una pareja se considera *válida* si:

- `0 <= i < j < n`
- `lower <= nums[i] + nums[j] <= upper`

Este problema se centra en el conteo eficiente de dichas combinaciones sin exceder los límites de tiempo impuestos por grandes volúmenes de datos, lo que lo convierte en un excelente ejercicio de optimización algorítmica.

## Implementación

La implementación propuesta está desarrollada en Python e incluye una clase `Solution` con el método `countFairPairs`. Este método aplica técnicas de optimización mediante ordenación y búsqueda binaria, con el objetivo de reducir la complejidad temporal del algoritmo a `O(n log n)`, lo cual es esencial dada la posible magnitud del array de entrada (`nums` puede tener hasta 10^5 elementos).

### Detalles de la implementación

- **Ordenación previa del array:** Se ordena el array `nums` para permitir búsquedas binarias eficientes de elementos complementarios que formen sumas válidas.
- **Cálculo de límites:** Para cada elemento `nums[i]`, se calcula el rango `[lower - nums[i], upper - nums[i]]` dentro del cual deben estar los elementos `nums[j]` con `j > i`.
- **Búsqueda binaria:** Se utiliza la librería `bisect` para encontrar la cantidad exacta de elementos dentro de ese rango mediante `bisect_left` y `bisect_right`.
- **Acumulación de resultados:** La cantidad de índices `j` válidos se suma para cada `i` de manera acumulativa.

Este enfoque garantiza que no se exploren todas las combinaciones posibles (lo cual sería ineficiente) y se aprovechan las propiedades del array ordenado para buscar rangos de forma rápida.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution`, proporcionar el array `nums` junto con los valores `lower` y `upper`, y llamar al método `countFairPairs` con estos parámetros:

```python
if __name__ == "__main__":
    nums = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6

    sol = Solution()
    result = sol.countFairPairs(nums, lower, upper)
    print(result)  # Output: 6
```

## Conclusión

El ejercicio "Count the Number of Fair Pairs" pone a prueba la capacidad de optimizar un problema de conteo de pares a través del uso de técnicas como la ordenación y la búsqueda binaria. Gracias a este enfoque, se logra una solución eficiente y escalable que cumple con los requisitos computacionales del problema. Este tipo de desafíos resulta especialmente útil para reforzar conceptos clave en algoritmos avanzados, como el uso de rangos, combinatoria y estructuras de búsqueda optimizadas. Además, resalta la importancia de seleccionar la estructura y técnica adecuada según la naturaleza del problema y los límites impuestos.
