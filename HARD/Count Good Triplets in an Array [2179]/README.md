# Count Good Triplets in an Array

## Descripción

El ejercicio "Count Good Triplets in an Array" consiste en contar el número total de tripletes "buenos" que se pueden formar a partir de dos arrays, `nums1` y `nums2`, ambos de longitud `n` y que son permutaciones del conjunto `[0, 1, ..., n - 1]`. Un triplete `(x, y, z)` se considera bueno si los elementos aparecen en el mismo orden relativo en ambos arrays, es decir:

- `pos1[x] < pos1[y] < pos1[z]`
- `pos2[x] < pos2[y] < pos2[z]`

Donde `pos1[v]` y `pos2[v]` indican la posición del valor `v` en `nums1` y `nums2`, respectivamente.

Este tipo de problema es útil para reforzar el conocimiento sobre estructuras de datos eficientes y técnicas de optimización como Binary Indexed Trees (Fenwick Trees), especialmente en contextos donde se trabaja con grandes volúmenes de datos.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` que contiene el método `goodTriplets`. La clave para resolver este problema de forma eficiente reside en aplicar un enfoque basado en árboles binarios indexados (BIT), que permite contar de manera eficiente el número de elementos menores o mayores en subrangos del array transformado.

## Detalles de la implementación

- **Mapeo de índices:** Primero, se construye un diccionario que mapea cada valor de `nums2` a su índice. Luego se transforma `nums1` en una lista `positions` que representa las posiciones correspondientes en `nums2`.

- **Contadores `left` y `right`:**
  - Para cada índice `i`, `left[i]` representa la cantidad de elementos antes de `i` que también están en orden relativo correcto.
  - Para cada índice `i`, `right[i]` representa la cantidad de elementos después de `i` que también cumplen el orden relativo.
  - La multiplicación de `left[i]` y `right[i]` representa el número de tripletes buenos que tienen como segundo elemento al valor en la posición `i`.

- **Uso de Binary Indexed Tree (BIT):**
  - Se utiliza un BIT para calcular `left[i]` de manera eficiente recorriendo de izquierda a derecha.
  - Posteriormente, se reinicia el BIT y se recorre de derecha a izquierda para calcular `right[i]` y acumular el resultado final.

Este enfoque tiene una complejidad temporal de O(n log n), lo cual es adecuado para los valores máximos de `n` indicados en las restricciones del problema.

## Uso

Para utilizar este código, se deben definir los arrays `nums1` y `nums2`, ambos como permutaciones del conjunto de enteros `[0, ..., n - 1]`. Luego se crea una instancia de la clase `Solution` y se llama al método `goodTriplets`.

```python
if __name__ == "__main__":
    nums1 = [4,0,1,3,2]
    nums2 = [4,1,0,2,3]

    sol = Solution()
    total_good_triplets = sol.goodTriplets(nums1, nums2)
    print(total_good_triplets)  # Output esperado: 4
```

## Conclusión

El ejercicio "Count Good Triplets in an Array" demuestra cómo resolver un problema de conteo de subsecuencias ordenadas en dos listas permutadas usando estructuras avanzadas como los Binary Indexed Trees. Gracias a este enfoque, es posible reducir la complejidad del algoritmo a O(n log n), lo que lo hace escalable para entradas de gran tamaño. Este tipo de técnica es altamente aplicable en problemas de análisis de secuencias y algoritmos competitivos, siendo un excelente ejemplo de cómo optimizar soluciones aparentemente costosas en tiempo.
