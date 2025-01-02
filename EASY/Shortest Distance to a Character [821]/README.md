# Shortest Distance to a Character

## Descripción

El ejercicio "Shortest Distance to a Character" consiste en encontrar la distancia más cercana de cada carácter de una cadena `s` a una letra específica `c`. La salida del programa es un arreglo de enteros donde cada elemento representa la distancia absoluta entre la posición de un carácter y la posición más cercana de `c`. Este tipo de problema es útil en contextos de análisis de datos y algoritmos relacionados con distancias y localizaciones.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` con el método `shortestToChar`. Este método calcula las distancias más cortas entre cada carácter de la cadena y el carácter objetivo mediante la búsqueda de índices y cálculos de distancia.

### Detalles de la implementación

- **Identificación de posiciones:** Se identifican todas las posiciones en las que el carácter `c` aparece en la cadena `s`.
- **Cálculo de distancias:** Para cada carácter en `s`, se calcula la distancia absoluta entre su posición y todas las posiciones de `c`, seleccionando la más corta.
- **Complejidad computacional:** El método es eficiente para entradas pequeñas y medianas, aprovechando operaciones simples de recorrido y cálculo.

## Conclusión

El ejercicio "Shortest Distance to a Character" proporciona una solución efectiva para calcular distancias relativas dentro de una cadena. Este enfoque refuerza conceptos de programación como iteración, comprensión de listas y optimización de cálculos mediante listas auxiliares. Es una herramienta práctica en análisis de patrones y manipulación de textos, destacándose por su simplicidad y claridad en la implementación.
