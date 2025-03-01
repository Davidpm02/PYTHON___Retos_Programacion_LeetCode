# Maximum Absolute Sum of Any Subarray

## Descripción

El ejercicio "Maximum Absolute Sum of Any Subarray" consiste en encontrar la suma absoluta máxima de cualquier subarray dentro de un array dado de números enteros. La suma absoluta se define como el valor absoluto de la suma de los elementos de un subarray específico.

Este problema es útil para entender cómo manejar secuencias de números con valores positivos y negativos, y cómo optimizar la búsqueda de la suma máxima en valor absoluto dentro de una lista de números.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que contiene el método `maxAbsoluteSum`. Este método recorre la lista de números y emplea una estrategia de seguimiento de sumas máximas y mínimas para determinar la máxima suma absoluta posible.

### Detalles de la implementación

- **Seguimiento de la suma máxima:** Se mantiene un valor acumulativo de la suma máxima posible en un subarray.
- **Seguimiento de la suma mínima:** Se rastrea la menor suma acumulativa en un subarray.
- **Comparación de valores:** La respuesta final es el máximo entre la suma absoluta de estos valores acumulativos.
- **Optimización con Kadane’s Algorithm:** Se aprovecha la lógica del algoritmo de Kadane para encontrar la subarray con la máxima y mínima suma de manera eficiente en tiempo O(n).

## Uso

Para utilizar este código, se debe definir la lista de números enteros y luego crear una instancia de la clase `Solution`. Se llama al método `maxAbsoluteSum` con la lista como argumento y se obtiene el resultado de la máxima suma absoluta posible.

```python
if __name__ == "__main__":
    nums = [1,-3,2,3,-4]
    
    sol = Solution()
    max_abs_sum = sol.maxAbsoluteSum(nums)
    print(max_abs_sum)  # Output: 5
```

## Conclusión

El ejercicio "Maximum Absolute Sum of Any Subarray" permite explorar técnicas de optimización para encontrar valores extremos en secuencias numéricas. La implementación presentada es eficiente, con una complejidad temporal O(n), lo que la hace adecuada para grandes conjuntos de datos. Comprender este problema ayuda a reforzar el uso de estrategias como el algoritmo de Kadane y el manejo de valores acumulativos en estructuras iterativas.
