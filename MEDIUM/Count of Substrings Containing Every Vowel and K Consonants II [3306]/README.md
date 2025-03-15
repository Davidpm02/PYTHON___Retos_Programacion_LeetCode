# Count of Substrings Containing Every Vowel and K Consonants II

## Descripción

El ejercicio "Count of Substrings Containing Every Vowel and K Consonants II" consiste en contar la cantidad total de subcadenas dentro de una cadena dada `word` que contengan todas las vocales (`'a'`, `'e'`, `'i'`, `'o'`, y `'u'`) al menos una vez y exactamente `k` consonantes.

Este problema es relevante en el análisis de cadenas y en la búsqueda de patrones dentro de texto, aplicando técnicas de preprocesamiento eficiente para mejorar el rendimiento de la solución.

## Implementación

La implementación se realiza en Python mediante una clase `Solution`, que contiene el método `countOfSubstrings`. Este método recorre la cadena, utilizando una estructura de prefijos acumulados para contar las consonantes de manera eficiente y aplicar una búsqueda binaria para encontrar las subcadenas válidas.

### Detalles de la implementación

- **Uso de prefijos acumulados:** Se precalcula un arreglo `prefix_cons` que almacena la cantidad acumulada de consonantes hasta cada posición.
- **Uso de un diccionario para prefijos:** Se almacena la posición de cada valor en `prefix_cons` para facilitar la búsqueda eficiente de subcadenas.
- **Seguimiento de las vocales:** Se mantiene un registro del último índice en el que apareció cada vocal para garantizar que todas están presentes en la subcadena actual.
- **Búsqueda binaria:** Se utiliza `bisect_right` para contar rápidamente cuántos índices de inicio de subcadenas cumplen con la cantidad requerida de consonantes.
- **Complejidad temporal:** La solución tiene una complejidad aproximada de **O(n log n)** debido a la búsqueda binaria aplicada sobre los índices precomputados.

## Uso

Para utilizar este código, se debe definir una cadena `word` y un entero `k`, luego crear una instancia de la clase `Solution` y llamar al método `countOfSubstrings` con estos parámetros.

```python
if __name__ == "__main__":
    word = "ieaouqqieaouqq"
    k = 1
    
    sol = Solution()
    result = sol.countOfSubstrings(word, k)
    print(result)  # Output: 3
```

## Conclusión

El ejercicio "Count of Substrings Containing Every Vowel and K Consonants II" es un problema que combina técnicas de procesamiento eficiente de cadenas con búsqueda binaria y estructuras de datos avanzadas. La solución implementada optimiza la búsqueda de subcadenas válidas utilizando prefijos acumulados y diccionarios de almacenamiento, reduciendo el tiempo de cómputo en comparación con una solución ingenua. Este enfoque es útil en problemas que requieren la búsqueda eficiente de patrones en cadenas grandes.
