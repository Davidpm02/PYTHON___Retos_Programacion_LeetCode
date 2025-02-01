# Make Lexicographically Smallest Array by Swapping Elements

## Descripción

El ejercicio "Make Lexicographically Smallest Array by Swapping Elements" consiste en transformar un arreglo de enteros en su versión lexicográficamente más pequeña posible. Para ello, se permite intercambiar dos elementos si y solo si la diferencia absoluta entre ellos es menor o igual a un valor límite dado (`limit`).

Un arreglo `A` es lexicográficamente menor que un arreglo `B` si, en la primera posición donde difieren, el elemento de `A` es menor que el elemento correspondiente en `B`.

## Implementación

La solución se implementa en Python utilizando la estructura de conjuntos disjuntos (Disjoint Set Union, DSU). Se identifican grupos de elementos que pueden intercambiarse entre sí y se ordenan dentro de cada grupo para formar la secuencia lexicográficamente más pequeña posible.

### Detalles de la implementación

- **Estructura de Conjuntos Disjuntos (DSU)**: Se emplea una estructura de conjuntos disjuntos con compresión de caminos y unión por rango para agrupar índices que pueden intercambiarse entre sí.
- **Clasificación de los elementos**: Se ordenan los índices del arreglo con base en sus valores para identificar conexiones entre elementos consecutivos.
- **Unión de conjuntos**: Se conectan los índices si la diferencia entre los elementos correspondientes es menor o igual al `limit`.
- **Reordenación de los elementos dentro de los conjuntos**: Una vez identificados los conjuntos de índices intercambiables, se ordenan los valores dentro de cada conjunto para obtener el arreglo lexicográficamente más pequeño.

## Uso

Para utilizar este código, se debe definir el arreglo de entrada `nums` y el valor de `limit`. Luego, se debe instanciar la clase `Solution` y llamar al método `lexicographicallySmallestArray` con los parámetros adecuados.

```python
if __name__ == "__main__":
    nums = [1, 5, 3, 9, 8]
    limit = 2

    sol = Solution()
    result = sol.lexicographicallySmallestArray(nums, limit)
    print(result)  # Output: [1, 3, 5, 8, 9]
```

## Conclusión

El ejercicio "Make Lexicographically Smallest Array by Swapping Elements" demuestra cómo utilizar estructuras de conjuntos disjuntos para agrupar elementos y ordenarlos eficientemente. La estrategia empleada permite realizar la transformación del arreglo en tiempo eficiente, optimizando los intercambios necesarios para obtener la versión lexicográficamente más pequeña. Esta técnica es útil en problemas de optimización y ordenación restringida dentro de estructuras dinámicas.
