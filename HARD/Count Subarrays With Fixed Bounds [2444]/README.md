# Count Subarrays With Fixed Bounds

## Descripción

El ejercicio "Count Subarrays With Fixed Bounds" consiste en contar el número de subarreglos dentro de un arreglo de enteros `nums` que cumplan con dos condiciones específicas: el valor mínimo dentro del subarreglo debe ser igual a un valor dado `minK` y el valor máximo dentro del subarreglo debe ser igual a un valor dado `maxK`. Un subarreglo es una parte contigua de un arreglo.

Este tipo de ejercicio es útil para mejorar la comprensión de subarreglos y el manejo de índices en arreglos, especialmente cuando se trata de trabajar con rangos de valores dentro de una secuencia.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `countSubarrays`. Este método recorre el arreglo `nums`, manteniendo un seguimiento de los índices que cumplen con las condiciones necesarias para formar subarreglos válidos.

### Detalles de la implementación

- **Inicialización de índices:** Se mantienen tres índices:
  - `left_bound`: Representa el índice del último elemento fuera del rango `[minK, maxK]`.
  - `last_min`: Representa la última posición donde se encontró el valor `minK`.
  - `last_max`: Representa la última posición donde se encontró el valor `maxK`.
  
- **Iteración sobre el arreglo:** Se recorre el arreglo `nums` para actualizar los índices según los valores encontrados y calcular cuántos subarreglos válidos terminan en la posición actual.

- **Cálculo de subarreglos válidos:** Para cada posición `i`, se calcula el número de subarreglos válidos que terminan en esa posición como la diferencia entre el índice mínimo de las últimas posiciones de `minK` y `maxK` y el `left_bound`.

- **Resultado:** El resultado final es el número total de subarreglos válidos que cumplen con las condiciones especificadas.

## Uso

Para utilizar este código, simplemente se deben definir los valores para el arreglo `nums`, y los valores `minK` y `maxK`. Luego, se crea una instancia de la clase `Solution` y se llama al método `countSubarrays` pasando los valores como parámetros.

```python
if __name__ == "__main__":
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5

    sol = Solution()
    result = sol.countSubarrays(nums, minK, maxK)
    print(result)  # Output: 2
```

## Conclusión

El ejercicio "Count Subarrays With Fixed Bounds" ofrece una manera eficiente de contar subarreglos dentro de un arreglo que cumplen con condiciones específicas sobre los valores mínimo y máximo. La implementación aprovecha el recorrido lineal del arreglo, actualizando solo los índices relevantes para la búsqueda de subarreglos válidos. Este enfoque es eficaz para arreglos grandes y permite obtener el resultado en tiempo lineal, lo cual es esencial para resolver el problema dentro de los límites de tiempo establecidos por las restricciones del problema.

Además, este ejercicio refuerza conceptos clave en programación, como la manipulación de índices, el uso de rangos y la optimización de algoritmos para trabajar con subarreglos.
