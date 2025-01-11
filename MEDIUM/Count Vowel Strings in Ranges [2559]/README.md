# Count Vowel Strings in Range

## Descripción

El ejercicio "Count Vowel Strings in Range" consiste en procesar consultas sobre un arreglo de cadenas (`words`). Cada consulta indica un rango de índices dentro del arreglo, y el objetivo es determinar cuántas cadenas dentro de ese rango comienzan y terminan con una vocal. Las vocales consideradas son: `a`, `e`, `i`, `o`, `u`.

El resultado del ejercicio es una lista donde cada elemento corresponde al resultado de una consulta, representando la cantidad de cadenas que cumplen la condición dentro del rango especificado.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que incluye el método `vowelStrings`. Este método sigue una estrategia eficiente que reduce el costo computacional, aprovechando el uso de sumas acumuladas (también conocidas como "prefix sums") para responder rápidamente a las consultas.

### Detalles de la implementación

1. **Identificación de vocales:**
   - Se utiliza un conjunto para verificar de manera eficiente si un carácter es una vocal.

2. **Validación de cadenas:**
   - Cada cadena de `words` se evalúa para determinar si tanto su primer carácter como su último carácter son vocales. Esto se almacena en una lista de indicadores binarios (`1` para cadenas válidas y `0` en caso contrario).

3. **Cálculo de sumas acumuladas:**
   - Se genera una lista de sumas acumuladas basada en los indicadores calculados. Esta lista permite obtener rápidamente el número de cadenas válidas en cualquier rango dado.

4. **Resolución de consultas:**
   - Para cada consulta en `queries`, se utiliza la lista de sumas acumuladas para calcular el número de cadenas válidas dentro del rango especificado en tiempo constante.

## Uso

Para utilizar este código, define una lista de palabras y un conjunto de consultas en forma de listas de índices. Llama al método `vowelStrings` proporcionando estos parámetros como entrada.

```python
if __name__ == "__main__":
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0, 2], [1, 4], [1, 1]]

    sol = Solution()
    result = sol.vowelStrings(words, queries)
    print(result)  # Output: [2, 3, 0]
```

## Conclusión

El ejercicio "Count Vowel Strings in Range" es un excelente ejemplo de cómo optimizar el procesamiento de consultas utilizando técnicas avanzadas como las sumas acumuladas. La implementación presentada asegura eficiencia incluso para grandes volúmenes de datos y consultas. Este problema refuerza conceptos importantes relacionados con estructuras de datos, algoritmos de búsqueda y procesamiento por rangos, aplicables en contextos de manipulación de textos y análisis de datos. Su resolución también promueve buenas prácticas en el manejo de listas y conjuntos en Python.
