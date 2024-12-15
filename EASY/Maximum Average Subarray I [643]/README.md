# Maximum Average Subarray I

## Descripción

El ejercicio "Maximum Average Subarray I" consiste en encontrar el subarreglo contiguo de longitud `k` dentro de un array de enteros `nums` que tiene el valor promedio máximo. El objetivo es identificar cuál es el subarreglo con la mayor media y devolver ese valor.

Este tipo de problemas es útil en el análisis de series temporales o de datos continuos, donde se requiere identificar el comportamiento promedio dentro de segmentos de datos.

## Implementación

La implementación se realiza en Python mediante la clase `Solution` que contiene el método `findMaxAverage`. Este método recorre el array `nums` buscando subarreglos de longitud `k`, calcula sus promedios y retorna el mayor promedio encontrado.

### Detalles de la implementación

- **Uso de `reduce` para la suma:** Se utiliza la función `reduce` del módulo `functools` para sumar los elementos de cada subarreglo de longitud `k`.
- **Cálculo de promedios:** La suma de cada subarreglo se divide entre `k` para obtener el promedio.
- **Obtención del máximo promedio:** A medida que se encuentran promedios, se mantienen en una lista y se retorna el valor máximo.

## Uso

Para usar este código, basta con crear una instancia de la clase `Solution` y llamar al método `findMaxAverage`, proporcionando el array `nums` y el valor `k` que indica la longitud del subarreglo. El método devolverá el promedio máximo encontrado con un error de cálculo menor a `10^-5`.

```python
if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    sol = Solution()
    max_average = sol.findMaxAverage(nums, k)
    print(max_average)  # Output: 12.75000
```

## Conclusión

El ejercicio "Maximum Average Subarray I" permite encontrar de manera eficiente el subarreglo contiguo con la media máxima dentro de un conjunto de datos. Este tipo de algoritmos son comunes en análisis de datos continuos, como en la evaluación de series temporales. La solución implementada utiliza un enfoque iterativo para calcular promedios de subarreglos de longitud k y luego encuentra el máximo de esos promedios, siendo una solución bastante eficaz y directa para el problema planteado.
