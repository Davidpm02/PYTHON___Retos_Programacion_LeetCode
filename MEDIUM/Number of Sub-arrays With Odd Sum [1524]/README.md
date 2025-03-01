# Number of Sub-arrays With Odd Sum

## Descripción

El ejercicio "Number of Sub-arrays With Odd Sum" consiste en contar la cantidad de subarrays contiguos dentro de un array dado cuya suma sea un número impar. Debido a que el resultado puede ser muy grande, se debe devolver el valor resultante módulo \(10^9 + 7\).

Este problema es relevante en el análisis de secuencias numéricas y optimización, ya que el uso de subarrays es común en problemas de procesamiento de datos y estructuras dinámicas en programación.

## Implementación

La solución se implementa en Python dentro de una clase `Solution`, que contiene el método `numOfSubarrays`. Este método emplea un enfoque basado en el cálculo de sumas acumulativas para determinar cuántos subarrays tienen una suma impar.

### Detalles de la implementación

- **Uso de sumas acumuladas:** Se mantiene una suma acumulada `prefix_sum` que se actualiza al recorrer el array.
- **Contadores de prefijos pares e impares:** Se utilizan dos contadores (`even_count` e `odd_count`) para registrar la cantidad de sumas acumuladas pares e impares encontradas.
- **Cálculo eficiente:** En cada iteración, se determina si la suma acumulada es par o impar, y se incrementa el resultado en función del número de sumas previas de la categoría opuesta.
- **Optimización con módulo:** Como el resultado puede ser muy grande, se toma el módulo \(10^9 + 7\) en cada paso para evitar desbordamientos.

## Uso

Para utilizar este código, se debe proporcionar un array de enteros positivos y llamar al método `numOfSubarrays` desde una instancia de la clase `Solution`.

```python
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    
    sol = Solution()
    result = sol.numOfSubarrays(arr)
    print(result)  # Output esperado: 16
```

## Conclusión

El ejercicio "Number of Sub-arrays With Odd Sum" demuestra un enfoque eficiente para contar subarrays con una suma impar utilizando sumas acumuladas y contadores de prefijos. En lugar de generar todos los subarrays posibles (lo que resultaría en una complejidad elevada), la solución aprovecha una técnica matemática que reduce el tiempo de ejecución a \(O(n)\), haciéndola escalable para grandes valores de `n`.

Este problema es útil para reforzar conceptos como el uso de sumas acumulativas, contadores de frecuencia y la aplicación del operador módulo en programación competitiva y análisis de datos.
