# Longest Continuous Increasing Subsequence

## Descripción

El ejercicio "Longest Continuous Increasing Subsequence" tiene como objetivo encontrar la longitud de la subsecuencia más larga de números enteros de una lista no ordenada, en la que los números estén estrictamente en orden ascendente de manera continua. Es decir, debemos identificar la subsecuencia más larga de números consecutivos que estén aumentando.

El concepto de subsecuencia continua creciente se define por dos índices \( l \) y \( r \) (donde \( l < r \)) tal que se cumple la condición:

- \( nums[l] < nums[l + 1] < ... < nums[r] \).

## Implementación

La implementación se realiza en Python utilizando una clase Solution con el método findLengthOfLCIS. Este método recorre la lista de números, calcula las subsecuencias ascendente más largas y retorna su longitud máxima. El código realiza el siguiente proceso:

1. Iteración a través de la lista: Se recorren todos los números del arreglo verificando si cada número es mayor que el anterior (lo que indica que están en orden ascendente continuo).
2. Contabilización de subsecuencias: Si los números están ascendiendo de manera continua, se incrementa el contador de longitud de subsecuencia. Si no lo están, se registra el tamaño de la subsecuencia actual y se reinicia el contador.
3. Retorno de la longitud máxima: Al final, se retorna el tamaño máximo de subsecuencia encontrado.

## Uso

Para utilizar este código, debes crear una instancia de la clase Solution y luego llamar al método findLengthOfLCIS pasando el arreglo de números como parámetro. El resultado será la longitud de la subsecuencia ascendente más larga.

```python
if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    
    sol = Solution()
    result = sol.findLengthOfLCIS(nums)
    print(result)  # Salida: 3
```

## Conclusión

El ejercicio "Longest Continuous Increasing Subsequence" permite practicar la implementación de algoritmos para encontrar subsecuencias en arreglos, lo cual es una habilidad útil en problemas de programación competitiva, procesamiento de señales y análisis de datos secuenciales. El enfoque utilizado es eficiente para listas de longitud moderada, y la implementación muestra cómo gestionar el control de flujos dentro de una secuencia mientras se realiza un seguimiento del tamaño de subsecuencias consecutivas y crecientes.

Este ejercicio también refuerza la comprensión sobre el manejo de subsecuencias dentro de listas y las operaciones de comparación entre elementos consecutivos en una secuencia. La implementación es sencilla pero ilustra conceptos de programación importantes como la iteración, la comparación y el uso de estructuras básicas de Python.
