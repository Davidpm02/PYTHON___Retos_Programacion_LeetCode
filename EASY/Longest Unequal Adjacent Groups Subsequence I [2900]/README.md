# Longest Unequal Adjacent Groups Subsequence I

## Descripción

El ejercicio **"Longest Unequal Adjacent Groups Subsequence I"** plantea el problema de seleccionar la subsecuencia más larga posible a partir de un array de palabras `words`, cumpliendo una condición de alternancia basada en un segundo array binario `groups`. Cada palabra está asociada a un grupo binario (0 o 1), y la subsecuencia válida es aquella en la que los grupos de dos palabras adyacentes sean distintos entre sí.

Este tipo de problema tiene aplicaciones en contextos donde se busca estructurar datos con alternancia categórica, optimizando la longitud de una secuencia bajo restricciones lógicas simples pero no triviales.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` con un método `getLongestSubsequence`. Este método itera sobre las posibles subsecuencias para construir, mediante programación dinámica, la más larga que cumpla con la condición de alternancia entre los grupos.

### Detalles de la implementación

- **Estructura de datos:** Se utiliza una lista `dp` que guarda tuplas con la longitud actual de la subsecuencia, el valor del último grupo y la propia subsecuencia de palabras.
- **Condición de alternancia:** Se comprueba que `groups[i] != groups[j]` antes de extender una subsecuencia.
- **Actualización óptima:** Solo se actualiza el estado `dp[i]` si se logra una subsecuencia más larga que la almacenada previamente.
- **Resultado final:** Se selecciona la subsecuencia de mayor longitud entre todas las almacenadas en `dp`.

## Uso

Para utilizar este código, se deben definir las listas `words` y `groups`, y luego crear una instancia de la clase `Solution`. El método `getLongestSubsequence` se encarga de retornar la subsecuencia válida más larga según la lógica del problema.

```python
if __name__ == "__main__":
    words = ["a", "b", "c", "d"]
    groups = [1, 0, 1, 1]

    sol = Solution()
    result = sol.getLongestSubsequence(words, groups)
    print(result)  # Ejemplo de salida: ["a", "b", "c"]
```

## Conclusión

El ejercicio "Longest Unequal Adjacent Groups Subsequence I" es un excelente ejemplo de cómo aplicar técnicas de programación dinámica para construir soluciones óptimas bajo restricciones de alternancia. Este tipo de problema permite reforzar conceptos como el diseño de estados dinámicos, optimización de subsecuencias y manipulación de estructuras de datos eficientes. La solución implementada no solo es clara y modular, sino que también es fácilmente extensible a variantes más complejas del problema, haciendo de este ejercicio una práctica valiosa para el desarrollo de habilidades algorítmicas.
