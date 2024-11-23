# Classes More Than 5 Students

## Descripción

El ejercicio "Classes More Than 5 Students" consiste en identificar aquellas clases que tienen al menos cinco estudiantes inscritos. A partir de una tabla llamada `Courses`, que contiene dos columnas (`student` y `class`), debemos analizar los datos para determinar qué clases cumplen con el requisito mínimo de estudiantes.

Este ejercicio aborda un problema común en el análisis de datos: filtrar conjuntos de información basándose en condiciones específicas. En este caso, la condición es el número de estudiantes en cada clase.

## Implementación

La solución está implementada en Python utilizando la biblioteca `pandas`. Se define una función `find_classes` que procesa un `DataFrame` con los datos de entrada y retorna otro `DataFrame` con las clases que cumplen con el criterio de tener al menos cinco estudiantes.

### Detalles de la implementación

1. **Conteo de estudiantes por clase:**
   - Se utiliza el método `value_counts()` de `pandas` para calcular la frecuencia de cada clase.

2. **Filtrado de clases con al menos 5 estudiantes:**
   - Se recorre el diccionario generado por `value_counts()` y se seleccionan aquellas clases con una frecuencia mayor o igual a 5.

3. **Creación del DataFrame de salida:**
   - Las clases seleccionadas se almacenan en un nuevo `DataFrame`, con una columna llamada `class`.

## Uso

Para utilizar esta función, se debe proporcionar un DataFrame con la estructura adecuada: dos columnas (student y class). A continuación, se muestra un ejemplo de uso:

```python
import pandas as pd

# Datos de ejemplo
data = {
    "student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "class": ["Math", "English", "Math", "Biology", "Math", "Computer", "Math", "Math", "Math"]
}

# Creación del DataFrame
courses = pd.DataFrame(data)

# Uso de la función
result = find_classes(courses)

# Impresión del resultado
print(result)
```

## Conclusión

El ejercicio "Classes More Than 5 Students" ilustra cómo realizar un filtrado eficiente en un conjunto de datos tabulares utilizando pandas. La solución emplea herramientas fundamentales como value_counts() y comprensión de listas para extraer la información necesaria. Este tipo de análisis es común en tareas de procesamiento y manipulación de datos, y el enfoque mostrado es extensible a problemas más complejos.
