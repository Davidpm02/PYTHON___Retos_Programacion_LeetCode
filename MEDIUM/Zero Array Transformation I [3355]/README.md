# Zero Array Transformation I

## Descripción

El ejercicio **"Zero Array Transformation I"** plantea el reto de determinar si es posible transformar un array de enteros `nums` en un array de ceros tras aplicar un conjunto de operaciones definidas en la lista `queries`.

Cada operación en `queries` representa un rango de índices `[li, ri]` dentro del cual se puede seleccionar un subconjunto de elementos de `nums` y decrementar su valor en uno. Todas las operaciones deben aplicarse secuencialmente y se permite elegir libremente los índices dentro de cada rango.

El objetivo final es verificar si, tras aplicar todas las operaciones, el array `nums` queda completamente lleno de ceros, es decir, si se convierte en un *Zero Array*.

## Implementación

La implementación se realiza en Python dentro de una clase `Solution` que contiene el método `isZeroArray`. Este método toma como entrada el array original `nums` y una lista de consultas `queries`. Para gestionar de forma eficiente los rangos, se hace uso de la técnica de *difference array* junto con un *prefix sum*, lo cual permite procesar todas las consultas en tiempo lineal.

## Detalles de la implementación

- **Difference Array:** Se crea un array auxiliar `diff` con un tamaño de `n+1` (donde `n` es la longitud de `nums`). Este array permite representar la variación acumulada de operaciones en rangos, añadiendo +1 al inicio de un rango y -1 al final.
- **Acumulación con prefix sum:** Se recorre el array `nums`, acumulando las operaciones aplicadas a cada índice. En cada paso se compara si `nums[i]` puede ser reducido con el número de operaciones disponibles. Si no es suficiente, se retorna `False`.
- **Verificación final:** Si todas las posiciones del array pueden ser transformadas en ceros mediante las operaciones acumuladas, se retorna `True`.

## Uso

Para utilizar este código, simplemente se deben definir el array de entrada `nums` y la lista de consultas `queries`, luego crear una instancia de la clase `Solution` y llamar al método `isZeroArray`.

```python
if __name__ == "__main__":
    nums = [1, 0, 1]
    queries = [[0, 2]]

    sol = Solution()
    result = sol.isZeroArray(nums, queries)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Zero Array Transformation I" es una excelente práctica para trabajar con algoritmos de rango y técnicas de optimización como difference arrays y prefix sums. Estas herramientas permiten procesar un alto volumen de consultas de forma eficiente, lo cual es esencial en contextos con restricciones de tiempo y espacio ajustadas. Además, el ejercicio refuerza conceptos fundamentales como el modelado de operaciones acumulativas sobre arrays y la evaluación condicional en estructuras iterativas.
