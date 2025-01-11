# Word Subsets

## Descripción

El ejercicio "Word Subsets" consiste en encontrar las cadenas de texto dentro de una lista `words1` que sean universales con respecto a un conjunto de palabras proporcionado en `words2`. Una palabra se considera "universal" si para cada palabra en `words2`, todas las letras de esa palabra (con sus respectivas frecuencias) están presentes en la palabra de `words1`. Por ejemplo, si una palabra de `words2` tiene una "a" repetida 2 veces, la palabra de `words1` también debe contener 2 o más "a"s para ser considerada universal.

El objetivo es devolver una lista con todas las palabras de `words1` que cumplen con esta condición de ser universales con respecto a `words2`.

## Implementación

La implementación se realiza en Python mediante la clase `Solution` y su método `wordSubsets`. Este método recibe dos listas de cadenas, `words1` y `words2`, y devuelve una lista de las palabras de `words1` que son universales con respecto a `words2`.

### Detalles de la implementación

1. **Contadores de caracteres:** Se utiliza el `Counter` de la biblioteca `collections` para contar las apariciones de cada carácter en las palabras. Esto ayuda a verificar rápidamente si una palabra en `words1` contiene todas las letras de las palabras en `words2`.

2. **Verificación de subsecuencia:** El método interno `isSubset` compara si una palabra de `words1` contiene los caracteres de todas las palabras de `words2` con sus respectivos números de repeticiones. Esta comparación se realiza mediante un ciclo que asegura que cada carácter en la palabra de `words2` esté presente en la palabra de `words1` en las cantidades necesarias.

3. **Combinación de contadores:** Al inicio del procesamiento de `words2`, se combinan los contadores de cada palabra en `words2`, asegurando que los caracteres más frecuentes entre todas las palabras de `words2` sean considerados.

4. **Resultado:** Finalmente, la función recorre las palabras en `words1` y usa la función `isSubset` para determinar si cumplen la condición de ser universales, devolviendo una lista de las palabras que sí lo son.

### Complejidad

- La complejidad temporal de la solución depende tanto de las palabras en `words2` como de las palabras en `words1`. La función `isSubset` recorre todas las letras de cada palabra de `words1`, por lo que la complejidad total puede ser aproximada a \(O(n \times m)\), donde \(n\) es la longitud de `words1` y \(m\) es la longitud promedio de las palabras.

## Uso

Para utilizar este código, se deben proporcionar dos listas de cadenas `words1` y `words2`, luego se debe crear una instancia de la clase `Solution`. Se llama al método `wordSubsets` con estas dos listas, y se obtiene el resultado en forma de una lista de las palabras universales.

```python
if __name__ == "__main__":
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]

    sol = Solution()
    result = sol.wordSubsets(words1, words2)
    print(result)  # Output: ["facebook", "google", "leetcode"]
```

## Conclusión

El ejercicio "Word Subsets" es una excelente manera de practicar el análisis de subsecuencias y frecuencias de caracteres dentro de cadenas de texto. La implementación proporcionada utiliza eficientemente los contadores para comparar las palabras en words1 con las exigencias de words2, logrando encontrar las cadenas que contienen todas las letras necesarias para ser consideradas universales. Este enfoque no solo es efectivo desde el punto de vista de la programación, sino que también demuestra cómo aplicar técnicas de conteo y verificación para resolver problemas prácticos de forma eficiente.
