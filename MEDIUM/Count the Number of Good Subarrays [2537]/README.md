# Count the Number of Good Subarrays

## Descripción

El ejercicio **"Count the Number of Good Subarrays"** consiste en encontrar la cantidad total de subarrays "buenos" dentro de un array de enteros. Un subarray se considera bueno si contiene al menos `k` pares de índices `(i, j)` tales que `i < j` y `nums[i] == nums[j]`. Esta tarea requiere un análisis eficiente de las frecuencias de los elementos y una estrategia de ventana deslizante para recorrer el array de manera óptima, especialmente considerando que la longitud del array puede ser muy grande.

## Implementación

La solución está implementada en Python utilizando una clase `Solution` que define el método `countGood`. Esta función utiliza una técnica de **ventana deslizante** combinada con un diccionario de frecuencias (`defaultdict`) para contar dinámicamente los pares válidos dentro de la ventana actual.

## Detalles de la implementación

- **Estructura de datos usada:** Se emplea un `defaultdict` para llevar un seguimiento de la frecuencia de cada número presente en la ventana actual.
- **Cálculo de pares:** Cada vez que se agrega un número a la ventana, se suman `freq[num]` pares al total, ya que el nuevo número puede formar un par con cada una de sus apariciones previas.
- **Ventana deslizante:** Mientras el número total de pares dentro de la ventana es mayor o igual a `k`, se considera que todos los subarrays que comienzan en la posición actual de `left` y terminan en `right` (inclusive) son válidos. Luego, se intenta minimizar la ventana eliminando elementos desde la izquierda, ajustando el conteo de pares en consecuencia.
- **Complejidad:** El algoritmo recorre el array una sola vez con una complejidad aproximada de O(n), lo que lo hace adecuado para valores grandes de `n`.

## Uso

Para utilizar este código, basta con definir el array de entrada `nums` y el valor `k`, crear una instancia de la clase `Solution`, y llamar al método `countGood`.

```python
if __name__ == "__main__":
    nums = [3,1,4,3,2,2,4]
    k = 2

    sol = Solution()
    result = sol.countGood(nums, k)
    print(result)  # Output esperado: 4
```

## Conclusión

El ejercicio "Count the Number of Good Subarrays" representa un caso práctico de análisis eficiente de subarrays en estructuras de datos grandes. El uso de una ventana deslizante junto con un diccionario de frecuencias permite mantener el control sobre los pares válidos sin necesidad de evaluar cada subarray de forma individual, lo cual sería inviable para grandes volúmenes de datos. Esta solución demuestra cómo aplicar técnicas de optimización para resolver problemas complejos de conteo en arreglos de manera escalable y elegante.
