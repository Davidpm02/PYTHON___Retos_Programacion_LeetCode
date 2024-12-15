# Relative Ranks

## Descripción

El ejercicio "Relative Ranks" consiste en asignar rangos a un conjunto de puntuaciones de una competencia. Se deben clasificar los participantes de acuerdo con sus puntuaciones, de la siguiente manera:

- El primer lugar recibe la medalla de oro ("Gold Medal").
- El segundo lugar recibe la medalla de plata ("Silver Medal").
- El tercer lugar recibe la medalla de bronce ("Bronze Medal").
- Los participantes en las posiciones siguientes reciben un rango numérico que representa su posición en el evento (por ejemplo, "4", "5", etc.).

Dado un array de enteros `score`, que representa las puntuaciones de los participantes, se debe retornar un array con los rangos correspondientes a cada participante, en el mismo orden en que aparecen las puntuaciones en el array original.

## Implementación

La implementación se realiza en Python mediante la clase `Solution`, la cual contiene el método `findRelativeRanks`. Este método toma como parámetro un array de enteros representando las puntuaciones y devuelve un array de cadenas que representa la clasificación de los participantes.

### Detalles de la implementación

- **Diccionario de rangos:** Se define un diccionario `first_ranks` para asignar las medallas a las primeras tres posiciones (Oro, Plata y Bronce).
- **Ordenación de puntuaciones:** Se ordenan las puntuaciones en orden descendente para determinar la clasificación de los participantes.
- **Asignación de rangos:** Los primeros tres elementos se asignan las medallas, mientras que el resto de los participantes reciben un número que representa su lugar en el ranking.
- **Actualización del array de puntuaciones:** El array original `score` es actualizado para reflejar los rangos correspondientes a cada participante.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `findRelativeRanks` con el array `score`. Este método devolverá el array con las clasificaciones correspondientes a cada puntuación.

```python
if __name__ == "__main__":
    score = [5, 4, 3, 2, 1]

    sol = Solution()
    ranks = sol.findRelativeRanks(score)
    print(ranks)  # Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
```

## Conclusión

El ejercicio "Relative Ranks" es una excelente forma de trabajar con listas y diccionarios en Python. Este ejercicio no solo pone a prueba habilidades básicas de ordenación y manipulación de listas, sino que también introduce un concepto de ranking basado en puntuaciones. El enfoque implementado es simple y eficiente para manejar listas grandes, manteniendo una complejidad de tiempo que depende de la operación de ordenación. Este ejercicio también demuestra cómo aprovechar las estructuras de datos para optimizar el proceso de asignación de rangos.
