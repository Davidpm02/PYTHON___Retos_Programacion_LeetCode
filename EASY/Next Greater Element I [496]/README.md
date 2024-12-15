# Next Greater Element I

## Descripción

El ejercicio "Next Greater Element I" tiene como objetivo encontrar el primer número mayor que aparece a la derecha de un número dado en una lista. A partir de dos listas de enteros, `nums1` y `nums2` (siendo `nums1` un subconjunto de `nums2`), el reto consiste en buscar para cada elemento de `nums1` su siguiente elemento mayor dentro de `nums2`. Si no existe tal elemento, la respuesta para ese número será -1.

## Implementación

La implementación se realiza en Python a través de la clase `Solution` que contiene el método `nextGreaterElement`. Este método recorre los elementos de `nums1`, los busca en `nums2` y encuentra el siguiente elemento mayor de cada uno, si es que existe. Si no se encuentra un número mayor, se agrega -1 en su lugar. 

La búsqueda de este número mayor en `nums2` se realiza buscando el primer elemento que sea mayor al actual desde la posición inmediata siguiente al índice del número en `nums2`.

### Detalles de la implementación

- **Búsqueda en `nums2`:** Para cada elemento de `nums1`, el código localiza su índice en `nums2` y examina los elementos posteriores de `nums2`.
- **Detección del siguiente mayor:** Una vez encontrado el elemento correspondiente en `nums2`, el código recorre los elementos posteriores para encontrar el primer número mayor que lo siga.
- **Excepciones:** Si no se encuentra ningún número mayor en los elementos siguientes, se agrega -1 al resultado.

## Uso

Para utilizar este código, simplemente se deben definir las listas `nums1` y `nums2`, luego se crea una instancia de la clase `Solution`. El método `nextGreaterElement` se llama pasando ambas listas y devuelve el resultado en una nueva lista.

```python
if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    sol = Solution()
    result = sol.nextGreaterElement(nums1, nums2)
    print(result)  # Output: [-1, 3, -1]
```

## Conclusión

El ejercicio "Next Greater Element I" aborda el problema clásico de la búsqueda del siguiente número mayor en un array. La implementación proporcionada es eficiente para pequeñas y medianas listas y utiliza una técnica básica de búsqueda secuencial para encontrar el siguiente mayor en las sublistas de nums2. Este tipo de ejercicios es útil para practicar habilidades de manipulación de listas y búsqueda dentro de arreglos en Python, y puede extenderse o modificarse para situaciones más complejas en problemas de programación de nivel intermedio.
