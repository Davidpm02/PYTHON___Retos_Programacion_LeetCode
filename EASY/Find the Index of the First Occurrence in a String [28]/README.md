# Find the Index of the First Occurrence in a String

## Descripción

Este ejercicio implementa una función para encontrar el índice de la primera aparición de una cadena (`needle`) dentro de otra cadena (`haystack`). Si `needle` no se encuentra dentro de `haystack`, la función devuelve -1. Esta implementación es útil para entender cómo manejar y buscar subcadenas dentro de cadenas más grandes en programación.

## Implementación

La implementación se realiza en la clase `Solution`, la cual contiene el método `strStr`. Este método acepta dos argumentos de tipo string: `haystack` y `needle`. El objetivo es determinar si `needle` se encuentra dentro de `haystack` y, en caso afirmativo, retornar el índice de la primera aparición. Si `needle` no se encuentra, se devuelve -1.

### Detalles de la Implementación

* **Validación inicial**: Se verifica que la longitud de `needle` no sea mayor que la de `haystack`.
* **Búsqueda**: Se recorre `haystack` y se compara cada subcadena de longitud igual a `needle` hasta encontrar una coincidencia.
* **Retorno**: Se devuelve el índice de la primera coincidencia o -1 si `needle` no se encuentra.

## Uso

Para utilizar esta función, simplemente instancie un objeto de la clase `Solution` y llame al método `strStr`, pasando las cadenas `haystack` y `needle` como argumentos. Por ejemplo:

```python
sol = Solution()
index = sol.strStr("hello", "ll")
print("El índice es:", index)
```

Este código debería imprimir El índice es: 2, que es el índice de la primera aparición de "ll" en "hello".

## Conclusión

Este ejercicio proporciona una buena base para entender cómo se pueden implementar funciones de búsqueda de subcadenas, que son fundamentales en muchas aplicaciones de procesamiento de texto y análisis de datos. La implementación es directa y eficaz para cadenas de longitud moderada.
