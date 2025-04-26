# Count the Hidden Sequences

## Descripción

El ejercicio "Count the Hidden Sequences" consiste en determinar cuántas secuencias ocultas posibles pueden generarse a partir de un array de diferencias entre elementos consecutivos. Cada secuencia resultante debe tener sus elementos dentro de un rango específico, definido por los valores `lower` y `upper`. Este tipo de problema es fundamental en áreas relacionadas con la reconstrucción de datos y la manipulación de secuencias, ya que obliga a considerar restricciones tanto en las diferencias como en los valores absolutos de los elementos.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `numberOfArrays`. Este método analiza las variaciones acumuladas en el array `differences` para determinar los valores mínimos y máximos que pueden alcanzar las secuencias, permitiendo así identificar el rango válido de valores iniciales posibles para construir secuencias que respeten los límites indicados.

## Detalles de la implementación

- **Construcción de acumulados:** Recorro el array `differences`, sumando las diferencias sucesivas para obtener el mínimo y máximo de los valores intermedios en la secuencia oculta.
- **Determinación del rango inicial válido:** A partir de los valores mínimos y máximos acumulados, calculo el rango permitido para el primer elemento de la secuencia (`hidden[0]`) de forma que toda la secuencia se mantenga dentro de los límites `[lower, upper]`.
- **Cálculo de secuencias posibles:** Si existe un rango válido, la cantidad de secuencias posibles es igual a la cantidad de enteros dentro de ese rango. Si no existe un rango que satisfaga las restricciones, se devuelve 0.

## Uso

Para utilizar este código, simplemente se debe definir el array `differences` junto con los valores `lower` y `upper`. Posteriormente, se crea una instancia de la clase `Solution`, se llama al método `numberOfArrays` con los parámetros adecuados, y se obtiene como resultado el número de secuencias posibles.

```python
if __name__ == "__main__":
    differences = [1, -3, 4]
    lower = 1
    upper = 6

    sol = Solution()
    possible_sequences = sol.numberOfArrays(differences, lower, upper)
    print(possible_sequences)  # Output: 2
```

## Conclusión

El ejercicio "Count the Hidden Sequences" permite trabajar en la reconstrucción de secuencias basadas en diferencias relativas y rangos absolutos, lo que resulta útil en numerosos contextos como análisis de datos, reconstrucción de señales y control de calidad de datos. La solución propuesta aprovecha un enfoque de recorrido lineal y razonamiento matemático sobre límites acumulativos, logrando así una implementación eficiente incluso para tamaños de entrada grandes, acorde con los requisitos de complejidad de problemas algorítmicos avanzados.
