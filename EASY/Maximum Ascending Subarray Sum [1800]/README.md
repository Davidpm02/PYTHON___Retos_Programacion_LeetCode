# Maximum Ascending Subarray Sum

## Descripción

El ejercicio "Maximum Ascending Subarray Sum" consiste en encontrar la suma máxima posible de una subcadena ascendente dentro de un array de enteros positivos. Una subcadena es una secuencia contigua de números dentro del array original, y se considera ascendente si cada elemento es estrictamente mayor que el anterior.

Este problema es útil para reforzar conceptos sobre la identificación de subsecuencias dentro de listas y la optimización mediante recorridos lineales.

## Implementación

La solución se implementa en Python utilizando una clase `Solution`, que contiene el método `maxAscendingSum`. Este método recorre el array `nums` y construye las subcadenas ascendentes, almacenando sus sumas y devolviendo la máxima de ellas.

## Detalles de la implementación

- **Identificación de subcadenas ascendentes:** Se recorre la lista `nums` y se construyen las subcadenas ascendentes siempre que el siguiente elemento sea mayor que el actual.
- **Cálculo de sumas:** Cada vez que se detecta un número menor o igual al anterior, se almacena la suma de la subcadena actual y se reinicia la acumulación.
- **Obtención del máximo:** Al finalizar el recorrido, se devuelve la mayor de las sumas calculadas.

## Uso

Para utilizar este código, se debe definir un array de enteros positivos y luego crear una instancia de la clase `Solution`. Se llama al método `maxAscendingSum` con el array y se obtiene la suma máxima de una subcadena ascendente.

```python
if __name__ == "__main__":
    nums = [10, 20, 30, 5, 10, 50]
    
    sol = Solution()
    max_sum = sol.maxAscendingSum(nums)
    print(max_sum)  # Output: 65
```

## Conclusión

El ejercicio "Maximum Ascending Subarray Sum" proporciona una manera eficiente de encontrar la subcadena ascendente con la suma más alta dentro de un array de enteros positivos. La solución implementada permite resolver el problema en tiempo lineal, lo que la hace óptima para los límites de entrada establecidos. Este enfoque es útil en diversos contextos de análisis de datos y optimización de secuencias numéricas.
