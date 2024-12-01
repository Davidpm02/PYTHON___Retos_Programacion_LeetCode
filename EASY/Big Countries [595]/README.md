# Big Countries

## Descripción

El ejercicio **"Big Countries"** tiene como objetivo identificar los países grandes en función de su área o población a partir de una tabla llamada `World`. Un país se considera grande si cumple al menos una de las siguientes condiciones:

1. Tiene un área de al menos 3,000,000 km².
2. Tiene una población de al menos 25,000,000 habitantes.

El resultado de este ejercicio debe devolver el nombre, la población y el área de estos países en cualquier orden. Este problema es relevante para filtrar y analizar grandes conjuntos de datos tabulares en aplicaciones de análisis de datos y bases de datos.

## Implementación

La solución se implementa en Python utilizando la biblioteca **Pandas**, que es ampliamente utilizada para manipular y analizar datos tabulares.

### Detalles de la implementación

1. **Filtrado de datos:**
   - Se utilizan las capacidades de filtrado de Pandas para seleccionar las filas del DataFrame que cumplen con al menos una de las dos condiciones:
     - `area` mayor o igual a 3,000,000.
     - `population` mayor o igual a 25,000,000.

2. **Selección de columnas:**
   - Se extraen únicamente las columnas `name`, `population` y `area` del DataFrame filtrado para cumplir con el formato del resultado.

3. **Devolución del DataFrame:**
   - El DataFrame resultante contiene solo los países grandes en las columnas requeridas.

## Uso

Para usar esta función, se debe proporcionar un DataFrame de Pandas que contenga la información de los países. El DataFrame debe incluir las columnas name, continent, area, population, y gdp. A continuación, se muestra un ejemplo práctico de cómo utilizar esta función:

```python
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
    "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
    "area": [652230, 28748, 2381741, 468, 1246700],
    "population": [25500100, 2831741, 37100000, 78115, 20609294],
    "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000],
}

world = pd.DataFrame(data)

# Llamar a la función
result = big_countries(world)

# Imprimir el resultado
print(result)
```

## Conclusión

El ejercicio "Big Countries" demuestra cómo filtrar y manipular grandes conjuntos de datos tabulares utilizando Pandas. La solución presentada es eficiente y se enfoca en el cumplimiento de las condiciones específicas del problema, devolviendo un subconjunto de datos relevantes.

Esta práctica refuerza habilidades fundamentales en el manejo de estructuras de datos tabulares y filtros condicionales, los cuales son esenciales para el análisis de datos en Python. Además, ilustra cómo estructurar una solución reutilizable y extensible dentro de proyectos de ciencia de datos y desarrollo de software.
