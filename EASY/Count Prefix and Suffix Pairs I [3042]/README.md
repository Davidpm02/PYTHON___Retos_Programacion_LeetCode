# Count Prefix and Suffix Pairs I

## Descripción

El ejercicio "Count Prefix and Suffix Pairs I" consiste en contar cuántas veces una cadena dentro de una lista es simultáneamente un prefijo y un sufijo de otra cadena en la misma lista. Cada pareja válida de índices `(i, j)` debe cumplir con la condición de que `i < j` y el elemento en la posición `i` sea un prefijo y un sufijo del elemento en la posición `j`.

Este problema se enfoca en la comprensión de conceptos relacionados con substrings y cómo evaluar cadenas bajo condiciones específicas.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que incluye el método principal `countPrefixSuffixPairs`. Este método recorre la lista dada y utiliza una función auxiliar `isPrefixAndSuffix` para determinar si una cadena es a la vez un prefijo y un sufijo de otra cadena.

### Detalles de la implementación

- **Función auxiliar `isPrefixAndSuffix`:**
  - Evalúa si una cadena (`str1`) es prefijo y sufijo de otra cadena (`str2`) utilizando los métodos integrados `startswith` y `endswith` de Python.
  - Retorna `True` si ambas condiciones se cumplen, y `False` en caso contrario.

- **Recorrido principal:**
  - Utiliza dos índices para evaluar todas las posibles combinaciones de cadenas dentro de la lista que cumplen con la condición `i < j`.
  - Incrementa un contador si `isPrefixAndSuffix` devuelve `True` para una combinación particular.

## Uso

Para utilizar este código, es necesario crear una instancia de la clase `Solution` y llamar al método `countPrefixSuffixPairs`, pasando como argumento una lista de cadenas.

```python
if __name__ == "__main__":
    words = ["a", "aba", "ababa", "aa"]

    sol = Solution()
    count = sol.countPrefixSuffixPairs(words)
    print(count)  # Output: 4
```

## Conclusión

El ejercicio "Count Prefix and Suffix Pairs I" ilustra cómo analizar relaciones entre cadenas utilizando propiedades específicas como prefijos y sufijos. La implementación aprovecha funciones nativas de Python para facilitar la detección de estas relaciones, permitiendo realizar evaluaciones precisas y eficientes en una lista de cadenas. Este enfoque no solo ayuda a resolver el problema, sino que también destaca la importancia de un diseño modular en la programación.
