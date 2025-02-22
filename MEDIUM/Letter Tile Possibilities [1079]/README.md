# Letter Tile Possibilities

## Descripción

El ejercicio "Letter Tile Possibilities" consiste en calcular el número total de secuencias no vacías que pueden formarse a partir de las letras impresas en una colección de baldosas. Se pueden utilizar las letras en cualquier orden, y cada baldosa solo puede ser utilizada una vez en cada secuencia.

Este problema es relevante en el contexto de la generación de combinaciones y permutaciones en programación, con aplicaciones en la teoría combinatoria y la generación de palabras o claves en criptografía y análisis de texto.

## Implementación

La solución se implementa en Python utilizando la biblioteca `itertools` para generar permutaciones. Se emplea una clase `Solution` que contiene el método `numTilePossibilities`, el cual calcula el número total de secuencias distintas que pueden formarse a partir de las letras disponibles en la cadena de entrada.

### Detalles de la implementación

- **Uso de permutaciones**: Se generan todas las permutaciones posibles de las letras, considerando diferentes longitudes.
- **Estructura de datos optimizada**: Se usa un conjunto (`set`) para almacenar las permutaciones y eliminar automáticamente duplicados.
- **Iteración sobre longitudes**: Se consideran todas las posibles longitudes de secuencias, desde 1 hasta la longitud total de la cadena.
- **Eficiencia**: Dado que la longitud máxima de `tiles` es 7, el uso de permutaciones es viable dentro de las restricciones del problema.

## Uso

Para utilizar este código, simplemente se debe definir una cadena de texto `tiles` y llamar al método `numTilePossibilities` de la clase `Solution`. A continuación, se muestra un ejemplo de uso:

```python
if __name__ == "__main__":
    tiles = "AAB"
    
    sol = Solution()
    result = sol.numTilePossibilities(tiles)
    print(result)  # Output esperado: 8
```

## Conclusión

El ejercicio "Letter Tile Possibilities" es un problema interesante de combinatoria que se resuelve eficientemente utilizando permutaciones. La estrategia basada en conjuntos permite descartar automáticamente duplicados y simplifica la implementación. Este tipo de problema tiene aplicaciones en análisis de texto, criptografía y generación de secuencias, además de reforzar conceptos fundamentales en programación sobre manejo de conjuntos y combinaciones.
