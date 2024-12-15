# Not Boring Movies

## Descripción

El ejercicio "Not Boring Movies" se centra en filtrar y ordenar las películas de una tabla llamada `Cinema`. Cada película está representada por varias columnas, incluyendo su ID, nombre, descripción y calificación. El objetivo es encontrar las películas cuyo identificador es impar y cuya descripción no sea "boring". Luego, las películas filtradas deben ser ordenadas en función de su calificación de manera descendente.

Este ejercicio es útil en el contexto de consultas sobre bases de datos o análisis de información estructurada en tablas, y también es aplicable en sistemas de recomendación o filtrado de datos con ciertas condiciones.

## Implementación

La implementación se lleva a cabo utilizando **Pandas**, una popular librería de manipulación de datos en Python. Se utiliza el método `.loc` para filtrar las filas del DataFrame según dos condiciones:

1. El ID de la película es impar.
2. La descripción de la película no es igual a 'boring'.

Una vez que se filtran las películas, se ordenan según su calificación en orden descendente utilizando el método `.sort_values()`. Este enfoque es eficiente y permite manejar grandes volúmenes de datos de manera fluida.

### Detalles de la implementación

- **Filtrado:** Se filtran las películas cuya `id` sea impar y cuya descripción no sea "boring".
- **Ordenación:** Se ordenan las películas filtradas por la columna `rating` de forma descendente para mostrar las mejor valoradas primero.
- **Pandas:** Utiliza `pd.DataFrame` para representar la tabla de películas y aplicar las operaciones de filtrado y ordenación.

## Uso

Para utilizar esta solución, simplemente se necesita un DataFrame de Pandas con las columnas `id`, `movie`, `description` y `rating`, representando las películas en el cine. El método `not_boring_movies()` tomará este DataFrame y devolverá las películas que cumplan con las condiciones de ser de ID impar y no tener una descripción "boring", ordenadas por rating.

```python
import pandas as pd

# Ejemplo de cómo utilizar la función

cinema_data = {
    'id': [1, 2, 3, 4, 5],
    'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'],
    'description': ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'],
    'rating': [8.9, 8.5, 6.2, 8.6, 9.1]
}

cinema_df = pd.DataFrame(cinema_data)

result_df = not_boring_movies(cinema_df)

# El resultado será un DataFrame con las películas filtradas y ordenadas por rating
```

## Conclusión

El ejercicio "Not Boring Movies" permite realizar una selección eficiente de películas a partir de un conjunto de datos en una tabla, basándose en condiciones específicas como el ID impar y una descripción que no sea "boring". La implementación aprovecha las capacidades de Pandas para realizar filtrados complejos y ordenaciones, lo que facilita el manejo de grandes conjuntos de datos. Este tipo de ejercicio es relevante en aplicaciones de bases de datos y análisis de datos, y ofrece una forma práctica de trabajar con DataFrames en Python para resolver problemas específicos de filtrado y ordenación.
