# Length of Longest Fibonacci Subsequence

## Descripción

El ejercicio "Length of Longest Fibonacci Subsequence" consiste en encontrar la longitud de la subsecuencia más larga dentro de un array estrictamente creciente de enteros positivos que siga una progresión similar a la secuencia de Fibonacci.

Para que una subsecuencia sea considerada Fibonacci-like, debe cumplir las siguientes condiciones:

- Debe contener al menos 3 elementos.
- La suma de dos elementos consecutivos en la subsecuencia debe ser igual al siguiente elemento en la misma.

Si no se encuentra una subsecuencia de estas características, la función debe retornar 0.

## Implementación

La solución está implementada en Python dentro de la clase `Solution`, la cual contiene el método `lenLongestFibSubseq`.

El algoritmo hace uso de un diccionario para mapear los valores del array con sus respectivos índices, permitiendo una búsqueda eficiente en tiempo O(1). Además, emplea programación dinámica para almacenar la longitud de la subsecuencia Fibonacci-like que termina en un par dado de índices, asegurando una solución eficiente en términos de tiempo y espacio.

## Uso

Para utilizar este código, simplemente se debe definir un array de enteros positivos y crear una instancia de la clase `Solution`. Luego, se llama al método `lenLongestFibSubseq` con el array como argumento y se obtiene la longitud de la subsecuencia Fibonacci-like más larga.

```python
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    
    sol = Solution()
    result = sol.lenLongestFibSubseq(arr)
    print(result)  # Output: 5
```

## Conclusión

El ejercicio "Length of Longest Fibonacci Subsequence" permite explorar el uso de programación dinámica y estructuras de datos eficientes para resolver problemas de subsecuencias en arrays. La solución propuesta optimiza la búsqueda de subsecuencias Fibonacci-like mediante el uso de un diccionario y una estrategia de memoización. Este enfoque resulta útil para trabajar con problemas que involucran patrones numéricos en secuencias ordenadas y demuestra la importancia de una gestión eficiente de datos en estructuras iterativas.
