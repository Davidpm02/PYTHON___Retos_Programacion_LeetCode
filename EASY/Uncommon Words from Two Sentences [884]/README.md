# Uncommon Words From Two Sentences

## Descripción

El ejercicio "Uncommon Words From Two Sentences" consiste en encontrar aquellas palabras que aparecen solo una vez en un par de cadenas de texto (sentencias). Estas palabras deben aparecer exactamente una vez en una de las cadenas, mientras que no deben aparecer en la otra. El objetivo de este ejercicio es extraer estas palabras únicas y devolverlas en una lista.

Este tipo de operaciones es común en situaciones de procesamiento de texto y manipulación de cadenas, y ayuda a aprender sobre cómo se pueden comparar y analizar diferentes conjuntos de datos a partir de cadenas de texto.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `uncommonFromSentences`. Este método toma dos cadenas de texto como parámetros y devuelve una lista con aquellas palabras que son únicas, es decir, que aparecen una sola vez entre ambas cadenas de entrada.

## Detalles de la implementación

- **Concatenación de cadenas:** Se concatenan ambas cadenas de texto `s1` y `s2` para procesarlas conjuntamente.
- **División en palabras:** Utiliza la función `.split(" ")` para dividir las cadenas en palabras individuales.
- **Conteo de ocurrencias:** Para cada palabra en las cadenas concatenadas, se cuenta cuántas veces aparece en la cadena completa concatenada. Si aparece una sola vez, esa palabra es añadida a la lista de salida.
- **Devolver palabras únicas:** El resultado final es una lista con las palabras que cumplen con el criterio de ser únicas.

```python
if __name__ == "__main__":
    s1 = "this apple is sweet"
    s2 = "this apple is sour"

    sol = Solution()
    uncommon_words = sol.uncommonFromSentences(s1, s2)
    print(uncommon_words)  # Output: ["sweet", "sour"]
```

## Conclusión

El ejercicio "Uncommon Words From Two Sentences" es una excelente manera de practicar la manipulación de cadenas y el análisis de datos. A través de este ejercicio, se pueden explorar técnicas como la concatenación de cadenas, el conteo de elementos y la gestión de listas. Esta implementación demuestra un enfoque simple para encontrar elementos únicos en dos colecciones de texto y es útil en muchas aplicaciones de procesamiento de lenguaje natural y análisis de datos textuales.
