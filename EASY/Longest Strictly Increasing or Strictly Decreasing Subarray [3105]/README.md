# Longest Strictly Increasing or Strictly Decreasing Subarray

## Descripción

El ejercicio "Longest Strictly Increasing or Strictly Decreasing Subarray" consiste en encontrar la longitud del subarray más largo dentro de una lista de números enteros que sea estrictamente creciente o estrictamente decreciente.

Un subarray es una secuencia contigua de elementos dentro del arreglo original. Un subarray es estrictamente creciente si cada elemento es mayor que el anterior y estrictamente decreciente si cada elemento es menor que el anterior.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `longestMonotonicSubarray`. Este método recorre la lista de números y encuentra todos los subarrays estrictamente crecientes y estrictamente decrecientes, determinando la longitud del más largo de ellos.

### Detalles de la implementación

- **Búsqueda de subarrays crecientes**: Se recorre la lista `nums` acumulando los elementos en un subarray mientras la secuencia siga siendo estrictamente creciente. Cuando la condición se rompe, el subarray se almacena y se comienza uno nuevo.
- **Búsqueda de subarrays decrecientes**: Se repite el proceso anterior, pero verificando que cada elemento sea menor que el anterior.
- **Cálculo de la longitud máxima**: Se comparan las longitudes de los subarrays crecientes y decrecientes obtenidos, devolviendo la mayor de ellas.

## Uso

Para utilizar este código, se debe definir una lista de enteros y luego crear una instancia de la clase `Solution`. Se llama al método `longestMonotonicSubarray` con la lista de números como parámetro y se obtiene la longitud del subarray más largo que sea estrictamente creciente o estrictamente decreciente.

```python
if __name__ == "__main__":
    nums = [1, 4, 3, 3, 2]
    
    sol = Solution()
    max_length = sol.longestMonotonicSubarray(nums)
    print(max_length)  # Output: 2
```

## Conclusión

El ejercicio "Longest Strictly Increasing or Strictly Decreasing Subarray" proporciona una manera eficiente de analizar la estructura de un arreglo de números enteros y determinar la longitud de la secuencia más larga que sigue un patrón de crecimiento o decrecimiento estricto. La solución implementada divide el problema en dos fases independientes (creciente y decreciente), permitiendo un cálculo claro y estructurado. Este tipo de algoritmos es útil en la manipulación y análisis de secuencias de datos en aplicaciones de procesamiento de información y optimización.
